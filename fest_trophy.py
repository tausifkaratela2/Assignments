class Player:
    def __init__(self, name):
        self.name = name
        self.bag = []

    def collect(self, item):
        if item in self.bag:
            print(f"You already have the {item}.")
            return
        self.bag.append(item)
        print(f"You put the {item} in your bag.")

    def show_bag(self):
        if self.bag:
            print("You are carrying: " + ", ".join(self.bag))
        else:
            print("Your bag is empty.")


class Place:
    def __init__(self, name, description, needs=None, item=None):
        self.name = name
        self.description = description
        self.needs = needs     
        self.item = item       

    def visit(self, player):
        if self.needs and self.needs not in player.bag:
            print(f"The {self.name} is locked. You need the {self.needs}.")
            return False
        print(f"{self.name}: {self.description}")
        return True


class Chest:
    def __init__(self, code):
        self.code = code

    def open(self, player):
        if self.code in player.bag:
            print("The chest opens... the trophy is found!")
            return True
        print("The chest stays shut. You need the code.")
        return False


def build_world():
    player = Player("Tausif")
    canteen = Place("Canteen", "Tables everywhere. A key is hidden under one of them.",
                    item="key")
    lab = Place("Computer Lab", "Rows of computers. A secret code is written on one.",
                needs="key", item="code")
    stage = Place("Main Stage", "The empty stand where the trophy should be. The chest is here.")
    chest = Chest("code")
    return player, canteen, lab, stage, chest


def failed_route():
    print("========== FAILED ROUTE ==========")
    player, canteen, lab, stage, chest = build_world()
    stage.visit(player)
    chest.open(player)
    lab.visit(player)
    player.show_bag()


def winning_route():
    print("\n========== WINNING ROUTE ==========")
    player, canteen, lab, stage, chest = build_world()
    canteen.visit(player)
    player.collect("key")
    if lab.visit(player):
        player.collect("code")
    stage.visit(player)
    chest.open(player)
    player.show_bag()


def play():
    print("\n========== PLAY IT YOURSELF ==========")
    player, canteen, lab, stage, chest = build_world()
    places = {"1": canteen, "2": lab, "3": stage}

    while True:
        print("\nWhere do you want to go?")
        print("1. Canteen   2. Computer Lab   3. Main Stage   4. Check bag   5. Quit")
        choice = input("> ").strip()

        if choice == "5":
            print("Thanks for playing.")
            break
        elif choice == "4":
            player.show_bag()
        elif choice in places:
            place = places[choice]
            if place.visit(player):              
                if place.item and place.item not in player.bag:
                    answer = input(f"Take the {place.item}? (y/n) ").strip().lower()
                    if answer == "y":
                        player.collect(place.item)
                if place is stage:
                    if chest.open(player):
                        break                    
        else:
            print("Please enter a number from 1 to 5.")


failed_route()
winning_route()

if input("\nWant to play it yourself? (y/n) ").strip().lower() == "y":
    play()