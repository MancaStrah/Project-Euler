# If we list all the natural numbers below 10 that are 
# multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.


def je_veckratnik_3_ali_5(n):
    return n % 3 == 0 or n % 5 == 0

stevec = 0
for stevilo in range(1, 1000):
    if je_veckratnik_3_ali_5(stevilo):
        stevec += stevilo

print(stevec)