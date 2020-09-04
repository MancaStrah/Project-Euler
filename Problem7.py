# By listing the first six prime numbers: 
# 2, 3, 5, 7, 11, and 13, we can see that the 6th 
# prime is 13.
# 
# What is the 10 001st prime number?

def delitelji_n ( n ):
    delitelji_seznam = list ()
    m = 1
    while m <= n:
        if n % m == 0:
            delitelji_seznam.append ( m )
        else:
            pass
        m += 1
    stevilo_deliteljev = len ( delitelji_seznam )
    return stevilo_deliteljev

prastevila = list ()

m = 2
while len ( prastevila ) < 10001 :
    if delitelji_n ( m ) == 2:
        prastevila.append ( m )
    else:
        pass
    m += 1

print ( prastevila )
print ( len ( prastevila ) )
print (  prastevila [ - 1 ] )


