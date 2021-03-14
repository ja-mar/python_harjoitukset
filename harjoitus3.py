#! /usr/bin/python3

#int()
#luku = int("4")
#str()
#input()
#print()

def eka_funktio():
    print("eka funtktio tulostaa!")

eka_funktio()
eka_funktio()
eka_funktio()
# TypeError: eka_funktio() takes 0 positional arguments but 1 was given
# eka_funktio("mitahan tama tekee")

def toka_funktio(teksti):
    print("toka funktio tulostaa taman + argumentin: " + teksti)

toka_funktio("ihan mita vaan")
toka_funktio("tai myos tallaista")
# TypeError: can only concatenate str (not "int") to str
# toka_funktio(34) ei toimi koska kokonaisluku

#  funktion palautuksella "return"
def kolmas_funktio():
    luku = 25
    return luku

funktion_palautus = kolmas_funktio()
print(funktion_palautus)