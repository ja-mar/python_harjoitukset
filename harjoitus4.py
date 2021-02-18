#! /usr/bin/python3

class Ensimmainen_luokka:
    x=2

luokka_objekti = Ensimmainen_luokka()
print(luokka_objekti.x)

luokka_objekti.x = 4
print(luokka_objekti.x)

class Toinen_luokka:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def tulosta_arvot(self):
        print(self.x)
        print(self.y)

luokka_objekti = Toinen_luokka(4,5)
luokka_objekti.tulosta_arvot()

while True:
    syote = input("kirjoita: ei ")
    if syote == "ei":
        break

syote2 = ""
while syote2 != "on":
    syote2 = input("kirjoita: on")