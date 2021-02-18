#! /usr/bin/python3

from math import sqrt


print("Tama ohjelma laskee suorakulmaisen kolmion hypotenuusan tai kateetin.\nValitse lasketaanko\n 1. hypotenuusa vai\n 2. kateetti")
def pythagora():
    while True:
        laskutoim = input("Anna valintasi ")
        if laskutoim == "1":
            while True:
                try:
                    kateetti1 = float(input("Anna ensimmainen kateetti: "))
                    break
                except ValueError:
                    print("Et antanut lukua!")
            while True:
                try:
                    kateetti2 = float(input("Anna toinen kateetti: "))
                    break
                except ValueError:
                    print("Et antanut lukua!")
            hypotenuusa = sqrt(kateetti1**2+kateetti2**2)
            print("Hypotenuusan pituus on: ", hypotenuusa)
            break
        elif laskutoim == "2":
            while True:
                try:
                    kateetti1 = float(input("Anna ensimmainen kateetti: "))
                    break
                except ValueError:
                    print("Et antanut lukua!")
            while True:
                try:
                    hypotenuusa = float(input("Anna hypotenuusa: "))
                    break
                except ValueError:
                    print("Et antanut lukua!")
            kateetti2 = sqrt(hypotenuusa**2-kateetti1**2)
            print("Toisen kateetin pituus on: ", kateetti2)
            break
        print("Väärä valinta, kirjoita 1 tai 2")        

    print("Haluatko viela tietaa kolmion pinta-alan? K/E")
    laskutoim = input("Vastauksesi: ")
    if laskutoim == "K" or laskutoim =="k":
        print("Pinta-ala on: ", ((kateetti1*kateetti2)/2))
    
    uudestaan = input("Lasketaanko viela? K/E")
    if uudestaan == "K" or uudestaan == "k":
        pythagora()
    else:
        print("Kiitos hei!")
    return
pythagora()