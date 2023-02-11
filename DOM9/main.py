import math
import random
import numpy as np

S=[2.424595205726587e-01, 1.737226395065819e-01, 1.315612759386036e-01,
 1.022985539042393e-01, 7.905975891960761e-02, 5.717509542148174e-02,
 3.155886625106896e-02, -6.242228581847679e-03, -6.565183775481365e-02,
 -8.482380513926287e-02, -1.828677714588237e-02, 3.632382803076845e-02,
 7.654845872485493e-02, 1.152250132891757e-01, 1.631742367154961e-01,
 2.358469152696193e-01, 3.650430801728451e-01, 5.816044173713664e-01,
 5.827732223753571e-01, 3.686942505423780e-01]



R0=15
N=20
velicina_populacije=60
F=0.8
CR=random.uniform(0,1)
min=100
min_res=[]

def f(x):
    xp1 = x[0]
    yp1 = x[1]
    xp2 = x[2]
    yp2 = x[3]
    A1 = x[4]
    A2 = x[5]

    if math.sqrt(xp1 ** 2 + yp1 ** 2) >= R0 or math.sqrt(xp2 ** 2 + yp2 ** 2) >= R0:
        return 100

    suma = 0

    for i in range(N):
        xi = R0 * math.cos(2 * math.pi * i / N)
        yi = R0 * math.sin(2 * math.pi * i / N)
        sabirak1 = A1 / (math.sqrt((xi - xp1) ** 2 + (yi - yp1) ** 2))
        sabirak2 = A2 / (math.sqrt((xi - xp2) ** 2 + (yi - yp2) ** 2))
        suma += (sabirak1 + sabirak2 - S[i]) ** 2

    return suma


populacija=[]
for i in range(0,velicina_populacije):
    jedinka=[]
    for j in range(0,6):
        jedinka.append(random.uniform(-15,15))
    populacija.append(jedinka)

while min>10**(-14):
    for jed in range(0,velicina_populacije):

        tekuca_jedinka=populacija[jed]

        jedinka_vektor=[]
        brojevi=[]
        for i in range(0,3):
            broj=random.randint(0,59)
            if broj in brojevi:
                broj=random.randint(0,59)
            brojevi.append(broj)

            x_=populacija[broj]
            jedinka_vektor.append(x_)

        xa = jedinka_vektor[0]
        xb = jedinka_vektor[1]
        xc = jedinka_vektor[2]

        z = np.add(xa,F*np.subtract(xb,xc))

        R=random.randint(0,5)
        nova_jedinka=[]
        for i in range(0,6):
            ri=random.uniform(0,1)
            if ri<CR or i==R:
                nova_jedinka.append(z[i])
            else:
                nova_jedinka.append(tekuca_jedinka[i])

        if f(nova_jedinka)<f(tekuca_jedinka):
            populacija[jed]=nova_jedinka
            if f(nova_jedinka)<min:
                min=f(nova_jedinka)
                min_res=nova_jedinka

print(min)
print(min_res)