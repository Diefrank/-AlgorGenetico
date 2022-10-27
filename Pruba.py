import json
from random import random
import math

import numpy as np

Converison = 0
SumDec = 0
Generacion = []
Decimal = []
Result = 0
fx = []
Posicion = []
for j in range(0, 8):
    Cromosoma = []
    for i in range(0, 4):
        NR = random()
        if (NR >= .5):
            Cromosoma.append(1)
        else:
            Cromosoma.append(0)

        cadena = json.dumps(Cromosoma)
        newstring = cadena.replace("[", "")
        new2 = newstring.replace("]", "")
        new3 = new2.replace(",", "")
        new4 = new3.replace(" ", "")
        NumDec = int(new4, 2)
    Result = NumDec

    Generacion.append(Cromosoma)
    Decimal.append(Result)
    # Generacion.sort()
#print(Generacion, '\n', Decimal)
for i in range(len(Decimal)):
    Fx = abs((Decimal[i] - 5) / (2 + math.sin(Decimal[i])))
    fx.append(Fx)
# fx.sort()
#print(fx)
print("===============================")

def sortKey(e):
  return e['fX']

for i in range(0, len(Generacion)):
    Posicion.append({'cromosoma' : Generacion[i], 'X' : Decimal[i], 'fX' : fx[i]})

Posicion.sort(key=sortKey, reverse=1)

for i in range(0, len(Posicion)):
    print(Posicion[i])

a = np.array([Generacion[0],Generacion[1], Generacion[2], Generacion[3], Generacion[4],Generacion[5], Generacion[6], Generacion[7]], dtype=np.int8)
print(a)
b1,b2,b3,b4,b5,b6,b7 = np.vsplit(a, 7)
#print(b1)
print(b1)
print(b2)
print(b3)
print(b4)
print(b5)
print(b6)
print(b7)


