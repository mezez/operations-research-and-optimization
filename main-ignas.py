import numdifftools as nd
import math
import matplotlib.pyplot as plt
import numpy as np


def f1(x):
    return((x[0]*2)+((x[1]*2)/20))


def f2(x):
    return(((x[0]*2)/2)+((x[1]*2)/2))


def f3(x):
    return(((1-x[0])*2) + (10(x[1]-(x[0]*2)*2)))


def f4(x):
    return(((x[0]**2)/2)+(x[0]*math.cos(x[1])))


def plot():
    x = np.arange(-5., 5., 0.01)
    y = np.arange(-5., 5., 0.01)
    fig1 = plt.figure(figsize=(5, 5))
    ax1 = fig1.add_subplot(111, projection='3d')
    ax1.scatter(x, y, f1([x, y]))
    plt.title("f1")
    fig2 = plt.figure(figsize=(5, 5))
    ax2 = fig2.add_subplot(111, projection='3d')
    ax2.scatter(x, y, f2([x, y]))
    plt.title("f2")
    fig3 = plt.figure(figsize=(5, 5))
    ax3 = fig3.add_subplot(111, projection='3d')
    ax3.scatter(x, y, f3([x, y]))
    plt.title("f3")
    plt.show()


def main():
    grad1 = nd.Gradient(f1)([2, 10])
    grad2 = nd.Gradient(f2)([2, 10])
    grad3 = nd.Gradient(f3)([-1, 1])
    grad4 = nd.Gradient(f4)([2, 0])
    print(grad1, grad2, grad3, grad4)
    plot()


if __name__ == '__main__':
    main()