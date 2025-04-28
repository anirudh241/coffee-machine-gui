# ☕ Coffee Machine GUI Project

This project is a **Python-based Coffee Machine** simulator with a graphical user interface (GUI) using **Tkinter**. It allows users to log in, order coffee, track their drink history, manage their balance, and refill the coffee machine inventory.

---

## ✨ Features

- **User Login:**  
  Users can log in with their username. If a username does not exist, it is automatically created.

- **Order Drinks:**  
  Users can order different types of coffee such as espresso, latte, and cappuccino.

- **User Balance Tracking:**  
  Each user has a balance. The cost of each drink is deducted automatically after each order.

- **Add Balance Feature:**  
  Users can easily **add money to their balance** via a dedicated "Add Balance" option.  
  > ✅ This allows users to continue purchasing drinks even after their balance runs low.

- **Drink History:**  
  The app tracks how many times each drink has been ordered by each user.

- **Inventory Management:**  
  The coffee machine tracks available water, milk, and coffee supplies. Admins can **refill** inventory when needed.

- **Persistent Data Storage:**  
  All user balances and drink histories are saved in a local `users.json` file, ensuring that data persists even after the program closes.

- **Simple and Clean GUI:**  
  Built with Tkinter, the GUI is intuitive, easy to navigate, and styled with a clean aesthetic.

---

## 📂 Project Structure

```
coffee-machine-gui/
├── data/
│   ├── users.json       # Stores user data (balance, drink history)
│   └── inventory.json   # Stores coffee machine inventory
├── utils/
    ├──file_io.py
├── coffee_machine.py           # CoffeeMachine class (handles drinks and resources)
├── user.py              # User and UserManager classes (handles user accounts)
├── gui.py               # GUI Application built using Tkinter
├── main.py              # Entry point to run the app
├── drink.py
├── menu.py
└── README.md            # Project documentation
```

---

## 🚀 How to Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/coffee-machine-gui.git
   cd coffee-machine-gui
   ```

2. **Install Python (if not already installed):**  
   Make sure you have **Python 3.x** installed.

3. **Install Required Libraries:**
   - Tkinter usually comes pre-installed with Python. If not, install via:
     ```bash
     pip install tk
     ```

4. **Run the App:**
   ```bash
   python main.py
   ```

---

## 🛠️ Future Enhancements (Optional Ideas)

- Add a login system with passwords.
- Implement admin privileges for refilling inventory.
- Add animations or sound effects on drink preparation.
- More detailed balance history and transaction logs.

---

## 📜 License

This project is open source and free to use.

