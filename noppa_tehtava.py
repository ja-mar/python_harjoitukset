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

tahoja = input("Anna tahojen maara")
tahot = int(tahoja)
noppien_lkm = input("Anna noppien maara")
n_lkm = int(noppien_lkm)


noppa =[i for i in range(1,tahot+1)]

print(noppa, "eka")
#nopan heitto
def heitto():
    monesko = 1
    total = 0
    while monesko <= n_lkm:
        store = random.choice(noppa) 
        print(store)
        total=total+store
        monesko+=1
    print('Yhteensa ', total)

def uudest():
    uudestaan = input("Haluatko heittää")
    if uudestaan == "K" or uudestaan == "k":
        heitto()
        return
    else:
        print("Kiitos hei!")

#noppa1 = random.choice(noppa)
#noppa2 = random.choice(noppa)
#print(noppa1, noppa2)
heitto()
uudest()

#print(random.choice(noppa))
# print(noppa[random.randrange(10)])
#from random import randint
#for i in range(n_lkm):
#    print("noppa antaa: ", randint(1,6))
5