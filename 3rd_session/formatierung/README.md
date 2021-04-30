# Ausgaben formatieren

Bisher haben wir das so gemacht: 

    s = 'Katze'
    a = 11
    print("Die "+ s + " ist " +str(a) +" Jahre alt.")

Oft aber wollen wir mehr, wir wollen etwa eine gewisse Zahl von Nachkommastellen für `float`-Zahlen, mit oder ohne vorzeichen etc.

Es gibt für String-Objekte, das Platzhalter enthält, die Methode 'format', der man eine beliebige Anzahl von Argumenten übergeben kann, die dann nach gewissen Regeln für die Platzhalter eingesetzt werden. Im einfachsten Fall werden Sie nach der Reihenfolge eingesetzt:


```python
print("Die Länge der {} ist {} {}".format('Strecke', 213.12312, 'Meter'))
```

    Die Länge der Strecke ist 213.12312 Meter
    


```python
print("Die Länge der {:10s} ist {:.2f} {:10s}.".format(
    'Strecke', 213.12312, 'Meter'))
# Strings in Felder der Länge 10 einsetzen, Fließkommazahl mit zwei Nachkommastellen.
```

    Die Länge der Strecke    ist 213.12 Meter     .
    


```python
print("Die Länge der {} ist {:.2e} {}".format('Strecke', 213.12312, 'Meter'))
```

    Die Länge der Strecke ist 2.13e+02 Meter
    

Die einfachste Version von Platzhalter hat die Form:
     
     {:[sign][width][.precision]type}
    
Dabei kann man jeden der Teile in eckigen Klammern weglassen. `width` beschreibt die 
Breite des Felds, `precision` die Anzahl der Nachkommastellen. Ist `sign` das Zeichen +, so werden 
Vorzeichen (von Zahlen) immer mit ausgegeben, ist es -, so werden nur negative Vorzeichen ausgegeben.
Achtung: Benötigt die Zahl für ihre Darstellung eine größere Breite als `width`, wird sie breiter
ausgegeben.

wobei `type` eines der folgenden Zeichen ist:

### Strings:

    s 	String format. This is the default type for strings and may be omitted.
    
Das s kann man weglassen, da Python das Format aus dem Typ erschließt.

### Integers:
    
    b 	Binary format. Outputs the number in base 2.
    c 	Character. Converts the integer to the corresponding 
        unicode character before printing.
    d 	Decimal Integer. Outputs the number in base 10.
    o 	Octal format. Outputs the number in base 8.
    x 	Hex format. Outputs the number in base 16, using 
        lower- case letters for the digits above 9.
    X 	Hex format. Outputs the number in base 16, using 
        upper- case letters for the digits above 9.
    n 	Number. This is the same as 'd', except that it uses 
        the current locale setting to insert the appropriate 
        number separator characters.
 
Steht kein Zeichen, so bedeutet das für Integers 'd'.
 
### Floats:

    'e' 	Exponent notation. Prints the number in scientific 
            notation using the letter ‘e’ to indicate 
            the exponent. The default precision is 6.
    'E' 	Exponent notation. Same as 'e' except it uses an upper 
            case ‘E’ as the separator character.
    'f' 	Fixed point. Displays the number as a fixed-point 
            number. The default precision is 6.
    'F' 	Fixed point. Same as 'f', but converts nan to NAN and 
            inf to INF.
    'g' 	
            General format. For a given precision p >= 1, this rounds the number to p significant digits and 
            then formats the result in either fixed-point format or in scientific notation, depending on 
            its magnitude. The precise rules are as follows: suppose that the result formatted with presentation
            type 'e' and precision p-1 would have exponent exp. Then if -4 <= exp < p, the number is formatted
            with presentation type 'f' and precision p-1-exp. Otherwise, the number is formatted with 
            presentation type 'e' and precision p-1. In both cases insignificant trailing zeros are removed 
            from the significand, and the decimal point is also removed if there are no remaining digits 
            following it.

            Positive and negative infinity, positive and negative zero, and nans, are formatted as inf, -inf, 0, 
            -0 and nan respectively, regardless of the precision.

            A precision of 0 is treated as equivalent to a precision of 1. The default precision is 6.
    'G' 	General format. Same as 'g' except switches to 'E' if the number gets too large. The 
            representations of infinity and NaN are uppercased, too.
    'n' 	Number. This is the same as 'g', except that it uses the current locale setting to 
            insert the appropriate number separator characters.
    '%' 	Percentage. Multiplies the number by 100 and displays in fixed ('f') format, followed 
            by a percent sign.


