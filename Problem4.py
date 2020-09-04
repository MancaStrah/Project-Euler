# A palindromic number reads the same both ways. The
# largest palindrome made from the product of two 2-digit
# numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of 
# two 3-digit numbers.

kandidati = list(range(10000, 998001))
palindromi = []
for stevilo in kandidati:
    if str(stevilo) == (str(stevilo))[::-1]:
        palindromi.append(stevilo)

palindromi.reverse()

for palindrom in palindromi:
    for j in range (100, 1000):
        if palindrom % j == 0 and len(str(palindrom // j)) == 3:
            print(palindrom)
            break
    

      
       
