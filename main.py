
import bank

'''
Classe principal
Aqui possui o menu para interação com o usuário
'''

print('Bank System')
b = bank.Bank()

while True:
    choiceUser = int(input('Choice an option: \n1-Add customer\n2-Add Account\n3-List Customers\n4-List Accounts\n5-Choice an account\n6-EXIT\n'))

    if choiceUser == 1:
        b.add_customer()

    elif choiceUser == 2:
        typeAccount = int(input('1 - Saving Account\n2 - Checking Account\n'))
        if typeAccount == 1:
            b.add_saving_account()
        elif typeAccount == 2:
            b.add_checking_account()
    elif choiceUser == 3:
        b.list_customers()

    elif choiceUser == 4:
        b.list_accounts()

    elif choiceUser == 5:
        accNumber = int(input('Number of the account'))
        account = b.search_account(accNumber)

        choiceTransaction = int(input('Choice an option:\n1 - Deposit an account | 2 - Withdraw an account '))
        if choiceTransaction == 1:
            value = float(input('Value to deposit: '))
            account.deposit(value)
        if choiceTransaction == 2:
            value = float(input('Value to withdraw: '))
            account.withdraw(value)
        else:
            print('Choice an valid option')

        ...



    elif choiceUser == 6:
        break

    else:
        print('Choice an valid option')

    ...




