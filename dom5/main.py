import math
import numpy as np
import matplotlib.pyplot as plt
import random
import scipy
from scipy.optimize import Bounds


def aktivaiona(x):
    return (math.exp(x) - math.exp(-x))/(math.exp(x) + math.exp(-x))

def ytrening(x):

    return -1 + 2*( pow(math.sin(math.pi*0.5*(x+1)), 4) + 1/4*( pow(math.sin(math.pi*0.5 * pow(1-abs( math.cos( math.pi*0.25*(x+1) ) ) , 4)) , 4) ) )


w = []
for i in range(0,16):
    w.append( -5 + 10*random.random() )


def yizlaz(x, w):
    r = 0
    r += w[15]
    for i in range(1,6):
        r += w[i+10] * aktivaiona( w[i]*x + w[i+5] )
    return r

donja_granica_x = -1
gornja_granica_x = 1.02
korak = 0.02
x_in = np.arange(donja_granica_x, gornja_granica_x, korak)

def f(w):
    r = 0
    for x in x_in:
        r +=  pow( (yizlaz(x, w) - ytrening(x)) , 2)
    return r/101
# r +=1/101 *  pow( (yizlaz(x, w) - ytrening(x)) , 2)





preciznost = 0.0001
rezultat = []

w_trening = w
while True:
    rezultat = scipy.optimize.minimize(f, w_trening, method='nelder-mead',bounds=Bounds(-5,5))
    w_trening = rezultat.x
    if rezultat.fun < preciznost:
        break

print(f'Optimizaciona funkcija: {rezultat.fun:.15f}')
print("Tezine:")
for count,i in enumerate(w_trening):
    print(f'w{count}: {i:.15f}', end="  ")


y1 = []
y2 = []
for x in x_in:
    y1.append(ytrening(x))
    y2.append(yizlaz(x, w_trening))

plt.plot(x_in,y1, label = 'ytrening')
plt.plot(x_in,y2, label = 'yilzaz')


plt.legend()
plt.grid()
plt.show()
