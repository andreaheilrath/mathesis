---
title: Klassen & Objekte
nav_order: 2
parent: 4. Session
permalink: /4th_session/klassen/
---

# Klassen und Objekte

Bisher waren unsere Programme so strukturiert, dass wir dem Rechner nach und nach vorgegeben haben, was er zu tun hat. Diese Form der Anweisung nennt man oft **Prozedurale Programmierung**.
Im Kontrast dazu steht die **Objektorientierte Programmierung** um die es hier gehen soll.

Objekte habt ihr in den letzten Wochen schon kennengelernt. Zum Beispiel habt ihr die _turtle_ benutzt. Eine **Instanz** (synonym zu Objekt) der Klasse _turtle_ verfügt sowohl über einen Zustand (z.B. aktuelle Position) als auch über Aktionen (goto, forward, lt, ...)  - im Allgemeinen werden die **Zustandsvariablen als Attribute** und die **Funktionen als Methoden bezeichnet.**  


**In einer Klasse werden Variablen und Funktionen in einen Container gesteckt und sind somit "verkapselt".**
Eine Klasse ist eine **_Blaupause_** für ein Objekt. Die Klassendeklaration gibt vor, welche Attribute (Variablen) und Methoden (Funktionen) existieren. Verschiedene Instanzen einer Klasse können in verschiedenen Zuständen sein - allerdings zeigen sie alle das gleiche Verhalten, da sie auf die selben Methoden zurückgreifen.

## Klassendeklaration

<img src="https://media1.giphy.com/media/3oriO0OEd9QIDdllqo/200.webp?cid=ecf05e47xps9hzonzme5bgk7gdgobbxxaiktvrjnvn5blonp&rid=200.webp" style="float:right">


So lässt sich eine Klasse erstellen:


    class KlassenName():
        ...
        ...   Deklaration
        ...


#### Ein Beispiel mit Katze:


```python
class Cat():
    """Eine Klasse für Katzen."""

    sounds = ["MiauMiau!"]  #Variable, die von allen Instanzen der Klasse geteilt wird

    def __init__(self): #Funktion die bei der Erstellung einer Instanz aufgerufen wird
        self.mood = 5        #Variablen, die für jede einzelne Instanz erstellt werden
        self.energy = 5
        self.hunger = 5

    def meow(self):
        for sound in self.sounds:
            print(sound)

    def play(self):
        self.mood += 1
        self.energy -= 0.5
        self.hunger += 0.5
        self.meow()
```


```python
miez = Cat()  # Hier wird ein Objekt der Klasse Cat mit dem Variablennamen miez erstellt
```


```python
miez.meow()   # Da miez ein Objekt der Klasse Cat ist, besitzt es die Methode meow
```


```python
miez.play()  # In der Methode .play() wird auch die Methode .meow() aufgerufen
print(miez.mood) # mood ist keine Methode, sondern ein Attribut. Daher wird es ohne Klammern () aufgerufen.
```

<img src="cat_class.png" style="float:right" width=55%>

*Bei der Deklaration von Klassen gibt es einiges zu beachten:*

Den Funktionen muss eine **Referenz auf die jeweilige Instanz der Klasse** übergeben werden: `self`.

Die Funktion `meow` verändert den Zustand der Katze nicht. Es wird nur gemauzt.

Die Funktion `play` verändert den Zustand der Katze, sie wird glücklicher, aber auch müder und hungriger.

Die Funktion `__init__`gehört zu den sogenannten **Special Methods**, von denen wir gleich noch mehr kennenlernen werden. Diese Funktion wird aufgerufen, wenn eine neue Instanz der Klasse erstellt wird, also bei `miez = Cat()`.
Nur die in der Init-Funktion definierten Variablen gehören der Instanz allein, die weiter oben definierte Variable `sounds` wird unter allen Instanzen von `Cat` geteilt!


```python
miez2 = Cat()
```


```python
miez2.sounds.append("maaumau") #das fügt für alle Katzen "maaumau" zur Liste sounds hinzu
```


```python
miez.play()
```


```python

```

Die Syntax die wir bei Klassen verwenden ist der beim Import von Modulen sehr ähnlich.

Die Sinusfunktion des Moduls `math` lässt sich mit `math.sin()` aufrufen - die Konstante Pi mit `math.pi` - wir sehen, dass der Aufruf von Methoden und Attritbuten bei Klassen auch mit einem `.` erfolgt.

Es gibt aber auch noch eine andere Variante die Methoden (=Funktionen) einer Klasse abzurufen:


```python
Cat.meow(miez) #das gleiche wie miez.meow() - nur ausgeschrieben
```

Mit Attributen (=Variablen) geht das nicht ...


```python
Cat.mood(miez)   # das wirft eine Fehlermeldung
```


```python
miez.mood # korrekte Schreibweise
```

### Public and non-Public

In anderen Programmiersprachen sind die Attribute einer Klasse per default _private_ , in diesem Fall dürfen nur die Methoden der Klasse selbst die Attribute verändern. In Python sind alle Attribute von außen abruf- und veränderbar.

Mit doppelten unterstrichen vor dem Variablennamen kann eine Variable jedoch "versteckt" werden.


