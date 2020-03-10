import numpy as np
import matplotlib.pyplot as plt
import os


def task1():
    os.mkdir("results")
    f = open('results/task_01_4O-506C_Podberezniy_4.txt', 'w')
    x = np.linspace(-10, 10, 21)
    print(' x \t f(x)', file=f)
    y = (np.sin(3 * np.pi * x)**2) + ((x - 1)**2) * (1 + np.sin(3 * np.pi)**2)
    for i in range(21):
        print(x[i], '\t', y[i], file=f, end="\n")
    f.close()
    plt.figure()
    plt.plot(x, y)
    plt.grid()
    plt.savefig('image.png')
    plt.show()


if os.path.exists('results'):
    os.remove('results/task_01_4O-506C_Podberezniy_4.txt')
    os.rmdir("results")
    task1()
else:
    task1()
