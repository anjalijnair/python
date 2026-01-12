from abc import ABC,abstractmethod 
class user(ABC):
    def __init__(self,name,joining_year):
        self.name=name
        self.joining_year=joining_year
    def calculate(self):
        current_year=2025
        return current_year-self.joining_year
    @abstractmethod
    def get_role(self):
        pass
    def display(self):
        print("Name : ",self.name,"\nrole : ",self.get_role(),"\nno of years : ",self.calculate(),"\n")
class customer(user):
    def get_role(self):
        return "customer"
class vendor(user):
    def get_role(self):
        return "vendor"
c=customer("athira",2020)
v=vendor("aravind",2021)
c.display()
v.display()
    

