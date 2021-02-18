#! /usr/bin/python3

#int()
#luku = int("4")
#str()
#input()
#print()

def eka_funktio():
    print("Eka funtktio tulostaa!")

eka_funktio()

def toka_funktio(teksti):
    print("toka funktio tulostaa taman + argumentin: " + teksti)

toka_funktio("ihan mita vaan")
toka_funktio("tai myos tallaista")
#toka_funktio(34)

#funktion palautuksella "return"
def kolmas_funktio():
    luku = 25
    return luku

funktion_palautus = kolmas_funktio()
print(funktion_palautus)