class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.int_rate * self.balance)
        else:
            print("invalid")
        return self
class User:
    
    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def display_info(self):
        print(f"Name: {self.name}\nEmail: {self.email}")
        return self

        
    def display_user_balance(self):
        self.account.display_account_info()

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

user1 = User("Joe","joesmith@comcast.net")
user1.display_info().make_deposit(300).make_withdrawal(200).display_user_balance()
user2 = User("Ryan","rkochen@comcast.net")
user2.display_info().make_deposit(700).make_withdrawal(160).display_user_balance()

