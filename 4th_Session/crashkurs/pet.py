class Pet():

    def __init__(self, mood=5, hunger=5, energy=5):
        self.mood = mood
        self.hunger = hunger
        self.energy = energy

    def __str__(self):
        return("Haustier. Laune: " + str(self.mood) + ", Hunger: " + str(self.hunger) + \
               ":, Energie: " + str(self.energy))

    def sleep(self):   #den Funktionen der Klasse muss die jeweilige Intanz (das Objekt) übergeben werden
        self.mood += 1
        self.energy += 2

    def feed(self):
        self.mood += 1
        self.hunger -= 1

    def sound(self):
        raise NotImplementedError()

    def play(self):
        self.mood += 1
        self.energy -= 1
        self.hunger += 1
        self.sound()

class Cat(Pet):
    def sound(self):
        print("Miau!")

class Dog(Pet):
    def sound(self):
        print("Wuff!")
