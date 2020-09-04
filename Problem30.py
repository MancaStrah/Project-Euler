# Surprisingly there are only three numbers 
# that can be written as the sum of fourth 
# powers of their digits:

# 1634 = 1 ** 4 + 6 ** 4 + 3 ** 4 + 4 ** 4
# 8208 = 8 ** 4 + 2 ** 4 + 0 ** 4 + 8 ** 4
# 9474 = 9 ** 4 + 4 ** 4 + 7 ** 4 + 4 ** 4
# As 1 = 1 ** 4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can 
# be written as te sum of fifth powers of their digits.

import itertools


potence  = [i ** 5 for i in range(0, 10)]
stevila = list(range(0, 10))
print(stevila)


vsote = [sum(x) for x in itertools.product(potence, repeat=7)]
prave = set()
for stevilo in vsote:
    stevke = str(stevilo)
    vsota_potecniranih_stevk = 0
    for stevka in stevke:
        vsota_potecniranih_stevk += int(stevka) ** 5
    if vsota_potecniranih_stevk == stevilo:
        prave.add(stevilo)

print(sum(x for x in list(prave)) - 1)

