from person import Customer
from account import SavingAccount, CheckingAccount
from gmail import Gmail

"""
Classe que contem os clientes e as contas

Contém metodos de inserção de novos clientes, e criação de contas.

"""



class Bank():
    '''
    Possui uma lista de clientes, uma lista de contas poupança e uma lista de contas corrente
    O banco pode possuir uma ou mais contas e um ou mais clientes
    a classe possui métodos de criação de clientes e contas

    também possui um metodo para verificação de existência de um cliente na lista, passando o seu customer Id para verificação
    e também métodos para verificar se o cliente escolhido para a criação de uma conta, já possui uma conta poupança ou conta correne

    '''
    def __init__(self):
        self.customers = []
        self.saving_accounts = []
        self.checking_accounts = []

    def verify_customer(self, customerId): #verifica se existe o cliente com ID na lista de clientes
        #usado para verificar a existencia do cliente na criação de uma conta
        for customer in self.customers:
            if customer.id == customerId:
                return customer
        print('Customer not defined')
        return None
    def verify_saving_account_customer(self, customerId): #verifica se o determinado cliente, possui uma conta poupança
        #caso ele possua, a conta nao vai poder ser criada
        if len(self.saving_accounts) ==0:
            return True
        for account in self.saving_accounts:
            if account.Customer.id == customerId:
                print(f'customer: {customerId}, already has a saving account')
                return False
            print('sucess bkpt2')
            return True
    def verify_checking_account_customer(self, customerId): #verifica se o determinado cliente, possui uma conta corrente
        #caso ele possua, a conta nao vai poder ser criada
        if len(self.checking_accounts) ==0:
            return True
        for account in self.checking_accounts:
            if account.Customer.id == customerId:
                print(f'Customer: {customerId}, already has a checking account')
                return False
            return True
    def add_customer(self): #método para adicionar um cliente
        firstName = input('First Name: ')
        LastName = input('Last Name: ')
        Age = int(input('Age: ')) #age not <18
        Address = input('Address: ')
        Cpf = input('CPF: ') #format
        Email = input('Email: ') #format

        c = Customer(firstName, LastName, Age, Address, Cpf, Email)
        self.customers.append(c)
        print(f'Added sucessfully customer: {firstName} {LastName} has id {c.id}')
    def add_saving_account(self): #método para adicionar uma conta poupança
        customerId = int(input('Customer ID: '))
        if self.verify_customer(customerId) is not None: #verifica se existe o cliente na lista
            customer = self.verify_customer(customerId)
            if self.verify_saving_account_customer(customerId): #verificando se o usuario ja possui uma conta
                s = SavingAccount(customer)
                self.saving_accounts.append(s) #adiciona a conta criada a lista
                print(f'Sucessfully customer {customer.FirstName} has creating account number: {s.nAccount}')
                return
    def add_checking_account(self): #método para adicionar uma conta corrente
        customerId = int(input('Customer ID: '))
        if self.verify_customer(customerId) is not None: #verifica se existe o cliente na lista
            customer = self.verify_customer(customerId)
            if self.verify_checking_account_customer(customerId): #verificando se o usuario ja possui uma conta
                s = CheckingAccount(customer)
                self.checking_accounts.append(s) #adiciona a conta criada a lista
                print(f'Sucessfully customer {customer.FirstName} has creating account number: {s.nAccount}')
                return

    def list_customers(self): #listar os clientes
        for customer in self.customers:
            print(f'Id: {customer.id} | First Name: {customer.FirstName} | Last Name: {customer.LastName} |'
                  f' Age: {customer.Age} | Cpf: {customer.Cpf} | Address: {customer.Address} | Email: {customer.Email} ')

    def list_accounts(self):
        print('Saving accounts:')
        for sAccounts in self.saving_accounts:
            print(f'Id: {sAccounts.nAccount} | Customer: {sAccounts.Customer} | Balance: R${sAccounts.balance}')
        print('Checking Accounts')
        for cAccounts in self.checking_accounts:
            print(f'Id: {cAccounts.nAccount} | Customer: {cAccounts.Customer} | Balance: R${cAccounts.balance}')


if __name__ == "__main__":
    print(help(CheckingAccount))
    # b = Bank()
    # b.add_customer()
    # b.add_checking_account()
    # b.add_saving_account()
    # print(f'checking accounts: {b.checking_accounts}')
    # print(f'saving accounts: {b.saving_accounts}')
    #
    # b.add_checking_account()
    # b.add_saving_account()