Steht kein Zeichen, so ist das ähnlich wie g, allerdings wird dafür gesorgt, dass in der Dezimaldarstellung mindestens eine Vorkommastelle steht. 


```python
import math
print('Der Wert beträgt {:.10f}'.format(math.pi))
```

    Der Wert beträgt 3.1415926536
    


```python
print('Der Wert beträgt {:n}'.format(math.pi))
```

    Der Wert beträgt 3.14159
    

### Was hat es mit `locale` auf sich?


```python
import locale
locale.getdefaultlocale()
```




    ('de_DE', 'cp1252')




```python
print('Der Wert beträgt {:n} .'.format(math.pi))
```

    Der Wert beträgt 3.14159 .
    


```python
locale.setlocale(locale.LC_ALL, "de_DE.utf8")
```




    'de_DE.utf8'




```python
print('Der Wert beträgt {:n} .'.format(math.pi))
```

    Der Wert beträgt 3,14159 .
    


```python
print('Der Wert beträgt {:n} .'.format(12346756765))
```

    Der Wert beträgt 12.346.756.765 .
    


```python
locale.setlocale(locale.LC_ALL, "C")
```




    'C'




```python
print('Der Wert beträgt {:n} .'.format(math.pi))
```

    Der Wert beträgt 3.14159 .
    


```python
print('Der Wert beträgt {:n} .'.format(12346756765))
```

    Der Wert beträgt 12346756765 .
    

### Übergabe von Werten mit Feldnamen

In den oben geschilderten Formatspezifikationen lassen sich auch 'keywords' vor den Namen schreiben. Dann können  die zu formatierenden Werte an .format(...) mit keywords übergeben werden, was oft lesbarer ist. Also ein Beispiel von vorhin mit dieser Form:




```python
print("Die Länge der {name:10s} ist {length:.2f} {unit:10s}.".format(
    name='Strecke', length=213.12312, unit='Meter'))
```

    Die Länge der Strecke    ist 213.12 Meter     .
    

### Weitere Details zur Formatierung

Formatstrings des neuen Typs enthalten Platzhalter, die in geschweifte Klammern {}
eingeschlossen sind (statt %).  Ansonsten ist das Format durch folgende **Grammatik**
charakterisiert:

    Platzhalter       ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
    field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
    arg_name          ::=  [identifier | integer]
    attribute_name    ::=  identifier
    element_index     ::=  integer | index_string
    index_string      ::=  <any source character except "]"> +
    conversion        ::=  "r" | "s" | "a"
    format_spec       ::=  siehe unten

und die Formatspezifizierung `format_spec` so:

    format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
    fill        ::=  <any character>
    align       ::=  "<" | ">" | "=" | "^"
    sign        ::=  "+" | "-" | " "
    width       ::=  integer
    precision   ::=  integer
    type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"


### Was ist das und wie ist es zu lesen?

Es handelt sich um eine *Backus-Naur-Form für die (kontextfreie) Grammatik* solcher Ausdrücke. Was kompliziert klingt und aussieht, ist im Kern ganz einfach.  Man beginnt mit dem Ausdruck, den es zu erklären gilt `Platzhalter` auf der linken Seite oben. Durch ::= wird definiert, was dafür eingesetzt werden kann, dabei stehen wieder [ ] für Teile, die man weglassen kann und  | steht für "oder".

