#! /usr/bin/python3
import random

noppa_d100 =[i for i in range(1,11)]

print(noppa_d100, "eka")

print(random.choice(noppa_d100))

print(noppa_d100[random.randrange(10)])