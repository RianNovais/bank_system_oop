from abc import ABC,abstractmethod
from itertools import count

proxId = count(start = 1)
class Person(ABC):
    def __init__(self, FirstName: str, LastName: str, Age: int, Address: str):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age
        self.Address = Address

class Customer(Person):
    def __init__(self, FirstName, LastName, Age, Address, Cpf, Email):
        super().__init__(FirstName, LastName, Age, Address)
        self.id = next(proxId)
        self.Cpf = Cpf
        self.Email = Email


if __name__ == "__main__":
    c1 = Customer('Rian', 'Muniz', 20, 'Rua Ibicarai', '09984751570', 'riannovais3@gmail.com')
    c2 = Customer('Rian', 'Muniz', 20, 'Rua Ibicarai', '09984751570', 'riannovais3@gmail.com')

    print(c1.id)
    print(c2.id)


