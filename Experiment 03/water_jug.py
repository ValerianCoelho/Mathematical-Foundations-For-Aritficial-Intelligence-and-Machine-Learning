import math

# Get container capacities and desired amount from user input
mc = int(input('Enter the capacity of m : '))  # Capacity of Container M
nc = int(input('Enter the capacity of n : '))  # Capacity of Container N
d = int(input('Enter the desired amount: '))   # Desired amount to achieve in both containers

# Initialize container levels
m = 0  # Current level of Container M
n = 0  # Current level of Container N

# Check if the desired amount is achievable using given containers
if d % math.gcd(mc, nc) == 0:
    while (m != d and n != d):
        # If Container M is empty, fill it to its capacity
        if m == 0:
            m = mc
        # If Container N is full, empty it
        elif n == nc:
            n = 0
        else:
            # Transfer as much as possible from M to N
            transfer = min(m, nc - n)
            m -= transfer
            n += transfer
        
        # Print current container levels
        print(f'Container M: {m}, Container N: {n}')

    print('Desired amount achieved!')
else:
    print('No solution')
