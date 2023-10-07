from abc import ABC,abstractmethod
from itertools import count
from gmail import Gmail
nAccount = count(start = 1)

g = Gmail()
class Account(ABC):
    def __init__(self, Customer: int):
        self.nAccount = next(nAccount)
        self.Customer = Customer
        self.balance = 0

    @abstractmethod
    def deposit(self, value: int):
        ...

    @abstractmethod
    def withdraw(self, value: int):
        ...


class SavingAccount(Account):
    def __init__(self, Customer):
        super().__init__(Customer)
        self.Overdraft = False

        g.send_mail_new_account_saving(self.Customer.FirstName, self.Customer.Email)

    def deposit(self, value):
        if not value <=0:
            self.balance += value
            print(f'R${value} deposit sucessfully completed')
            return
        print('invalid value')

    def withdraw(self, value):
        def withdraw(self, value: int):
            if self.Overdraft is True:
                if (self.balance - value) < 0:
                    userChoice = input('Overdraft: [Y/N]')
                    if userChoice.lower() == 'y':
                        self.balance = self.balance - value
                        print(f'Sucessfully withdraw: R${value}, actual balance is R${self.balance}')
                        return
                    else:
                        print('Impossivel sem o cheque especial')
                        return
                self.balance = self.balance - value
                print(f'Sucessfully withdraw: R${value}, actual balance is R${self.balance}')
                return
            if (self.balance - value) < 0:
                print('Insufficient funds')
                return
            self.balance = self.balance - value
            print(f'Sucessfully withdraw: R${value}, actual balance is R${self.balance}')


class CheckingAccount(Account):
    def __init__(self, Customer):
        super().__init__(Customer)
        self.Overdraft = True

        g.send_mail_new_account_checking(self.Customer.FirstName, self.Customer.Email)

    def deposit(self, value):
        if not value <=0:
            self.balance += value
            print(f'R${value} deposit sucessfully completed')
            return
        print('invalid value')

    def withdraw(self, value: float):
        if self.Overdraft is True:
            if (self.balance - value) <0:
                userChoice = input('Overdraft: [Y/N]')
                if userChoice.lower() == 'y':
                    self.balance = self.balance - value
                    print(f'Sucessfully withdraw: R${value} an account id: {self.nAccount}, actual balance is R${self.balance}')
                    return
                else:
                    print('Impossible without overdraft')
                    return
            self.balance = self.balance - value
            print(f'Sucessfully withdraw: R${value}, actual balance is R${self.balance}')
            return
        if (self.balance - value) < 0:
            print('Insufficient funds')
            return
        self.balance = self.balance - value
        print(f'Sucessfully withdraw: R${value}, actual balance is R${self.balance}')


if __name__ == "__main__":
    cc = CheckingAccount(12)
    print(cc.balance)
    cc.deposit(10)
    cc.withdraw(10)
    cc.withdraw(1)







