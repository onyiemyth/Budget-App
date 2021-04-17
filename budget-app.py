

class Budget:
    def __init__(self, category, balance):
        self.category = category
        self.balance = balance

    def deposit(self):
        print(f' You Deposited #{self.balance} into {self.category} Category')
    def withdraw(self):
        print(f' You Withdrew #{self.balance} from {self.category} Category')
    def remaining_balance(self):
        print(f' Your Balance on {self.category} Category is #{self.balance}')
    def transfer_from_food(self):
        print(f' Your are transfered #{self.balance} from {self.category} Category to Clothing Category')
    def transfer_from_clothing(self):
        print(f' Your are transfered #{self.balance} from {self.category} Category to Entertainment Category')
    def transfer_from_entertainment(self):
        print(f' Your transfered #{self.balance} from {self.category} Category to Food Category')
        

print('\nHere is the funds deposited into the three categories')    
food_deposit = Budget('Food',10000)
clothing_deposit = Budget('Clothing',2400)
entertainment_deposit = Budget('Entertainment',1000)

food_deposit.deposit()
clothing_deposit.deposit()
entertainment_deposit.deposit()
print()

print('Here is the funds withdrawn from the three categories')           
food_withdrawal = Budget('Food',2000)
clothing_withdrawal = Budget('Clothing',400)
entertainment_withdrawal = Budget('Entertainment',900)

food_withdrawal.withdraw()
clothing_withdrawal.withdraw()
entertainment_withdrawal.withdraw()
print()


print('Here is the Balances for the three categories')
food_balance = Budget('Food',8000)
clothing_balance = Budget('Clothing',2000)
entertainment_balance = Budget('Entertainment',100)

food_balance.remaining_balance()
clothing_balance.remaining_balance()
entertainment_balance.remaining_balance()
print()

print('Here is your transfer details')
food_transfer = Budget('Food',8000)
clothing_transfer = Budget('Clothing',2000)
entertainment_transfer = Budget('Entertainment',100)

food_transfer.transfer_from_food()
clothing_transfer.transfer_from_clothing()
entertainment_transfer.transfer_from_entertainment()
print()

