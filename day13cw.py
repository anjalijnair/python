item=input("Enter the stationary items :")
try:
    with open("items.txt","a") as file:
        file.write(item+"\n")
    #file.close()
    print("Item added successfully")
    print("List the stationar items :")
    with open("items.txt","r") as file:
        for x in file:
            print(x)
    #file.close()
except Exception as e:
    print("An error occured")



