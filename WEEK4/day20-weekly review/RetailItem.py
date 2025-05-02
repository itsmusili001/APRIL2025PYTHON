# This code is for a retail item class that stores information about an item in a retail store.
class RetailItem:
    def __init__(self, description, quantity,price):
        self.description = description
        self.quantity = quantity
        self.price = price
class CashRegister:
    def __init__(self,itemList):
        self.itemList = itemList
    def purchase_item(self, item):
        self.itemList.append(item)
    def get_total(self):
        total = 0
        for item in self.itemList:
            total += item.price 
        return total 
    def show_items(self):
        for item in self.itemList:
            print(f"Description: {item.description}\nQuantity in the inventory: {item.quantity}\nPrice: kshs{item.price:.2f}\n")
    def clear_items(self):
        self.itemList.clear()
        
        

