import sympy
from sympy import *
from sympy.abc import x, y
import numpy as np
import matplotlib.pyplot as plt


def partial_derivative(my_function, wrt=x):
    """

    :param my_function: function to differentiate
    :param wrt: with respect to
    :return: returns differentiated function
    """
    return diff(my_function, wrt)


# define a function
def f_one(x, y):
    return x ** 2 + ((y ** 2) / 20)

def f_two(x, y):
    return ((x ** 2)/2) + ((y ** 2) / 2)

def f_three(x, y):
    return ((1 - x) ** 2) + (10 * (y - (x ** 2))**2)

def f_four(x, y):
    return ((x ** 2)/2) + (x * sympy.cos(y))


f1 = x ** 2 + ((y ** 2) / 20)
f2 = ((x ** 2)/2) + ((y ** 2) / 2)
f3 = ((1 - x) ** 2) + (10 * (y - (x ** 2))**2)
f4 = ((x ** 2)/2) + (x * sympy.cos(y))

df1x = partial_derivative(f1, x)  # differentiate with respect to x
df1y = partial_derivative(f1, y)  # differentiate with respect to y

df2x = partial_derivative(f2, x)  # differentiate with respect to x
df2y = partial_derivative(f2, y)  # differentiate with respect to y

df3x = partial_derivative(f3, x)  # differentiate with respect to x
df3y = partial_derivative(f3, y)  # differentiate with respect to y

df4x = partial_derivative(f4, x)  # differentiate with respect to x
df4y = partial_derivative(f4, y)  # differentiate with respect to y

print(df1x)
print(df1y)

print(df2x)
print(df2y)

print(df3x)
print(df3y)

print(df4x)
print(df4y)



# plotting
x_list = np.linspace(-10, 10, num=20)

y1list = f_one(x_list, 10)
y2list = f_two(x_list, 10)
y3list = f_three(x_list, 10)
y4list = f_four(x_list, 10)

plt.figure(1)
plt.plot(x_list, y1list)
plt.title("f1")
plt.figure(2)
plt.plot(x_list, y2list)
plt.title("f2")
plt.figure(3)
plt.plot(x_list, y3list)
plt.title("f3")
plt.figure(4)
plt.plot(x_list, y4list)
plt.title("f4")
plt.show()


#do 1.1, 1.2, 2.1, 2.2, 2.3