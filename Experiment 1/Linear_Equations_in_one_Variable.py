def linear_equ_one_var(a, b, c):
    x = (c - b) / a
    return x

print('Equation Format : ax + b = c')
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

x = linear_equ_one_var(a, b, c)
print(f'Value of x : {x}')