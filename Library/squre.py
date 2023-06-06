class Account:

    def __init__(self, money):
        self.balance = money

        
    @property
    def balanceInDollars(self):
        return self.balance/70


s1 = Account(1000)
s1.balance = 2000
print(s1.balanceInDollars)