import random
rice_price,sugar_price,oil_price=45,40,130
rice_quantity,sugar_quantity,oil_quantity=3,2.5,1.8
rice_total=rice_quantity*rice_price
sugar_total=sugar_quantity*sugar_price
oil_total=oil_quantity*oil_price
print("total price of rice",rice_total)
print("total price of sugar",sugar_total)
print("total price of oil",oil_total)
final_bill=rice_total+sugar_total+oil_total
print("The final bill of all products",final_bill)
final_bill_int=int(final_bill)
print("final bill in integer",final_bill_int)
final_bill_str=str(final_bill)
print("final bill in string",final_bill_str)
delivery_charge=random.randrange(5, 10)
print("Final bill including delievry charges",final_bill+delivery_charge)
