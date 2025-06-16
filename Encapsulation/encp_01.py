# --------------------------------------------
# Simple Demonstration of Encapsulation in Python
# Description:
# This script shows how encapsulation works in Python using
# a simple Owner class that manages a private bank balance.
# --------------------------------------------

class Owner:
    # Constructor to initialize owner's name and starting balance
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # private attribute, not accessible directly from outside

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # increase balance
        else:
            print("0 or negative deposit not accepted")  # basic validation

    # Method to withdraw money if sufficient balance is available
    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount  # deduct from balance
        else:
            print("Not sufficient balance or invalid amount.")  # handle errors

    # Getter method to safely access the private balance
    def get_balance(self):
        return self.__balance

    # Setter method to update the balance (used carefully)
    def set_balance(self, newbalance):
        self.__balance = newbalance


# -------------- Usage Example ----------------

# Create an Owner object with initial balance
own = Owner("Anish", 2000)

# Access public attribute
print(own.name)

# Deposit some money
own.deposit(200)
print(own.get_balance())  # Output should be 2200

# Try withdrawing too much money
own.withdraw(16000)       # Should show an error
print(own.get_balance())  # Balance should remain unchanged (2200)

# ----------------------------------------------------
# This example shows how private attributes (like __balance)
# can be accessed and modified safely using getter and setter methods,
# protecting data from unauthorized or invalid operations.
# ----------------------------------------------------
