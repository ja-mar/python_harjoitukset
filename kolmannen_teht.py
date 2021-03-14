#! /usr/bin/python3

from math import sqrt


print("\nTama ohjelma laskee suorakulmaisen kolmion hypotenuusan tai kateetin.")
def pythagora(): #!Luodaan funktio
    print("\nValitse kumpi lasketaan\n 1. hypotenuusa\n 2. kateetti")
    while True:
        laskutoim = input("Anna valintasi ")
        if laskutoim == "1":
            #! 1 laskutoimitus alkaa jossa lasketaan hypotenuusan pituus, käyttäjän antamien arvojen perustella.
            while True:
                     #! try kokeilee onko syötetty numeroita
                     #! jos ei, niin antaa virhe ilmoituksen ja anntaa mahdollisuus syöttää arvon udelleen
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
            #! 1 laskutoimitus päättyy

            #! 2 laskutoimitus alkaa jossa lasketaan kateetin pituus, käyttäjän antamien arvojen perustella.
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
            #! 2 laskutoimitus päättyy 
        print("Väärä valinta, kirjoita 1 tai 2")        

    #! tiedustellaan haluaako käyttäjä tietää kolmion-pinta-alan 
    print("\nHaluatko viela tietaa kolmion pinta-alan? K/E")
    laskutoim = input("Vastauksesi: ")
    if laskutoim == "K" or laskutoim =="k":
        print("\nPinta-ala on: ", ((kateetti1*kateetti2)/2))
    
    #! tiedustellaan haluaako käyttäjä laskea vielä lisaa.
    uudestaan = input("\nLasketaanko viela? K tai k jatkaa, mika tahansa muu lopettaa\n")
    if uudestaan == "K" or uudestaan == "k":
        pythagora()
    else:
        print("\nKiitos hei!")
    return
    #! funktio päättyy

pythagora() #!Kutsutaan funktio eli ohjelma alkaa