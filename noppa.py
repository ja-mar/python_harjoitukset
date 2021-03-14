#! /usr/bin/python3
import random

def nro_pyynto(kysymys):
    player_in = None
    while True:
        player_in = input(kysymys)
        try: 
            player_in = int(player_in)
            if player_in == 0:
                raise ValueError
        except ValueError:
            print("Et syottany numeroa! ")
            continue
        return player_in

def main():
    while True:
        noppa_tahot = nro_pyynto("Anna nopan sivujen maara")
        noppa_lkm = nro_pyynto("Anna noppine lukumaara")
        noppa = [i for i in range(1,noppa_tahot+1)]
        total = 0
        for i in range(noppa_lkm):
            store = random.choice(noppa)
            print('Noppa', i+1,':',store)
            total=total+store
        print('Yht', total)
        heita_uudestaan = None
        while True:
            heita_uudestaan = input("Heitetaanko uudestaan?")
            if heita_uudestaan not in ["K", "E", "KYLLA", "EI", "e", "ei"]:
                continue
            break
        if heita_uudestaan in ['E', 'EI', 'e', 'ei']:
            break

        if __name__ == "__main__":
            main()

main()