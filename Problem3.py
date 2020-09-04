# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor 
# of the number 600851475143 ?

from math import sqrt

x = int(input("Stevilo, katerega največji prafaktor zelite:"))

def delitelji_n (n):
    delitelji_seznam = list ()
    m = 1
    while m <= int(sqrt(n)):
        if n % m == 0:
            delitelji_seznam.append ( m )
        m += 1
    return delitelji_seznam

delitelji = delitelji_n(x)
print ("Delitelji stevila" , x , "so" , delitelji , ".")

def je_prastevilo(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    else:
        for i in range ( 4 , int (sqrt (n) ) + 1 ):
            if n % i == 0:
                return False
        else:
            return True

prastevilski_delitelji = list ()
for stevilo in delitelji:
    if je_prastevilo(stevilo) == True:
        prastevilski_delitelji.append(stevilo)
    

print("Prastevilski delitelji stevila" , x , "so" , prastevilski_delitelji , ".")
print("Najvecji prastevilski delitelj stevila" , x, "je" ,prastevilski_delitelji[ - 1], ".")



