# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

print(" The smallest positive number that is evenly divisble by all of the numbers from 1 to: ")
x = int ( input () )

# def fakulteta(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fakulteta (n - 1)
# 
# 
# def smallest_number(n):
#     for i in range (1, fakulteta(n) + 1 ):
#         stevila = list()
#         stevila = stevila.append(i)
#         return(stevila)
# 
# 
# print(smallest_number(x))
# 

# a * b == gcd (a , b) + lcm (a , b)
# lcm (a , b) == ( a * b ) / gcd ( a, b )
 

def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd (n, m % n)
    
def lcd (a, b):
    least = (a * b) / gcd (a , b)
    return least


def smallest_divisible_by_both(n):
    if n <= 1:
        return 1
    else:
        return lcd ( n , smallest_divisible_by_both(n - 1) )

print (int (round (smallest_divisible_by_both(x) ) ) )