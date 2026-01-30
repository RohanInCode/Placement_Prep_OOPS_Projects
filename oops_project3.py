class libraryitem:
    def __init__(self,days):
        self.days=days
    def book_charge(self): # METHOD WILL BE OVERRIDDEN 
        pass

class Book(libraryitem): #INHERITANCE
    def book_charge(self): 
        return self.days * 10
class Magzine(libraryitem):
    def book_charge(self):
        return self.days * 10

class LibraryApp: #HAS-A RELATION
    def __init__(self, name, days):
        self.name = name
        self.item_duration = Book(days)  

    def show(self):
        print("Item Type:", self.name)
        print("Days borrowed:", self.item_duration.days)
        print("Total Charge:", self.item_duration.book_charge())

app = LibraryApp("Magzine", 4)
app.show()
