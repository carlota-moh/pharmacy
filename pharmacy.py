def selection():
    choice = input("Your choice: ")
    if choice == "1":
        view_inventory()
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
    count = 0
    inventory = {}

    def __init__(self, name, dose):
        self.name = name
        self.dose = dose

    def __repr__(self):
        return self.name

    @classmethod
    def get_inventory(cls, name):
        return cls.inventory.get(name, "Sorry, we do not have that drug in stock")


class Antidepressant(Drug):
    count = 0
    inventory = {}
    def __init__(self, name, dose):
        super().__init__(name, dose)


class Neuroleptic(Drug):
    count = 0
    inventory = {}
    def __init__(self, name, dose):
        super().__init__(name, dose)


def view_inventory():
    print(Drug.inventory)
    print(Antidepressant.inventory)
    print(Neuroleptic.inventory)
    menu()


def add_item():
    dtype = input("What type of drug is it? ")
    dtype = dtype.lower()
    Drug.count += 1
    if dtype == "antidepressant":
        drug = Antidepressant(name = input("What's your drug's name? "), dose = input("Specify dose: "))
        Antidepressant.count += 1
        if drug.name not in Antidepressant.inventory.keys():
            Antidepressant.inventory[drug.name] = 1
            Drug.inventory[drug.name] = 1
        else:
            Antidepressant.inventory[drug.name] =+ 1
            Drug.inventory[drug.name] += 1
    elif dtype == "neuroleptic":
        drug = Neuroleptic(name = input("What's your drug's name? "), dose = input("Specify dose: "))
        Neuroleptic.count += 1
        if drug.name not in Neuroleptic.inventory.keys():
            Neuroleptic.inventory[drug.name] = 1
            Drug.inventory[drug.name] = 1
        else:
            Neuroleptic.inventory[drug.name] =+ 1
            Drug.inventory[drug.name] += 1
    menu()


def remove_item():
    name = input("What's your drug's name? ")
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

