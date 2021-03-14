#! /usr/bin/python3
import random


#helppo
#Kysy kauttajalta kuinka monta tahoista noppaa kayttaja haluaa heittaa.
#Tee funtio joka ottaa sisaansa tahojen lukumaaran ja palauttaa listan jossa on nopan silmaluvut.
#Anna satunnainen nopantulos printtaamalla se kayttajalle.

#normaali
#sama kuin normaali, mutta kysy kuinka monta noppaa kayttaja haluaa heittaa, ja printtaa
# noppien tulos erikseen ja summana


#vaikea
#Sama kuin normaali, mutta tuloksen jalkeen kysy kayttajalta halutaanko heittaa uudelleen.
#entterilla uusi heitto
#muuta noppa kysyy uudelleen tahot
#muuta noppien lukumaara kysyy noppaluvun uudelleen
#lopeta lopettaa ohjelman
def alusta_noppa():
    tahoja = int(input("Anna tahojen maara "))
    noppa = [i for i in range(1,tahoja+1)]
    return noppa

def set_nop_lkm():
    noppien_lkm = int(input("Anna noppien maara "))
    return noppien_lkm
    
    #print(noppa, "eka")
#nopan heitto
def heitto():
    monesko = 1
    total = 0
    while monesko <= noppien_lkm ():
        store = random.choice(noppa) 
        print(store)
        total=total+store
        monesko+=1
    print('Yhteensa ', total)

def uudest():
    uudestaan = input("Haluatko heittää")
    if uudestaan == "K" or uudestaan == "k":
        heitto()
        uudest()
    else:
        print("Kiitos hei!")

#noppa1 = random.choice(noppa)
#noppa2 = random.choice(noppa)
#print(noppa1, noppa2)
alusta_noppa()
set_nop_lkm()
print(set_nop_lkm)
heitto()
uudest()

#print(random.choice(noppa))
# print(noppa[random.randrange(10)])
#from random import randint
#for i in range(n_lkm):
#    print("noppa antaa: ", randint(1,6))
