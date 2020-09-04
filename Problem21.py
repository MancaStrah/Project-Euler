# Let d(n) be defined as the sum of proper divisors of n 
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b 
# are an amicable pair and each of a and b are called 
# amicable numbers.

# For example, the proper divisors of 220 are 
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore
# d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
from math import sqrt

def delitelji_n ( n ):
    delitelji_seznam = list ()
    m = 1
    while m <= int(n / 2):
        if n % m == 0:
            delitelji_seznam.append ( m )
        else:
            pass
        m += 1
    vsota = (sum (i for i in delitelji_seznam))
    return vsota

amicable_numbers = list ()
a = 1
while a <= 10000:
    b = delitelji_n (delitelji_n (a))
    if (a == b) and ( delitelji_n(a) != b ) :
        amicable_numbers.append (a)
    else:
        pass
    a += 1

print(amicable_numbers)

vsota = sum (i for i in amicable_numbers)

print (vsota)