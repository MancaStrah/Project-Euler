from string import ascii_uppercase

slovar_crk = {}
for crka in ascii_uppercase:
    slovar_crk[crka] = ascii_uppercase.index(crka) + 1

with open('names.txt' , 'r' ,encoding='utf8') as d:
    vsebina = d.readlines()
    imena = []
    for ime in vsebina:
        imena = ime.replace('"', '').split(',')
    imena.sort()

    slovar_imen = {}
    for i in range(len(imena)):
        slovar_imen[imena[i]] = i + 1

def ovrednoti_ime(ime):
    vsota = 0
    for crka in ime:
        vsota += slovar_crk[crka]
    return vsota


score = 0
for ime in imena:
    score += (ovrednoti_ime(ime) * slovar_imen[ime])

print(score)