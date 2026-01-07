inventory=[]
def add_item(item):
    inventory.append(item)
def count_items(items):
    if items==[]:
        return 0
    else:
        return 1+count_items(items[1:])
def main():
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")
    show_items=lambda item:print("item in stock: ",item)
    for item in inventory:
        show_items(item)
    total_count=count_items(inventory)
    print("total no of items: ",total_count)
main()