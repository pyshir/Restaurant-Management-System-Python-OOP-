# 🍕 Restaurant Management System (Python OOP)
## Author: Jahid, whatsapp: 8801309495010

A simple command-line **Restaurant Management System** built with **Python** using Object-Oriented Programming (OOP) concepts.

This project was created for practicing OOP fundamentals such as **Abstraction, Inheritance, Polymorphism, and Encapsulation**.

---

## 📌 Features

* 📋 Show restaurant menu
* 🍕 Order Pizza (Normal / Extra Cheese)
* 🍔 Order Burger (Basic / Large)
* 🍝 Order Pasta (Normal / Extra Sauce)
* 🧃 Order Juice
* 🛒 Store multiple orders
* ➕ Automatically increase quantity if the same item is ordered again
* 💵 Generate total bill

---

## 🛠️ OOP Concepts Used

* ✅ Abstract Base Class (ABC)
* ✅ Abstract Methods
* ✅ Inheritance
* ✅ Method Overriding
* ✅ Runtime Polymorphism
* ✅ Composition (Restaurant contains Food objects)
* ✅ Encapsulation (Basic)

---

## 📂 Project Structure

```text
restaurant_management/
│
├── main.py
└── README.md
```

---

## 🧩 Class Diagram

```text
               +------------------+
               |   Food (ABC)     |
               +------------------+
               | - name           |
               | - price          |
               +------------------+
               | +show_info()     |
               | +calculate_price()|
               +---------^--------+
                         |
      -----------------------------------------
      |            |            |             |
+-----------+ +-----------+ +-----------+ +-----------+
|  Pizza    | |  Burger   | |   Pasta   | |   Juice   |
+-----------+ +-----------+ +-----------+ +-----------+

                  +--------------------+
                  |    Restaurant      |
                  +--------------------+
                  | - menu             |
                  | - order            |
                  +--------------------+
                  | +show_menu()       |
                  | +place_order()     |
                  | +show_order()      |
                  | +show_bill()       |
                  +--------------------+
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/restaurant-management-system.git
```

Move into the project folder:

```bash
cd restaurant-management-system
```

Run the program:

```bash
python main.py
```

---

## 📖 Sample Menu

```text
1. Pizza
2. Burger
3. Pasta
4. Juice
```

---

## 📸 Sample Output

```text
1. Show menu
2. Order food
3. Show order
4. Show bill
5. Exit

= 1

Name: Pizza, Price: $30, Feature: normal
Name: Burger, Price: $50, Feature: basic
Name: Pasta, Price: $40, Feature: normal
Name: Juice, Price: $10, Feature: basic
```

---

## 🚀 Future Improvements

Some features planned for future versions:

* Add `OrderItem` class
* Add `Menu` class
* Use Composition more effectively
* Apply SOLID Principles
* Add Custom Exceptions
* Use `@property`
* Implement Magic Methods (`__str__`, `__repr__`)
* Save orders to a file/database
* Better input validation
* Graphical User Interface (GUI)

---

## 🎯 Learning Purpose

This project was built to practice Python Object-Oriented Programming and improve software design skills through hands-on implementation.

---

## 📜 License

This project is open-source and available under the MIT License.
