import RetailItem
item1=RetailItem.RetailItem("Jacket",12,59.95)
item2=RetailItem.RetailItem(price=34.95,description="Designers Jeans",quantity=40)#using keyword arguments
item3=RetailItem.RetailItem("Shirt",20,24.95)

def get_menu_choice():
    print()
    print("1. select items of purchase")
    print("2. Show items purchased")
    print("3. Show total amount of purchase")
    print("4. Clear items purchased")
    print("5. Exit")

    choice=int(input("Enter your choice: "))
    return choice

def main():
    itemList = []

    choice=0
    while choice != 5:
        choice = get_menu_choice()
        if choice == 1:
            item = input("Enter item to purchase (1-jacket,2-designer jeans,3-shirt): ")
            if item == "1":
                itemList.append(item1)
            elif item == "2":
                itemList.append(item2)
            elif item == "3":
                itemList.append(item3)
            else:
                print("Invalid choice")
        elif choice == 2:
            print("Items purchased:")
            for item in itemList:
                print(f"Description: {item.description}\nQuantity in the inventory: {item.quantity}\nPrice: kshs{item.price:.2f}\n")
        elif choice == 3:
            total = 0
            for item in itemList:
                total += item.price 
            print(f"Total amount of purchase: kshs{total:.2f}")
        elif choice == 4:
            itemList.clear()
            print("Items purchased cleared")
        else:
            print("exiting program")
main()