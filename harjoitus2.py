#! /usr/bin/python3

eka_lista = [12,21,54,12,75]

print(eka_lista)

toka_lista = ["eka", "toka", "kolmas"]
print(toka_lista)
print(toka_lista[0])

toka_lista[0] = "vika"
print(toka_lista)

toka_lista.append("toimiiko")
print(toka_lista)
##
eka_lista.extend(toka_lista)
print(eka_lista)

kolmas_lista = eka_lista +  toka_lista
print(kolmas_lista)

print(toka_lista)
eka_muuttuja = toka_lista.pop()
print(toka_lista)
print(eka_muuttuja)

for mita_tahansa in toka_lista:
    print(mita_tahansa)

print(len(toka_lista))

for i in range(len(toka_lista)):
    print(toka_lista[i])

for i in range(30):
    print("luku" + str(i))
    if i == 15:
        break
