from abc import ABC,abstractmethod 
class user(ABC):
    def __init__(self,name,year):
        self.name=name
        self.creation_year=year
    def account_age(self):
        return 2025-self.creation_year
    @abstractmethod
    def get_role(self):
        pass
class admin(user):
        def get_role(self):
            return "admin"
        def __str__(self):
            return f"{self.name} is an admin user"
class guest(user):
        def get_role(self):
            return "guest"
        def __str__(self):
            return f"{self.name} is a guest user"
A=admin("avani",2021)
G=guest("anu",2022)
print("Admin User")
print(A)
print("Role :",A.get_role())
print("Account Age : ",A.account_age())
print("\nGuest Role")
print(G)
print("Role : ",G.get_role())
print("Account age",G.account_age())


