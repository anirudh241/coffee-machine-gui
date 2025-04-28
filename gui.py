import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For adding images
from coffee_machine import CoffeeMachine
from user import UserManager

class CoffeeMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("☕ Coffee Machine")
        self.root.geometry("500x400")
        self.root.configure(bg="#FFF8E7")  # Light cream background
        self.machine = CoffeeMachine()
        self.user_manager = UserManager()
        self.current_user = None

        self.create_login_screen()

    def create_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Load and display logo
        img = Image.open("images/coffee-logo.jpg")  # Ensure this image exists in your images folder
        img = img.resize((100, 100))  # Resize if needed
        self.logo = ImageTk.PhotoImage(img)
        tk.Label(self.root, image=self.logo, bg="#FFF8E7").pack(pady=10)

        tk.Label(self.root, text="Welcome to Coffee Machine!", font=("Helvetica", 20, "bold"), bg="#FFF8E7", fg="#6B4F4F").pack(pady=20)

        tk.Label(self.root, text="Username:", font=("Helvetica", 14), bg="#FFF8E7", fg="#4A4A4A").pack(pady=5)
        self.username_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.username_entry.pack(pady=5)

        tk.Button(self.root, text="Login", font=("Helvetica", 12, "bold"), bg="#D7B49E", fg="white", command=self.login).pack(pady=15)

    def login(self):
        username = self.username_entry.get()
        if username:
            self.current_user = self.user_manager.get_user(username)
            self.show_main_screen()
        else:
            messagebox.showerror("Error", "Please enter a username!")

# In gui.py, update the show_main_screen method
    def show_main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Welcome, {self.current_user.username}!", font=("Helvetica", 18, "bold"), bg="#FFF8E7", fg="#6B4F4F").pack(pady=20)
        
        # Add this to display user balance
        balance_frame = tk.Frame(self.root, bg="#FFF8E7")
        balance_frame.pack(pady=10)

        # Add this to display user balance
        tk.Label(
            self.root, 
            text=f"Your balance: ${self.current_user.balance:.2f}", 
            font=("Helvetica", 14), 
            bg="#FFF8E7", 
            fg="#4A4A4A"
        ).pack(pady=10)

        tk.Button(
        balance_frame,
        text="Add Balance",
        font=("Helvetica", 10),
        bg="#85A389",  # Green color
        fg="white",
        command=self.show_add_balance_dialog
    ).pack(side=tk.LEFT, padx=5)

        # Update this to access drinks through self.menu.drinks
        for drink in self.machine.menu.drinks:
            tk.Button(
                self.root,
                text=f"Order {drink.name.capitalize()} - ${drink.cost}",
                font=("Helvetica", 12),
                bg="#C9ADA7",
                fg="white",
                width=20,
                command=lambda d=drink: self.order(d)
            ).pack(pady=8)

        tk.Button(self.root, text="Refill Machine", font=("Helvetica", 12), bg="#A39393", fg="white", command=self.refill_machine).pack(pady=20)

    def order(self, drink_obj):
    # First check resources
        sufficient, missing_item = self.machine.is_resource_sufficient(drink_obj)
        if not sufficient:
            messagebox.showerror("Resource Error", f"Sorry, not enough {missing_item}!")
            return
        
        # Debug: Print initial balance
        print(f"Initial balance: ${self.current_user.balance}")
        
        # Then check user balance
        if not self.current_user.charge(drink_obj.cost):
            messagebox.showerror("Insufficient Balance", f"You need ${drink_obj.cost:.2f}. Your balance: ${self.current_user.balance:.2f}")
            return
        
        # Debug: Print balance after charge
        print(f"Balance after charge: ${self.current_user.balance}")
        
        # Debug: Print resource levels before making coffee
        print(f"Resources before making coffee: {self.machine.resources}")
        
        # Make coffee if both checks pass
        success, message = self.machine.make_coffee(drink_obj)
        
        # Debug: Print resource levels after making coffee
        print(f"Resources after making coffee: {self.machine.resources}")
        
        if success:
            # Record the purchase
            self.current_user.record_drink(drink_obj.name)
            # Update user data in the manager
            self.user_manager.update_user(self.current_user)
            # Show success message
            messagebox.showinfo("Enjoy!", message)
            # Refresh the screen to show updated balance
            self.show_main_screen()
        else:
            # If making coffee failed for some reason, refund the user
            self.current_user.add_balance(drink_obj.cost)
            self.user_manager.update_user(self.current_user)
            messagebox.showerror("Oops!", message)

    def refill_machine(self):
        additions = {
            "water": 500,
            "milk": 300,
            "coffee": 200
        }
        self.machine.refill(additions)
        messagebox.showinfo("Refilled", "Machine refilled successfully!")


    def show_add_balance_dialog(self):
        # Create a top-level window for the dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Balance")
        dialog.geometry("300x200")
        dialog.configure(bg="#FFF8E7")
        dialog.transient(self.root)  # Make dialog modal
        
        # Center the dialog on the parent window
        dialog.geometry("+{}+{}".format(
            self.root.winfo_rootx() + 100,
            self.root.winfo_rooty() + 100))
        
        tk.Label(
            dialog,
            text="Enter amount to add:",
            font=("Helvetica", 12),
            bg="#FFF8E7"
        ).pack(pady=20)
        
        # Create an entry for the amount
        amount_var = tk.StringVar()
        amount_entry = tk.Entry(dialog, textvariable=amount_var, font=("Helvetica", 12), width=10)
        amount_entry.pack(pady=10)
        amount_entry.focus()  # Set focus to the entry
        
        # Create a frame for the buttons
        button_frame = tk.Frame(dialog, bg="#FFF8E7")
        button_frame.pack(pady=20)
        
        # Add button to confirm
        tk.Button(
            button_frame,
            text="Add",
            font=("Helvetica", 12),
            bg="#85A389",
            fg="white",
            command=lambda: self.add_balance(amount_var.get(), dialog)
        ).pack(side=tk.LEFT, padx=10)
        
        # Add button to cancel
        tk.Button(
            button_frame,
            text="Cancel",
            font=("Helvetica", 12),
            bg="#A39393",
            fg="white",
            command=dialog.destroy
        ).pack(side=tk.LEFT, padx=10)

    def add_balance(self, amount_str, dialog):
        try:
            # Convert the amount to float
            amount = float(amount_str)
            
            # Check if amount is positive
            if amount <= 0:
                messagebox.showerror("Invalid Amount", "Please enter a positive amount.")
                return
            
            # Add the amount to the user's balance
            self.current_user.add_balance(amount)
            
            # Update the user in the manager
            self.user_manager.update_user(self.current_user)
            
            # Show a success message
            messagebox.showinfo("Success", f"${amount:.2f} added to your account.")
            
            # Close the dialog
            dialog.destroy()
            
            # Refresh the main screen to show the updated balance
            self.show_main_screen()
            
        except ValueError:
            # Show an error message if the input is not a valid number
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
def run_app():
    root = tk.Tk()
    app = CoffeeMachineGUI(root)
    root.mainloop()
