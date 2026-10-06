class CoffeeMachine:
    def make_coffee(self):
        self._boil_water()
        self._brew_coffee()
        print("Your coffee is ready")

    def _boil_water(self):
        print("Boiling water..")

    def _brew_coffee(self):
        print("Brewed Coffee")

machine = CoffeeMachine()
machine.make_coffee()