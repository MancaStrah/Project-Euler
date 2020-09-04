# 2 ** 15 = 32768 and the sum of its digits
# is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2 ** 1000?

print ("Sum of digits of the number two to the power of ")
x = int (input() )

number = 2 ** x

def sum_of_digits(n):
    if ( n // 10 ) == 0:
        return n
    else:
        return (n % 10) + sum_of_digits (n // 10)

print(sum_of_digits(number))

