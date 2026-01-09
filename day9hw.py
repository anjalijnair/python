class account:
    def __init__(self,_name,_balance):
        self._name=_name
        self._balance=_balance
    def __add__(self,other):
        return self._balance+other._balance
class savingsaccount(account):
    def calculate_interest(self):
        return self._balance*0.05
class currentaccount(account):
    def calculate_interest(self):
        return self._balance*0.02

s=savingsaccount("ravi",10000)
c=currentaccount("anjali",15000)
print("savings accaount")
print("name",s._name)
print("balance",s._balance)
print("interest",s.calculate_interest())
print("\ncurrent account")
print("name",c._name)
print("balance",c._balance)
print("interest",c.calculate_interest())
total_balance=s+c
print("\ntotal balance: ",total_balance)