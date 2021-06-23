class User():
    def _init_(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("personal detail")
        print("")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender", self.gender)

Aparna = User('Aparna', 21, 'female')
Aparna.show_details()

class Bank(User):
    def _init_(self, name, age, gender):
        super()._init_(name, age, gender)
        self.balance = 0


    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("The amount has been updated: RS ",self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount> self.balance:
            print("insufficient fund | Available balance is: RS",self.balance)
        else:
            print("The updated balance is: RS",self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance",self.balance)

Aparna = Bank('Aparna', 20, 'female')
Aparna.deposit(1000)
Aparna.withdraw(100)
Aparna.withdraw(1100)
Aparna.view_balance()