import numpy as np
import matplotlib.pyplot as plt
import os


def task1():
    f = open('results/task_01_4O-506C_Podberezniy_4.txt', 'w')
    x = np.linspace(-10, 10, 21)
    print(' x ' + '    ' + ' f(x) ', file=f)
    for valuex in x:
        valuey = (np.sin(3 * np.pi * valuex)**2) + \
            ((valuex - 1)**2) * (1 + np.sin(3 * np.pi)**2)
        print(str(valuex) + '    ' + str(valuey), file=f, end="\n")
    f.close()
    y = (np.sin(3 * np.pi * x)**2) + ((x - 1)**2) * (1 + np.sin(3 * np.pi)**2)
    plt.figure()
    plt.plot(x, y)
    plt.grid()
    plt.show()
    return()


try:  # Если папка result и файл в ней существуют
    os.remove('results/task_01_4O-506C_Podberezniy_4.txt')
    os.rmdir("results")
    os.mkdir('results')
    task1()
except OSError:
    try:  # Если нет папки и файла
        os.mkdir('results')
        task1()
    except OSError:  # Если нет только файла
        task1()
