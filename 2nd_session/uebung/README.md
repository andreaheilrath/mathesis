---
title: Übung
parent: 2. Session
nav_order: 4
permalink: /2nd_session/uebung/
---

# 2. Übung

Listen, Wörterbücher, Mengen,  for-Schleifen

Hausaufgabe: Löse mindestens 6 der folgenden Aufgaben. Ihr dürft die Aufgaben in Gruppen bearbeiten. 

Abgabe im ISIS-Kurs, spätestes Abgabedatum wird dort angegeben, Gruppenpartner bitte bei der Abgabe vermerken.


### Hinweis zum Plotten

In den Aufgaben sollen die Ergebnisse häufig mit `matplotlib.pyplot` visualisiert werden.

An dieser Stelle ein kurzer Hinweis zur Verwendung des Moduls:


```python
# Zunächst erstelle ich einige Listen, die gleich geplottet werden sollen.
x_werte = [0, 1, 2, 3, 4, 5]
y_werte1 = [0, 0, 2, 2, 4, 4]
y_werte2 = [3, 3, 1, 1, 0, 0]

import matplotlib.pyplot as plt

plt.scatter(x_werte,y_werte1) #erzeugt punkte
plt.plot(x_werte,y_werte1) #erzeugt verbindungslinien

plt.scatter(x_werte,y_werte2, marker = "x") #erzeugt kreuze
plt.plot(x_werte,y_werte2) #erzeugt verbindungslinien

plt.show()
```

## Einfachere Aufgaben

### 1. Sägezahnmuster
Schreiben Sie ein Programm, das unter der Verwendung von Schleifen ein 
Sägezahnmuster wie folgt ausgibt:
```
*
**
***
****
*
**
***
****
```
Gestalte das Programm so, dass die Länge des Sägezahns durch eine Eingabe festgelegt wird.



### 2. Schatzsuche
Gegeben ist eine Folge von Anweisungen mit Schrittzahlen und Drehungen um 90 Grad nach links oder rechts, z.B. *2 3 L 1 L L 2*. 
Am Anfang steht man auf der Koordinate $(0, 0)$ mit Blickrichtung und Schrittweite derart, dass ein Schritt einen auf die Koordinate $(0, 1)$ bringt. 

Schreibe ein Programm, das für eingegebenen Anweisungen die Endkoordinate ausgibt, also etwa für das Beispiel $(1, 5)$.


### 3. Pascalsches Dreieck

