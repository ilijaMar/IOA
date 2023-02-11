import math
import numpy as np
import matplotlib.pyplot as plt

n = 5
beta = 20*math.pi
d = 0.05
teta = math.pi/4
donjaGranica = 0
gornjaGranica = 2*math.pi
brojTacaka = 100
preciznost = 1e-07

def Fs(n, delta , beta , d, teta):

    f = delta+beta*d*math.cos(teta)

    i = complex(0,1)
    resultat = 0
    for k in range(0,n):
        exp = -i*k*f
        resultat += pow(math.e, exp)

    return resultat

def Fsmoduo(c:complex):
    return abs(c)

############################################
fig = plt.figure()
delta_x = np.linspace(donjaGranica, gornjaGranica, brojTacaka)

y = []

for delta in delta_x:
    F = Fs(n, delta, beta, d, teta)
    y.append(Fsmoduo(F))

plt.plot(delta_x,y, label = 'f')
############################################


def Fsizvod(n: float, delta:float , beta:float , d:float, teta:float, deltaX:float = 1e-09): #formula za racunanje izvoda
    izvod = (Fsmoduo(Fs(n, delta + deltaX, beta, d, teta)) - Fsmoduo(Fs(n, delta, beta, d, teta))) / deltaX
    return izvod


############################################
y2 = []
y_zero = []
for delta in delta_x:
    y2.append(Fsizvod(n, delta, beta, d, teta, preciznost))
    y_zero.append(0)


plt.plot(delta_x,y2, label = "f'")
plt.plot(delta_x, y_zero)

############################################








plt.legend()
plt.show()

#polovljenje intervala
a=3
b=5
x1=0.5*(a+b)

while abs(Fsizvod(n,x1,beta,d,teta))>preciznost:
    nx1=Fsizvod(n,x1,beta,d,teta)
    na = Fsizvod(n, a, beta, d, teta)
    nb = Fsizvod(n, b, beta, d, teta)

    if nx1*na<0:
        b=x1
    elif nx1*nb<0:
        a=x1
    else:
        print("ERROR")

    x1=0.5*(a+b)

print("Maksimum: " + str(round(Fsmoduo(Fs(n, x1, beta, d, teta)), 8)) + " za delta: " + str(round(x1, 8)))



