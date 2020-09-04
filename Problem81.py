# In the 5 by 5 matrix below, the minimal path sum from the top left to the 
# bottom right, by only moving to the right and down, is indicated in bold 
# red and is equal to 2427.

 
# Find the minimal path sum from the top left 
# to the bottom right by only moving right and down in matrix.txt 
# (right click and "Save Link/Target As..."), a 31K text file 
# containing an 80 by 80 matrix.

slovar = {}

matrika = []
with open('p081_matrix.txt', 'r' ) as datoteka:
    for vrstica in datoteka:
        matrika.append([int(stevilka) for stevilka in vrstica.rstrip().split(',')])
     
for vrstica in range(len(matrika)):
    for stolpec in range(len(matrika[vrstica])):
        slovar[(vrstica, stolpec)] = 0
        
for vrstica in range(len(matrika)):
    for stolpec in range(len(matrika[vrstica])):
        if stolpec == 0 and vrstica == 0:
            slovar[(vrstica, stolpec)] = matrika[0][0]
        if stolpec == 0 and vrstica != 0:
            slovar[(vrstica, stolpec)] = slovar[(vrstica - 1, stolpec)] + int(matrika[vrstica][stolpec])
        if vrstica == 0 and stolpec != 0:       
            slovar[(vrstica, stolpec)] = slovar[(vrstica, stolpec - 1)] + int(matrika[vrstica][stolpec])
        if stolpec != 0 and vrstica != 0:
            slovar[(vrstica, stolpec)] = min(slovar[(vrstica, stolpec - 1)], slovar[(vrstica - 1, stolpec)]) + int(matrika[vrstica][stolpec])


print(slovar[79,79])
