import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10, 10, 21)

f=open('results/task_01_4O-506C_Podberezniy_4.txt','w')
print(' x ' + '    '+' f(x) ',file=f )
for valuex in x:
	valuey=(np.sin(3*np.pi*valuex)**2)+((valuex-1)**2) *(1+np.sin(3*np.pi)**2)
	print(str(valuex)+'    '+str(valuey), file=f, end="\n")
f.close()
y=(np.sin(3*np.pi*x)**2)+((x-1)**2) *(1+np.sin(3*np.pi)**2)
plt.figure
plt.plot(x,y)
plt.grid()
plt.show()

