import json
from datetime import datetime
# Path of JSON file where all bank data will be stored
DATA_FILE = "E:\\python\\BankingSystem\\bank_data.json"# Enter your correct file path


def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


class Account:
    def __init__(self, acc_no, name, pin, balance=0, transactions=None):
        self.__acc_no = acc_no
        self.name = name
        self.__pin = pin
        self.__balance = balance
        self.transactions = transactions if transactions else []

    def check_pin(self, pin):
        return self.__pin == pin

    def credit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        self.__balance += amount
        self._add_txn(f"Credited Rs {amount}")
        print(f"Rs {amount} credited successfully")

    def debit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            self._add_txn(f"Debited Rs {amount}")
            print(f"Rs {amount} debited successfully")

    def show_balance(self):
        print(f"Current Balance: Rs {self.__balance}")

    def _add_txn(self, msg):
        time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
        self.transactions.append(f"{time} | {msg}")

    def to_dict(self):
        return {
            "acc_no": self.__acc_no,
            "name": self.name,
            "pin": self.__pin,
            "balance": self.__balance,
            "transactions": self.transactions
        }


class Bank:
    def __init__(self):
        self.data = load_data()

    def create_account(self):
        try:
            acc_no = input("Enter Account Number: ")
            if acc_no in self.data:
                print("Account already exists")
                return
            name = input("Enter Name: ")
            pin = input("Set 4-digit PIN: ")
            balance = int(input("Enter Initial Balance: "))
            if balance < 0:
                print("Balance cannot be negative")
                return

            acc = Account(acc_no, name, pin, balance)
            self.data[acc_no] = acc.to_dict()
            save_data(self.data)
            print("Account created successfully")
        except ValueError:
            print("Invalid input")

    def login(self):
        acc_no = input("Enter Account Number: ")
        pin = input("Enter PIN: ")

        acc_data = self.data.get(acc_no)
        if not acc_data or acc_data["pin"] != pin:
            print("Invalid account or PIN")
            return

        acc = Account(**acc_data)
        self.account_menu(acc)
        self.data[acc_no] = acc.to_dict()
        save_data(self.data)

    def account_menu(self, acc):
        while True:
            print("\n1. Credit\n2. Debit\n3. Balance\n4. Transactions\n5. Logout")
            ch = input("Choose: ")

            if ch == '1':
                acc.credit(int(input("Amount: ")))
            elif ch == '2':
                acc.debit(int(input("Amount: ")))
            elif ch == '3':
                acc.show_balance()
            elif ch == '4':
                for t in acc.transactions:
                    print(t)
            elif ch == '5':
                break
            else:
                print("Invalid choice")

    def main_menu(self):
        while True:
            print("\n--- BANK SYSTEM ---")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            ch = input("Choose: ")

            if ch == '1':
                self.create_account()
            elif ch == '2':
                self.login()
            elif ch == '3':
                print("Thank you")
                break
            else:
                print("Invalid choice")


bank = Bank()
bank.main_menu()