import math

mc = int(input('Enter the capacity of m : '))
nc = int(input('Enter the capacity of n : '))
d = int(input('Enter the capacity of d: '))

m = 0
n = 0

if(d % math.gcd(mc, nc) == 0):
    while (m != d and n != d):
        if(m == 0):
            m = mc
        elif(n == nc):
            n = 0
        else:
            transfer = min(m, nc - n)
            m = m - transfer
            n = n + transfer
        
        print(f'({m}, {n})')

else:
    print('No solution')