Das [Pascal'sche Dreieck](de.wikipedia.org/wiki/Pascalsches_Dreieck) besteht aus den Binominialkoeffizienten $n$ über $k$.

So kann man aus der $(n+1)$. Reihe die Koeffizienten für $(a+b)^n$ ablesen, z.B. ist  

$(a+b)^4 = 1\cdot a^4+4\cdot a^3b +6\cdot a^2b^2+4\cdot ab^3+1\cdot b^4$.

Berechnen kann man einen Eintrag einfach als Summe der beiden Elemente links und rechts aus der Reihe über dem Wert (siehe Wikipedia). An den Rändern nimmt man für die fehlende Werte einfach jeweils den Wert 0. 

Schreibe ein Programm, dass die ersten $n$ Zeilen des Pascalsche Dreiecks ausgibt, wobei $n$ vom Benutzer eingelesen werden soll. Es reicht, wenn das Dreieck linksbündig ausgegeben wird, also so:

```
1
1 1 
1 2 1
1 3 3 1
1 4 6 4 1
```

### 4. Balkendiagramm 1
Schreibe ein Programm, das eine (durch Leerzeichen getrennte) Liste von Zahlen (zwischen 0 und 50)  einliest und daraus ein einfaches Balkendiagramm macht.
Dabei soll eine Zahl, die zu $n$ gerundet ist, durch $n$ Sternchen dargestellt werden. 

Die Eingabe 2 3 5 2 wird zu:
```
**
***
*****
**
```

### 5. Balkendiagramm 2

Schreibe ein Programm, dass in derselben Weise wie eben eine Liste von Zahlen einliest, dann aber eine Balkengraphik mit Hilfe des Moduls `matplotlib` anzeigt.

Dann steht Ihnen die Funktion `plt.bar` zur Verfügung, die in der Dokumentation von `matplotlib` beschrieben wird: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.bar

Nach dem Aufruf von `plt.bar(...)` ist die Grafik erzeugt, aber noch unsichtbar. Sichtbar wird sie erst  durch `plt.show()`.

### 6. Sinus-Funktion plotten

Schreibe ein Programm, das die Sinus-Funktion im Bereich von [0, 2pi] zeichnet. Wähle ausreichend Datenpunkte, damit die Funktion glatt dargestellt wird. Benutze die Module `math` und `matplotlib`.

## Mittelschwere Aufgaben

### 7. Vollkommene Zahlen (zählt doppelt)

Als **Vollkommene Zahlen** bezeichnet man die Zahlen, die gleich der Summe Ihrer Teiler (ganzzahlig, positiv, ohne die Zahl selbst, aber inklusive der Eins) sind.  

Die ersten beiden vollkommenen Zahlen sind $6 = 1 + 2 + 3$ und $28 = 1 + 2 + 4 + 7 + 14$.  

Schreibe ein Programm, das die ersten vier (oder mit viel Zeit: fünf) vollkommenen Zahlen ausgibt.

**Hinweis:** Für ganze Zahlen $i$ und $n$ teilt $n$ das $i$, wenn mit ganzzahliger Division gilt $(i/n)*n == i$. Eleganter kann
man dies auch mit Modulo prüen, ob kein Divisionsrest bleibt: $i \, \% \, n == 0$.

**Historische Anmerkung:** Von der ersten vollkommenen Zahl rührt auch die Bezeichnung: Die christlichen Zahlenmystiker sahen die Sechs als vollkommen an, da dies die Zahl der Tage gewesen ist, die Gott zum Erschaffen der Welt benötigt hat.

### 8. Anagramme
Ein Anagramm ist ein Wort oder Satz, der durch Umstellen aller Buchstaben eines anderen Satzes gebildet werden kann. Leerzeichen sowie Unterschiede zwischen Groß- und Kleinschreibung werden ignoriert. 

Beispiele sind die Paare **Buecher sind Freunde** und **Befreie den Urschund** oder **Chaos** und **Ach so**. 

Schreibe ein Programm, das prüft ob zwei eingegebene Zeichenkette ein Anagramm von einander bilden. 


### 9. Diskretes Räuber-Beute-Modell

Dieses in der mathematischen Biologie betrachtete Modell beschreibt die Entwicklung der Populationsdichte $x$ einer Beutespezies ('Kaninchen') und der Populationsdichte $y$ einer Räuberspezies ('Füchse'). Die Populationen werden nur in gewissen Zeitabständen ermittelt, und das Modell macht auch nur für diese Zeiten Voraussagen. Man sagt, das Modell sei diskret in der Zeit.

$x_{n+1} =  ax_n(1-x_n) - bx_ny_n \qquad y_{n+1} = cx_ny_n \;. $

Schreibe ein Programm, das die Populationen mit den Parametern $a=3.5$, $b=2$, $c=4.05$ und den Anfangswerten
$x_0=0.5$ und $y_0=0.4$  hundert Schritte  lang berechnet.

Speichere für jeden Schritt den Wert `n`, `x` und `y`. Visualisiere den Verlauf von $x$ über $n$, sowie $y$ über $n$ in einem Plot.

Fertigen Sie diesen Plot auch für andere Parameterwerte a,b,c an. Was fällt auf?


### 10. Quersumme
Schreibe ein Programm, das als Eingabe eine (ganze) Dezimalzahl erwartet und die Quersumme ausgibt, diesmal allerdings ohne Verwendung von Schleifen, sondern unter Verwendung der Funktionen `sum` und `map`.


### 11. Random Walk Fortsetzung
Simuliere (ohne Graphik) eine große Zahl $N$ von Irrfahrten, die im Ursprung starten und $M$ Schritte lang verfolgt werden. Bestimmen Sie den mittleren Abstand vom Ursprung nach $k$ Schritten und das mittlere Quadrat des Abstands vom Ursprung nach $k$ Schritten für $k\in\{1,\ldots,M\}$. 

Stelle diese Statistiken mit Hilfe von `matplotli` dar.

Bestimme die Häufigkeit der ersten Rückkehr zum Ursprung nach $2k$ Schritten für $1\leq k\leq M/2$ und stelle diese ebenfalls dar. 


### 12. Zufällige Karte geben

Mit `import random` liefert `random.random()` (Pseudo-)Zufallszahlen aus dem Bereich von 0.0 bis 0.999...
als `float`.

Verwende dies um eine `int`-Zufallszahl von 0 bis 3 (für eine zufällige Spielkartenfarbe) und eine
zweite von 0 bis 12 (Spielkartenwert) zu erzeugen. Gebe dann textuell Farbe (Karo, Herz, Pik oder Kreuz) und Wert (As, 2 bis 10, Bube, Dame, König) aus. 

Hinweis: Verwende für die Umwandlung in den Ausgabetext die Zahl als Index einer Liste von Zeichenketten.

### 13. Folge und Reihe
Gegeben ist die mathematische Folge $a_i = (-1)^i \frac{1}{i+1}$ für $i \ge 0$.

1. Schreibe ein Programm, das die Folgeglieder von $a_0$ bis $a_n$ ausgibt, wobei als $n$ vom Nutzer eingelesen werden soll.

2. Schreibe ein Programm, dass die Reihenglieder von $s_n = \sum_{j=0}^{n} a_j$ ausgibt. 

### 14. Häufigkeit von Aminosäuren
Lese wie in der 1. Übung die DNA-Sequenz des 'ersten' Proteins von E. Coli in einen String.

Je drei Basen ('ein Triplett') definieren eine Aminosäure. Erstelle eine Häufigkeitstabelle der Tripletts.

(Das ist noch keine Häufigkeitstabelle für die Aminosäuren, da mehrere Tripletts dieselbe Aminosäure codieren können.)

### 15. Wortliste

Erstelle eine eine Liste der Wörter aus einem Buch deiner Wahl (in reinem Text-Format). 
Hilfreich ist hierbei die String-Methode `split`.

Schau dir die erzeugte Liste stichprobenweise an - z.B. das 100. - 120. Wort.

Zur Erinnerung der Codeschnipsel, der etwa die Buddenbrooks in einen langen String lädt:


```python
with open("buddenbrooks.txt","r") as file:
    text=file.read()

print(text)
```

### 16. Worthäufigkeiten
Erstelle ein Wörterbuch, das die Worthäufigkeiten in dem von dir gewählten Buch ermittelt.

Zusatz: Sortiere die Wörter absteigend nach ihrer Häufigkeit. Schlagen im Internet *Zipf's law* nach und überprüfe dieses an dem gewählten Buch. Zur graphischen Darstellung kannst du `matplotlib` benutzen.

### 17. Rätsel lösen
In dem folgenden Rätsel sind Ziffern durch Buchstaben ersetzt.
Schreiben Sie ein Programm, das alle Lösungen ausgibt.

```
 OMA
+OPA
----
PAAR
```
Wenn Sie noch Lust haben, können Sie zusätzlich die Lösung von
```
 SEND
+MORE
-----
MONEY
```
suchen. 

Wenn man davon ausgeht, das die drei Zahlen nicht mit Null beginnen,
gibt es für dieses zweite Rätsel eine eindeutige Lösung.

## (Sehr) schwere Aufgaben

### 18. Gini-Index
Schreiben Sie ein Programm, das aus einer Liste von Zahlen $x_1,\ldots, x_n$ den Gini-Index dieser Zahlen berechnet.
Der Gini-Index ist ein  Maß für die Abweichung einer Verteilung (bspsw. einer Einkommensverteilung) von der Gleichverteilung, das von internationalen Organisationen als Ungleichheitsindikator verwendet wird.
Der Gini-Index lässt sich so berechnen:

$ G = \frac{\sum_{i=1}^n\sum_{j=1}^n |x_j-x_i|}{2n\sum_{i=1}^n x_i} \; . $

Testen Sie, ob $G$ für eine Liste gleicher Zahlen tatsächlich 0 ist. Bestimmen Sie weiterhin den Gini-Index von $\{1,\ldots, n\}$ für $n=100,1000,10000$.

Zusatz: Bestimmen Sie die Gini-Indizes des Einkommens im Bundesgebiet und per Bundesland mit Hilfe der Mikrozensusdaten. 
(Es lohnt sich, die Wikipedia-Seiten zum Gini-Index zu lesen. Wer sich allgemeiner für das Thema, Ungleichheit zu messen, interessiert, findet auf ISIS einen Übersichtsartikel von Atkinson.)


### 19. Sieb
Erzeugen Sie eine Liste aller Primzahlen, die kleiner als eine Million sind, mit dem Sieb des Eratosthenes. 

(Ein Tip: Verwenden Sie zu dem im Sieb-Algorithmus vorkommenden Durchstreichen ein Numpy-Array und die Ihnen bekannten 'Slicing'-Operationen.) 

Kleiner Wettbewerb:  Wer schreibt das Programm, das (auf einem Prozessor) am schnellsten läuft?

### 20. Datenanalyse 1 (zählt doppelt)

Lese die Tabelle der Mikrozensusdaten 2003 ein. 

Bestimme Median und Mittelwert des Einkommens in Abhängigkeit von Bundesland und Geschlecht.

Zeige außerdem Histogramme der Einkommen in Abhängigkeit von Bundesland oder Geschlecht an.

Hinweis: Bevor mit der Auswertung der Datem begonnen werden kann, müssen die erst mal ins richtige Format gebracht werden ...


```python
raw_data = []
datei=open("algebuei.csv","r")
for zeile in datei:
    raw_data.append(zeile)
datei.close()

zeilen = 5
for i in range(zeilen):
    print(raw_data[i])
```


```python
processed_data = []
for index in range(len(raw_data)):
    processed_data.append(raw_data[index][:-1].split(";"))
    
for i in range(zeilen):
    print(processed_data[i])  #hier stehen immernoch strings...
```

### 21. Datenanalyse 2  (zählt doppelt)
`av_temps`  bezeichnet ein Numpy-Array, das die täglichen Durchschnittstemperaturen vom 1.1.1948 bis zum 31.12.2018 enthält. Die direkte Darstellung der Temperaturen zeigt ein Auf-und-Ab, erlaubt aber nicht ohne weiteres, Tendenzen des Klimawandels zu sehen, die unter den Schwankungen unsichtbar werden.

Berechne aus dem Array `av_temps` ein neues Array, das für jeden Tag den Mittelwert der mittleren Temperaturen von N Tagen vorher bis N Tagen nacher enthält. Wichtig ist hierbei, sich zu überlegen, wie der Rand behandelt wird, d.h. die ersten und die letzten N Tage des Datensatzes. 

Schau dir die zugehörigen Plots mit Hilfe der im Notebook definierten Funktion `show_plots` für verschiedene Werte von N an und interpretiere die Resultate.

Kommst du noch auf andere Ideen?


```python
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Die Funktion how_plot müssen Sie nicht im einzelnen verstehen; sie
# können sie zunächst einfach verwenden

def show_plot(dates, temps_list, labels_list):
    '''Shows the graphs of all the temperature array in temps_list,
    labels them with the labels in labels_list. The common x-axis
    is given by dates.'''
    assert len(temps_list) == len(labels_list)  # es ist erforderlich, dass es
    # so viele Labels wie Temperaturarrays gibt.
    plt.figure()
    for temps, label in zip(temps_list, labels_list):
        plt.plot(dates, temps, label=label, alpha=0.7)

    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gcf().autofmt_xdate()
    plt.legend(loc=4)
    plt.grid()
    plt.show()


with open("produkt_klima_tag_19480101_20181231_00433.txt", "r") as f:
    dat = np.genfromtxt(f, names=True, delimiter=';')

dates = [datetime.datetime(year=int(str(d)[:4]), month=int(str(d)[4:6]), day=int(
    str(d)[6:8])) for d in np.array(dat['MESS_DATUM'], dtype=np.int)]

av_temps = dat['TMK']
max_temps = dat['TXK']
min_temps = dat['TNK']

show_plot(dates, [av_temps, max_temps, min_temps], ['av', 'max', 'min'])
```

### 22. Schall (zählt doppelt)

Schreibe ein Programm, das als Eingabe einen String mit Tonsymbolen verlangt 'a h c a' und diese hörbar macht. (Über eine Oktave zunächst, komplizierter mit mehreren Oktaven, etc.).

Dazu kannst du mit `from schallwerkzeuge import * ` eine Funktion importieren, die das Abspielen eines Klangs 
erlaubt. Um die Schallwerkzeuge benutzen zu können muss auch noch `numpy` importiert werden. Das Modul benötigt 
das Modul `pyaudio` - um das zu installieren muss in der Konsole `pip install pyaudio` eingegeben werden - das kann aber auch gerne mal nicht klappen.

Ein kleiner Codeschnipsel, der einen Ton erzeugt:


```python
import numpy as np
from schallwerkzeuge import *

werte=[np.sin(x/10.) for x in range(40000)]
playsnd(np.array(werte),RATE)
```

### 23. 1D-Zellularautomaten mit ASCII-Graphik (zählt dreifach)

Stellen dir eine Reihe von Zellen vor, die in einer Linie nebeneinander liegen. Jede Zelle hat einen Zustand, tot oder lebendig. Nun sollen sich die Zustände der Zellen in der Zeit schrittweise verändern, und zwar ist der Zustand abhängig von dem alten Zustand und den Zustand der beiden benachbarten Zellen.

Den Zustand von je drei Zellen kann man als eine Zahl von 0 bis 7 auffassen: die Zustände als  0/1-Ziffern der Binärcodierung. Zum Beispiel Tot-Lebendig-Tot entspricht $010_2 = 2$. Eine Regel für den zellulären Automaten deﬁniert nun für jeden Zellenzustand unter Berücksichtigung ihrer Nachbarn einen darauf folgenden Zustand, d.h. es ergibt sich eine Tabelle mit acht Einträgen.

| Nachbarschaft | Nachfolger |
|---|---|
|LLL ($111_2 = 7$)|L (1)|
|LLT ($110_2 = 6$)|T (0)|
|LTL ($101_2 = 5$)|T (0)|
|LTT ($100_2 = 4$)|L (1)|
|TLL ($011_2 = 3$)|T (0)|
|TLT ($010_2 = 2$)|L (1)|
|TTL ($001_2 = 1$)|L (1)|
|TTT ($000_2 = 0$)|T (0)|

Damit kann man dann die Regel einfach als Folge von acht Bits auffassen, also als Zahl von 0 bis
255 (im Beispiel $10010110_2 = 150$).

Schreibe ein Programm, das eine Regel als Zahl 0 bis 255 einliest und die Entwicklung der Zellen in der Zeit berechnet. gib für jeden Zeitschritt (Generation) die Zellen in einer Zeile aus, jede Zelle je nach Zustand als anderen Buchstaben. Für die Zellen am Rand ist es am einfachsten, wenn Sie die äußerste linke und rechte Zelle als benachbart ansehen (ein sog.
*wraparound* oder auch *periodische Randbedingungen*).

Die Anfangspopulation kann zufällig belegt werden. Hierfür bietet sich `random.random()` aus dem Modul `random` an, welches (Pseudo-)Zufallszahlen von 0.0 bis (ausschließlich) 1.0 liefert.

Verschiedene Regeln ergeben verschiedene Verläufe https://en.wikipedia.org/wiki/Elementary_cellular_automaton

Erklärung in *The Nature of Code* https://natureofcode.com/book/chapter-7-cellular-automata/


```python

```
