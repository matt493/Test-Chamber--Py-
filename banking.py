import random
class Person:
    def __init__(self,name,age,occupation):
        self.Name = name
        self.Age = age
        self.Occupation = occupation
    def readData(self):
        self.Name = input("Enter Name : ")
        self.Age = int(input("Enter Age : "))
        self.Occupation = input("Enter Occupation : ")
class BankAccount(Person):
    def __init__(self):
        self.AccountNo = 0
        self.Balance = 0
        self.pin = 0
        self.Transactions = []
    def createAccount(self):
        name = input("Enter name : ")
        age = int(input("Enter Age : "))
        occupation = input("Enter Occupation : ")
        super().__init__(name,age,occupation)
        self.AccountNo = random.randint(1000,9999)
        self.pin = int(input("Enter Pin : "))
        print('----------------------------------')
        print('Account Created !!')
        print("Account Number : ",self.AccountNo)
        print('Pin : ',self.pin)
        print('----------------------------------')
    def withdraw(self):
        amount = int(input("Enter Amount to be withdrawn : "))
        if amount > self.Balance : print("Insufficient Balance !!")
        else:
            print(amount," withdrawn !")
            self.Balance -= amount
            str1 = 'Rs.' + str(amount) + " withdrawn !!"
            self.Transactions.append(str1)
            print("Available Balance : ", self.Balance)
    def deposit(self):
        amount = int(input("Enter amount to be deposited : "))
        self.Balance += amount
        str1 = "Deposited Rs." + str(amount) 
        self.Transactions.append(str1)
        print("Amount deposited !!")
    def checkBalance(self):
        print("Account Balance : ",self.Balance)
    def viewTransactions(self):
        for i in self.Transactions:
            print(i)
    def verifyLogin(self,accountno,pin):
        if self.AccountNo == accountno and self.pin == pin: return True
        else :  return False
no = 0
Accounts = []
condition = False
while 1:
    print("1. Create Account ")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Transactions")
    print("5. Check balance ")
    choice = int(input("Choice : "))
    if choice == 1 :
        Accounts.append(BankAccount())
        Accounts[no].createAccount()
        no += 1
    elif choice == 2 :
        accountno = int(input("Enter Account No. "))
        pin = int(input("Enter Pin "))
        for i in Accounts:
            if i.verifyLogin(accountno,pin):
                print('-------------------------')
                i.deposit()
                print('-------------------------')
                condition = True
                break
        if condition == False: print("Invalid Account No or Pin !!")
        else : condition = True
    elif choice == 3:
        accountno = int(input("Enter Account No. "))
        pin = int(input("Enter Pin "))
        for i in Accounts:
            if i.verifyLogin(accountno,pin):
                condition = True
                print('-------------------------')
                i.withdraw()
                print('-------------------------')
                break
        if condition == False: print("Invalid Account No or Pin !!")
        else : condition = False
    elif choice == 4:
        accountno = int(input("Enter Account No. "))
        pin = int(input("Enter Pin "))
        for i in Accounts:
            if i.verifyLogin(accountno,pin):
                condition = True
                print('-------------------------')
                i.viewTransactions()
                print('-------------------------')
                break
        if condition == False: print("Invalid Account No or Pin !!")
        else : condition = False
    elif choice == 5:
        accountno = int(input("Enter Account No. "))
        pin = int(input("Enter Pin "))
        for i in Accounts:
            if i.verifyLogin(accountno,pin):
                condition = True
                print('-------------------------')
                i.checkBalance()
                print('-------------------------')
                break
        if condition == False: print("Invalid Account No or Pin !!")
        else : condition = False
    elif choice == 6:
        break
    else : print('Invalid Choice!!')