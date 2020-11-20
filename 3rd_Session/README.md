## 3. Session

### Grundlagen

#### Rekursion

Bei der [rekursiven Programmierung](https://de.wikipedia.org/wiki/Rekursive_Programmierung) ruft sich eine Prozedur, Funktion oder Methode in einem Computerprogramm selbst wieder auf. Es gibt viele Probleme, deren rekursive Formulierung besonders verständlich ist. Allerdings lässt sich, wer rekursiv programmiert, darauf ein, den genauen Ablauf der Ausführung schwer zu durchschauen. 

Ein Beispiel hierfür sind die [Fibonacci-Zahlen](https://de.wikipedia.org/wiki/Fibonacci-Folge). 

Die Fibonacci-Folge ist definiert durch a<sub>0</sub>=1, a<sub>1</sub>=1, a<sub>n+2</sub>=a<sub>n</sub>+a<sub>n+1</sub>

Ruft eine Funktion sehr oft sich selbst auf, kann viel Speicherplatz verbraucht werden. Außerdem ist in Python eine maximale Rekursionstiefe (d.h. wie oft sich eine Funktion selbst aufrufen darf) eingestellt, die sich aber ändern lässt.



Schreiben Sie eine Funktion fib(n) die Ihnen $a_n$ liefert. Berechnen Sie mit dieser Funktion $a_{10}$, $a_{20}$, $a_{30}$ und $a_{35}$.
Was fällt Ihnen auf? Analysieren Sie die Ursache des Problems und schreiben Sie eine zweite Funktion, die diesen Fehler nicht hat.

    def fib(n):
        if n == 0 or n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

    fib(40)

Der Interpreter gestattet nur eine gewisse 'Rekursionstiefe'. Diese lässt sich auslesen mit `sys.getrecursionlimit()` und verändern mit `sys.setrecursionlimit()`.

**Drachenkurve**


#### Other

### Crashkurs

* *[funktionen.ipynb](./crashkurs/funktionen.ipynb)*
  * Definition
  * Doc-Strings
  * Namespaces
  * Keywords, Argumente
  * Rekursion
  
* *[numpy_matplotlib_anderes.ipynb](./crashkurs/numpy_matplotlib_anderes.ipynb)*

* *[formatierung.ipynb](./crashkurs/formatierung.ipynb)*


### Ressourcen

* [numpy Cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
