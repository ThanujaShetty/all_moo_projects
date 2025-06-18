from abc import ABC,abstractmethod

class Bank(ABC):
    def __init__(self,account_type,users):
        self.account_type = account_type
        self.users = users

    @abstractmethod
    def branch(self):
        pass

    @abstractmethod
    def account_holder(self):
        pass


#implementation for abstract class

class karnataka_bank(Bank):

    def account_holder(self):
        return f"{self.users}has Account with us"

    def branch(self):
        return f"{self.account_type} for user1"

