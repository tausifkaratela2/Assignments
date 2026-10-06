#Different classes can use the exact same method name but each implements in its own way.

class Bird:
    def speak(self):
        return "Chirp..."

class Cat:
    def speak(self):
        return "Meow"

def make_animal_speak(animal):
    print(animal.speak())

make_animal_speak(Bird())
make_animal_speak(Cat())