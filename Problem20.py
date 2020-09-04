print ("Vsota števk: ")
x = int (input ())

def fakulteta(n):
    if n == 0:
        return 1
    else: 
        return n * fakulteta(n - 1)

def vsota_stevk(n):
    seznam = [int(x) for x in str(n)]
    vsota = (sum (i for i in seznam))
    return vsota


print(vsota_stevk(fakulteta(x)))