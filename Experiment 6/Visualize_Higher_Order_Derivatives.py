import matplotlib.pyplot as plt
from sympy import *

def nthOrderDerivative(function, n):
    # Computes the nth order derivative of the function at each angle from -360 to 360 degrees
    derivatives = [diff(function, x, n).subs(x, (angle*pi)/180) for angle in range(-360, 361)]
    return derivatives

def visualizeNthOrderDerivative(function, xaxix_label):
    plt.xlabel(xaxix_label)
    plt.plot(nthOrderDerivative(function, 1), label='1st Order Derivative')
    plt.plot(nthOrderDerivative(function, 2), label='2nd Order Derivative')
    plt.plot(nthOrderDerivative(function, 3), label='3rd Order Derivative')
    plt.plot(nthOrderDerivative(function, 4), label='4th Order Derivative')
    plt.legend()
    plt.show()

x = symbols('x')
plt.title('Visualizing nth Order Derivatives')
plt.xticks(range(0, 721, 60), labels=[str(x) for x in range(-360, 361, 60)])

visualizeNthOrderDerivative(sin(x), 'sin(x)')
visualizeNthOrderDerivative(sin(x)/x, 'sin(x)/x')
visualizeNthOrderDerivative(cos(x**2), 'cos(x^2)')
visualizeNthOrderDerivative(x**5 - 3*x**4 + 2*x**3 + 4*x**2 - 5*x + 1, 'x^5 - 3x^4 + 2x^3 + 4x^2 - 5x + 1')