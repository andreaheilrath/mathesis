class Vieh:
    def __init__(self, name, alter = 0):
        self.name = name
        self.alter = alter

    def geburtstag(self):
        self.alter += 1

    def __str__(self):
        return tier1.name + ', Alter: ' + str(tier1.alter)

    def __int__(self):
        return self.alter

tier1 = Vieh('Garfield', alter=12)
tier2 = Vieh('Pikatchu', 5)
