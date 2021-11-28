def selection():
    choice = input("Your choice: ")
    if choice == "1":
        view_items()
    elif choice == "2":
        add_item()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        search_item()
    elif choice == "5":
        print("Have a nice day!")
    else:
        print("Sorry, I did not understand you")
        selection()


    def menu():
        print("--- WELCOME TO THE PHARMACY ---")
        print("Choose one option: ")
        print("1. View inventory")
        print("2. Add drug")
        print("3. Remove drug")
        print("4. Search drug")
        print("5. Exit")
        print("--------------------------------")
        selection()

class Drug:
    inventory = {}

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


    @classmethod
    def view_inventory(cls):
        print(cls.inventory)


    @classmethod
    def add_drug(cls, name):
        if name not in cls.inventory.keys():
            cls.inventory[name] = 1
            print(cls.inventory)
        else:
            cls.inventory[name] += 1
            print(cls.inventory)


    @classmethod
    def remove_drug(cls, name):
        if name not in cls.inventory.keys():
            print("Sorry, we do not have that drug in stock")
        elif cls.inventory[name] == 1:
            cls.inventory.pop(name)
        else:
            cls.inventory[name] = cls.inventory[name] - 1



class Antidepressant(Drug):
    inventory = {}
    def __init__(self, name, dose):
        super().__init__(name, dose)


class Neuroleptic(Drug):
    inventory = {}
    def __init__(self, name, dose):
        super().__init__(name, dose)

def view_items():
    Drug.view_inventory()
    menu()


def add_item():
    name = input("What's your drug's name? ")
    dtype = input("What type of drug is it?").lower()
    Drug.add_drug(name)
    if dtype == "antidepressant":
        Antidepressant.add_drug(name)
    elif dtype == "neuroleptic":
        Neuroleptic.add_drug(name)
    menu()


def remove_item():
    name = input("What's your drug's name? ")
    dtype = input("What type of drug is it?").lower()
    Drug.remove_drug(name)
    if dtype == "antidepressant":
        Antidepressant.remove_drug(name)
    elif dtype == "neuroleptic":
        Neuroleptic.remove_drug(name)
    menu()


def search_item():
    name = ("What drug are you looking for? ")
    dtype = ("What type of drug is it? ")
    dtype = dtype.lower()
    if dtype == "antidepressant":
        Antidepressant.get_inventory(name)
    elif dtype == "neuroleptic":
        Neuroleptic.get_inventory(name)
    menu()

menu()

