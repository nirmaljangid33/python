class Bank:
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")

    def show_balance(self):
        print("Current Balance: Rs.", self.balance)


s = Bank(3234, 23435)
s.credit(23343)
s.debit(3423)
s.show_balance()
