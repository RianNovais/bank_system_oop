from abc import ABC,abstractmethod
from itertools import count

# We have the "Person" class as abstract, and there is a daughter class, "Customer".
# each customer that is created will have an id auto incremented by +1, this work is done by an itertools count,
# "Customer" has a repr method defined


proxId = count(start = 1)

g = Gmail()
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
    def __repr__(self):
        return f'({self.FirstName},{self.LastName},{self.Age},{self.Address},{self.Cpf},{self.Email})'


if __name__ == "__main__":
    ...


