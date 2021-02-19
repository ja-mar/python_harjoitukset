#! /usr/bin/python3

from math import sqrt


print("\nTama ohjelma laskee suorakulmaisen kolmion hypotenuusan tai kateetin.")
def pythagora(): #!Luodaan funktio
    print("\nValitse kumpi lasketaan\n 1. hypotenuusa\n 2. kateetti")
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
            print("\nHypotenuusan pituus on: ", hypotenuusa)
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
                    if kateetti1 > hypotenuusa:
                        print("Hypotenuusa ei voi olla pienempi kuin kateetti!")
                    else:
                        break
                except ValueError:
                    print("Et antanut lukua!")
                  
            kateetti2 = sqrt(hypotenuusa**2-kateetti1**2)
            print("\nToisen kateetin pituus on: ", kateetti2)
            break
        print("Väärä valinta, kirjoita 1 tai 2")        

    print("\nHaluatko viela tietaa kolmion pinta-alan? K/E")
    laskutoim = input("Vastauksesi: ")
    if laskutoim == "K" or laskutoim =="k":
        print("\nPinta-ala on: ", ((kateetti1*kateetti2)/2))
    
    uudestaan = input("\nLasketaanko viela? K tai k jatkaa, mika tahansa muu lopettaa\n")
    if uudestaan == "K" or uudestaan == "k":
        pythagora()
    else:
        print("\nKiitos hei!")
    return

pythagora() #!Kutsutaan funktio eli ohjelma alkaa