```python
class Cat():
    """Eine Klasse für Katzen."""

    sounds = ["MiauMiau!"]

    def __init__(self):
        self.mood = 5        # kein Unterstrich: public
        self._energy = 5   # ein Unterstrich: soll wie non-public behandelt werden
        self.__hunger = 5  # doppelter Unterstrich: non-public

    def meow(self):
        for sound in self.sounds:
            print(sound)

    def play(self):
        self.mood += 1
        self._energy -= 0.5
        self.__hunger += 0.5
        self.meow()

    def sleep(self):
        self.mood += 1
        self._energy += 2

    def feed(self):
        self.mood += 1
        self.__hunger -= 1
```


```python
private_miez = Cat()
```


```python
private_miez.mood
```


```python
private_miez.mood = 0
```


```python
private_miez._energy # eine so benannte Variable abzurufen ist schlechter Stil
```


```python
private_miez.__hunger # Variablen mit doppeltem Unterstrich können nicht abgerufen werden
```


```python
private_miez.feed()
```

### Special (\Magic \Dunder) Methods

Es gibt spezielle Methoden die im Kontext von Klassen benutzt werden können, diese werden durch doppelte Unterstriche gekennzeichnet (Dunder = double under).

    __init__  # "Konstruktor" zum Erstellen es Objekts
    __str__   # Definiert, wie das Objekt durch die print() Funktion dargestellt wird
    __len__   # Definiert, was die len() Funktion auf dem Objekt zurückgibt

    __getitem__ #getitem und setitem ermöglichen das Zugeifen auf Einträge via Indizes
    __setitem__ #dann lässt sich auch über das Objekt iterieren (wie bei Listen, Arrays, ...)


... und noch einige mehr siehe z.B. [hier]("https://www.tutorialsteacher.com/python/magic-methods-in-python"). Mehr dazu in den Beispielen.



```python
class Cat():

    def __init__(self, mood = 5, hunger = 5, energy = 5):
        self.mood = mood
        self.hunger = hunger
        self.energy = energy

    def __str__(self): ## Definiere die Print-Ausgabe des Objekts
        return("Katze. Laune: " + str(self.mood) + ", Hunger: " + str(self.hunger) + \
               ", Energie: " + str(self.energy))

    def sleep(self):   #den Funktionen der Klasse muss die jeweilige Intanz (das Objekt) übergeben werden
        self.mood += 1
        self.energy += 2

    def play(self):
        self.mood += 1
        self.energy -= 1
        self.hunger += 1
        self.meow()

    def feed(self):
        self.mood += 1
        self.hunger -= 1

    def meow(self):
        print("MiauMiau")
```


```python
miez2 = Cat(mood = 3, hunger = 4, energy = 5) #wir können die Miez jetzt in einem gewählten Zustand initialisieren!
print(miez2.hunger)
```


```python
print(miez) #Ohne __str__ Magic Method (Objekt von oben)
print("\n")
print(miez2) #mit __str__ Das ist hübscher!
```

<img src = "Pet_inheritance.png" style="float:right" width=55%>

### Vererbung (inheritance)

Klasseneigenschaften lassen sich auch an andere Klassen vererben, die Definition sieht dann wie folgt aus:

     class KlassenName(AndereKlasse):
        ...
        ...   Deklaration
        ...   

Angenommen wir möchten nun auch eine Klasse zu Hunden haben. Eine Variante möglichst Effizient zu arbeiten ist alle Eigenschaften die Katze und Hund gemeinsam haben in einer übergeordneten Klasse `Pet` zusammenzufassen.


```python
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
```


```python
class Cat(Pet):

    def meow(self):
        print("MiauMiau")

    def play(self):
        self.mood += 1
        self.energy -= 1
        self.hunger += 1
        self.meow()

class Dog(Pet):

    def bark(self):
        print("WauWau!")

    def play(self):
        self.mood += 1
        self.energy -= 1
        self.hunger += 1
        self.bark()
```


```python
rex = Dog()
garfield = Cat()
```


```python
rex.play()
```


```python
garfield.sleep()
print(garfield.mood)
```

### Polymorphismus (Vielgestaltigkeit)

Hier soll noch erwähnt sein, dass Funktionen aus der Elternklasse auch **überschrieben** werden können. Dies kann man unter anderem dafür nutzen, dass die selbe Methode bei ähnlichen Objekten verschiedene Resultate liefert - deshalb polymorph.

Hier das Gleiche wie oben nur anders.


```python
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
```


```python
rex = Dog()
garfield = Cat()
```


```python
rex.play()
```


```python
garfield.play()
```

### Python Code auslagern

Funktionen und auch Klassen lassen sich in gesonderten `.py` Dateien speichen und über `import` laden. Die oben stehende Klassendeklaration habe ist in der Datei `pet.py` gespeichert und kann wie folgt verwendet werden:


```python
import pet as p
```


```python
katze = p.Cat()
```


```python
katze.play()
```

### Abstraktion

Zum Schluss sei noch angemerkt welchen enormen Vorteil Objektorientierte Programmierung noch bietet - Vereinfachung durch Abstraktion! Meist will User garnicht wissen, welche Codeberge sich hinter Methoden verbergen. **Mit möglichst sprechenden Attributen und Variablen wird ein Programm extrem aufgeräumt und bedienbar, obwohl es sehr komplex sein mag.**

Damit haben wir die grundlegenden Konzepte hinter Objektorientierer Programmierung abgedeckt:
* Verkapselung
* Abstraktion
* Vererbung
* Polymorphismus

Einige Beispiele und Konzepte sind aus [diesem FreeCodeCamp Post]("https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/") entnommen.



```python

```


```python

```
