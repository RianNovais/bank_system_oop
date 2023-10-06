from person import Customer
from account import SavingAccount, CheckingAccount
from gmail import Gmail



class Bank():
    def __init__(self):
        self.customers = []
        self.accounts = []
