# The sum of the squares of the first ten natural numbers is,
# 
# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,
# 
# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares 
# of the first ten natural numbers and the square of the 
# sum is 3025−385=2640.
# 
# Find the difference between the sum of the squares of 
# the first one hundred natural numbers and the square 
# of the sum.


def vsota_kvadratov ( n ) :
    i = 1
    kvadrati = list ()
    while i <= ( n ):
        kvadrati.append ( i ** 2 )
        i += 1
    vsota = sum ( m for m in kvadrati )
    return vsota

def kvadrat_vsote ( n ) :
    vsota_stevil = n * ( n + 1 ) / 2
    kvadrat = vsota_stevil ** 2
    return kvadrat


def razlika (n):
    y = kvadrat_vsote ( n ) - vsota_kvadratov ( n )
    return y