Auf der rechten Seite stehen entweder bestimmte Zeichen oder Typen, dann wissen wir, was gemeint ist, oder aber es stehen wieder zunächst unverständliche Ausdrücke. In diesem Fall müssen wir nun wieder auf der linken Seite nach diesen Ausdrücken suchen. So finden wir wieder eine Definition ::=, durch die wir den Ausdruck ersetzen können. Auf diese Weise werden alle möglichen Ausdrücke beschrieben.  

Keine Angst, unten stehen viele Beispiele, mit denen man es genausogut begreifen kann, ohne sich auf die Backus-Naur-Form einzulassen. So steht diese aber in der offiziellen Dokumentation: Es ist also nützlich, sie lesen zu können oder zumindest nicht abgeschreckt zu sein.

Diese Form erklärt aber nur die **Syntax**, nicht die **Semantik**, d.h.  Bedeutung der Ausdrücke.  Dazu braucht es
weitere Erklärungen. Die vollständigen Erklärungen finden sich unter https://docs.python.org/3/library/string.html,
ich erkläre nur einen Teil davon per Beispiel.


Hier soll nur ein Beispiel für die weiteren Möglichkeiten stehen, die das Beispiel von vorhin nochmal um Füllzeichen und rechts- bzw. linksbündige Ausrichtung erweitert:


```python
for name,length,unit in zip(['Strecke','Katze','Straße'],[213.123,33.335,123213.32],['Meter','Daumenbreit','Centimeter']):
    print("Die Länge der {name:-<10s} ist {length:10.2f} {unit:-<12s}.".format(
        name=name, length=length, unit=unit))
```

    Die Länge der Strecke--- ist     213.12 Meter-------.
    Die Länge der Katze----- ist      33.34 Daumenbreit-.
    Die Länge der Straße---- ist  123213.32 Centimeter--.
    

## Noch eine ander Art der Formatierung: f-Strings (Python >= 3.6)

Diese Art der Formatierung wurde erst in Python 3.6 eingeführt, s.:

https://www.python.org/dev/peps/pep-0498/

Dabei wird eine neue Art von Strings eingeführt, bei denen ein `f` vor den Anführungszeichen steht. Alle Ausdrücke in geschweiften Klammern werden dann evaluiert und das Ergebnis an dieser Stelle in den f-String eingesetzt; das Ergebnis ist ein gewöhnlicher String. Die Ausdrücke können noch durch eine Formatspezifikation erweitert werden, wie wir sie schon kennen, etwa `:.3f`. Sehen wir uns einige Beispiele an:


```python
tier = "Die Katze"
objekt = "der Matte"
satz = f"{tier} sitzt auf {objekt}"

print(satz)
```

    Die Katze sitzt auf der Matte
    


```python
f"{tier} ist {laenge:.2f} Meter und damit {laenge/0.9144:.2f} yards lang."
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-17-5f98b1acdabc> in <module>
    ----> 1 f"{tier} ist {laenge:.2f} Meter und damit {laenge/0.9144:.2f} yards lang."
    

    NameError: name 'laenge' is not defined


Wenn nicht zufällig vorher schon eine Variable 'laenge' definiert wurde, gibt es einen Fehler.

Achtung: Nur, wenn die  Ausdrücke in geschweiften Klammern korrekt evaluiert werden können, wird der f-String ohne Fehler ausgewertet.


```python
laenge = 0.7
f"{tier} ist {laenge:.2f} Meter und damit {laenge/0.9144:.2f} yards lang."
```




    'Die Katze ist 0.70 Meter und damit 0.77 yards lang.'




```python
import numpy as np
radius = 1.23
f"Ein Kreis des Radius {radius:.2f} hat einen Flächeninhalt von {np.pi*radius**2:.2f}."
```




    'Ein Kreis des Radius 1.23 hat einen Flächeninhalt von 4.75.'




```python

```


```python

```
