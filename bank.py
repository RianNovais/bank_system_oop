from person import Customer
from account import SavingAccount, CheckingAccount

class Bank():
    '''
     has a list of customers, a list of savings accounts and a list of current accounts
     The bank may have one or more accounts and one or more customers
     the class has methods for creating customers and accounts

     also has a method for checking the existence of a customer in the list, passing their customer Id
     for verification and also methods to verify that the customer chosen for creating an account,
     already have a savings or checking account
    '''
    def __init__(self):
        self.customers = []
        self.saving_accounts = []
        self.checking_accounts = []

    def verify_customer(self, customerId): #Check if the customer with ID exists in the customer list
        #used to check the existence of the customer when creating an account
        for customer in self.customers:
            if customer.id == customerId:
                return customer
        print('Customer not defined')
        return None
    def verify_saving_account_customer(self, customerId): #Check if a customer has a savings account
        #if he does, the account cannot be created
        if len(self.saving_accounts) ==0:
            return True
        for account in self.saving_accounts:
            if account.Customer.id == customerId:
                print(f'customer: {customerId}, already has a saving account')
                return False
            print('sucess bkpt2')
            return True
    def verify_checking_account_customer(self, customerId): #Check if the customer has a current account
        #if he does, the account cannot be created
        if len(self.checking_accounts) ==0:
            return True
        for account in self.checking_accounts:
            if account.Customer.id == customerId:
                print(f'Customer: {customerId}, already has a checking account')
                return False
            return True
    def add_customer(self): #method to add a customer
        firstName = input('First Name: ')
        LastName = input('Last Name: ')
        Age = int(input('Age: ')) #age not <18
        Address = input('Address: ')
        Cpf = input('CPF: ') #format
        Email = input('Email: ') #format

        c = Customer(firstName, LastName, Age, Address, Cpf, Email)
        self.customers.append(c)
        print(f'Added sucessfully customer: {firstName} {LastName} has id {c.id}')
    def add_saving_account(self): #method for adding a savings account
        customerId = int(input('Customer ID: '))
        if self.verify_customer(customerId) is not None: #check if the customer exists in the list
            customer = self.verify_customer(customerId)
            if self.verify_saving_account_customer(customerId): #check if the user already has an account
                s = SavingAccount(customer)
                self.saving_accounts.append(s) #add the created account to the list
                print(f'Sucessfully customer {customer.FirstName} has creating account number: {s.nAccount}')
                return
    def add_checking_account(self): #method for adding a current account
        customerId = int(input('Customer ID: '))
        if self.verify_customer(customerId) is not None: #check if the customer exists in the list
            customer = self.verify_customer(customerId)
            if self.verify_checking_account_customer(customerId): #checking if the user already has an account
                s = CheckingAccount(customer)
                self.checking_accounts.append(s) #add the created account to the list
                print(f'Sucessfully customer {customer.FirstName} has creating account number: {s.nAccount}')
                return

    def list_customers(self): #list the clients
        for customer in self.customers:
            print(f'Id: {customer.id} | First Name: {customer.FirstName} | Last Name: {customer.LastName} |'
                  f' Age: {customer.Age} | Cpf: {customer.Cpf} | Address: {customer.Address} | Email: {customer.Email} ')

    def list_accounts(self): #list the accounts
        print('Saving accounts:')
        for sAccounts in self.saving_accounts:
            print(f'Id: {sAccounts.nAccount} | Customer: {sAccounts.Customer} | Balance: R${sAccounts.balance}')
        print('Checking Accounts')
        for cAccounts in self.checking_accounts:
            print(f'Id: {cAccounts.nAccount} | Customer: {cAccounts.Customer} | Balance: R${cAccounts.balance}')

    def search_account(self, accNumber): #find the account with its number, used in the function of withdrawing and
        # depositing from a given account
        for accounts in self.saving_accounts:
            if accounts.nAccount == accNumber:
                account = accounts
        for accounts in self.checking_accounts:
            if accounts.nAccount == accNumber:
                account = accounts
        return account

if __name__ == "__main__":
    ...




