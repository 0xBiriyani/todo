class myAccount:
    def __init__(self, name, account_number, balance=1000):
        self.name = name
        self.account_number= account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance>= amount:
            self.balance = self.balance- amount
            return True
        else:
            return False
        
    def Showdetails(self):
        print(f"Customer Name :{self.name}\nAccount Number :{self.account_number}\nAccount Balance :{self.balance}")
    
    def transfer(self,other, amount):
        if self.withdraw(amount):
            other.deposit(amount)
            print(f"Transfer Successful:{amount} debited , current balance {self.getbalance()} ")
        else:
            print("Transfer failed due to insuficient balance")
    
    def getbalance(self):
            return self.balance
        
customer1= myAccount("priyanka", 1000105678,10000)  
customer2= myAccount ("kalyan",1000106789, 10000) 
# cus_list=[Customer1,customer2]
# for i in cus_list:
#     if i.name=="kalyan":
#         i.withdraw(1000000)
#     i.Showdetails() 
# customer2.transfer(customer1, 1000000)
# print(customer2.getbalance())
# print(customer1.getbalance())     
customer1.transfer(customer1, 1000)
print(customer2.getbalance())
print(customer1.getbalance())    