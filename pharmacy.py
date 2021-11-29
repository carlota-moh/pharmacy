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
        else:
            cls.inventory[name] += 1

    @classmethod
    def remove_drug(cls, name):
        if name not in cls.inventory.keys():
            print("Sorry, we do not have that drug in stock")
        elif cls.inventory[name] == 1:
            cls.inventory.pop(name)
        else:
            cls.inventory[name] = cls.inventory[name] - 1

    @classmethod
    def search_drug(cls, name):
        print(cls.inventory.get(name, "Sorry, we do not have that drug in stock"))


class Antidepressant(Drug):
    inventory = {}

    def __init__(self, name):
        super().__init__(name)


class Neuroleptic(Drug):
    inventory = {}

    def __init__(self, name):
        super().__init__(name)


def view_items():
    Drug.view_inventory()
    menu()


def add_item():
    name = input("What's your drug's name? ").capitalize()
    dtype = input("What type of drug is it? ").lower()
    Drug.add_drug(name)
    if dtype == "antidepressant":
        Antidepressant.add_drug(name)
    elif dtype == "neuroleptic":
        Neuroleptic.add_drug(name)
    menu()


def remove_item():
    name = input("What's your drug's name? ").capitalize()
    dtype = input("What type of drug is it? ").lower()
    Drug.remove_drug(name)
    if dtype == "antidepressant":
        Antidepressant.remove_drug(name)
    elif dtype == "neuroleptic":
        Neuroleptic.remove_drug(name)
    menu()


def search_item():
    Drug.search_drug(name)
    menu()

if __name__ == "__main__":
    menu()