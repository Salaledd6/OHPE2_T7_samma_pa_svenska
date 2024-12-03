import random

sanasto = {"apina":"apa", "banaani":"banan", "juusto":"ost",
           "kakku":"kaka", "kala":"fisk", "kirja":"bok",
           "lintu":"fågel", "porkkana":"morot", "punajuuri":"röbeta",
           "puu":"trä"}

avaimet = list(sanasto.keys())
oikeat = 0
vaarat = 0

for i in range(len(avaimet)):
    kysyttava_sana = random.choice(avaimet)
    vastattu_sana = input(f"Kirjoita '{kysyttava_sana}' ruotsiksi > ")


    if vastattu_sana == sanasto[kysyttava_sana]:
        oikeat += 1
        avaimet.remove(kysyttava_sana)
        print("Oikein meni!")
    else:
        vaarat += 1
        print("Yritä uudelleen")

print(f"Oikeat vastaukset; {oikeat} Väärät vastaukset: {vaarat}")