def selection():
    choice = input("Your choice: ")
    if choice == "1":
        ViewInventory()
    elif choice == "2":
        AddItem()
    elif choice == "3":
        RemoveItem()
    elif choice == "4":
        SearchItem()
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
    count = 0
    inventory = {}

    def __init__(self, name, dose):
        self.name = name
        self.dose = dose

    def __repr__(self):
        return self.name

    @classmethod
    def getinventory(cls, name):
        return cls.inventory.get(name, "Sorry, we do not have that drug in stock")


class Antidepressant(Drug):
    def __init__(self, name, dose):
        super().__init__(name, dose)


class Neuroleptic(Drug):
    def __init__(self, name, dose):
        super().__init__(name, dose)


def ViewInventory():
    print(Antidepressant.inventory)
    print(Neuroleptic.inventory)
    menu()


def AddItem():
    name = input("What's your drug's name? ")
    type = input("What type of drug is it? ")
    type = type.lower()
    dose = input("Specify dose: ")
    if type == "antidepressant":
        Antidepressant.count += 1
        if name not in Antidepressant.inventory.keys():
            Antidepressant.inventory[name] = 1
        else:
            Antidepressant.inventory[name] += 1
    elif type == "neuroleptic":
        Neuroleptic.count += 1
        if name not in Neuroleptic.inventory.keys():
            Neuroleptic.inventory[name] = 1
        else:
            Neuroleptic.inventory[name] += 1
    menu()


def RemoveItem():
    name = input("What's your drug's name? ")
    menu()


def SearchItem():
    name = ("What drug are you looking for? ")
    type = ("What type of drug is it? ")
    type = type.lower()
    if type == "antidepressant":
        Antidepressant.getinventory(name)
    elif type == "neuroleptic":
        Neuroleptic.getinventory(name)
    menu()


menu()

