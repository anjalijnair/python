fruits=["apple","orange","grapes"]
vegetables=["chilli","cucumber","onion"]
bevereges=["water","milk","tea"]
fruits.append("kiwi")
vegetables.insert(1,"tomato")
print(vegetables)
bevereges.pop()
print(bevereges)
inventory=[fruits,vegetables,bevereges]
print(inventory)
print(fruits[:2])
print(vegetables[-1])
len_list=[len(x) for x in fruits]
print(len_list)
print("water" in bevereges)
allitem_tuple=(fruits[0],vegetables[0],bevereges[0])
print(allitem_tuple)

