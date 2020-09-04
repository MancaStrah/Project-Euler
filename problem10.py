# # The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# # 
# # Find the sum of all the primes below two million
# 
# def delitelji_n ( n ):
#     delitelji_seznam = list ()
#     m = 1
#     while m <= n:
#         if n % m == 0:
#             delitelji_seznam.append ( m )
#         else:
#             pass
#         m += 1
#     stevilo_deliteljev = len ( delitelji_seznam )
#     return stevilo_deliteljev
# 
# prastevila = list ()
# m = 2
# while m < 2000000 :
#     if delitelji_n ( m ) == 2:
#         prastevila.append ( m )
#     else:
#         pass
#     m += 1
# 
# print ( prastevila )
# print ( sum ( i for i in prastevila ) ) 


# def delitelji_n ( n ):
#     delitelji_seznam = list ()
#     m = 1
#     while m <= n:
#         if n % m == 0:
#             delitelji_seznam.append ( m )
#         else:
#             pass           
#         m += 1
#     stevilo_deliteljev = len ( delitelji_seznam )
#     return stevilo_deliteljev
# 
# prastevila = list ()
# m = 2
# while m < 20 :
#     if delitelji_n ( m ) == 2:
#         prastevila.append ( m )
#     else:
#         pass
#     m += 1
# 
# print ( prastevila 
# )
# print ( sum ( i for i in prastevila ) ) 

x = int (input ("Vsota prvih n praštevil:"))
from math import sqrt

def je_prastevilo(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    else:
        for i in range ( 3 , int (sqrt (n) ) + 1 ):
            if n % i == 0:
                return False
        else:
            return True



# def prvih_prastevil (n):
#     m = 3
#     prastevila = list ()
#     prastevila.append (2)
#     prastevila.append (3)
#     while m < n:
#         if je_prastevilo(m) == True:
#             prastevila.append(m)
#         else:
#             pass
#         m += 2

#     return (prastevila)

# seznam = prvih_prastevil(x)

# print ( sum (i for i in seznam))

def prvih_n_prastevil(n):
    vsota = 0
    for i in range (1, n):
        if je_prastevilo(i):
            
            vsota += i
    return vsota



print (prvih_n_prastevil(x))