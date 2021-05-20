import math
# name: [duchmesser, Preis]
pizzen = {"Funghi": [20, 8.5],
          "Marinara": [30, 16],
          "Margherita": [17, 19],
          "Spinaci": [8, 10.5],
          "Quattro Formaggi": [15, 15.0]}

mi = 1000000000
kandidat = ''

for key in pizzen:
    preis_pro_flaeche = pizzen[key][1]/(math.pi*(pizzen[key][0]/2)**2)
    if mi > preis_pro_flaeche:
        mi = preis_pro_flaeche
        kandidat = key

#    mi = min(mi, preis_pro)

print(kandidat, mi)
