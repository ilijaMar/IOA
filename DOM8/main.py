import matplotlib.pyplot as plt
import numpy as np
import math
import random

files_size = [173669, 275487, 1197613, 1549805, 502334, 217684, 1796841, 274708, 631252, 148665, 150254, 4784408, 344759, 440109, 4198037, 329673, 28602, 144173, 1461469, 187895, 369313, 959307, 1482335, 2772513, 1313997, 254845, 486167, 2667146, 264004, 297223, 94694, 1757457, 576203, 8577828, 498382, 8478177, 123575, 4062389, 3001419, 196884, 617991, 421056, 3017627, 131936, 1152730, 2676649, 656678, 4519834, 201919, 56080, 2142553, 326263, 8172117, 2304253, 4761871, 205387, 6148422, 414559, 2893305, 2158562, 465972, 304078, 1841018, 1915571]
broj_fajlova = 64  #velicina gena
memory = 2**25
velicina_populacije = 20000
broj_generacija = 50
broj_simulacija = 20

sto_najboljih = 100  #100
verovatnoca = 5  #5

cumulative_minimum = []
for i in range(0, broj_simulacija):
    cumulative_minimum.append([])

fopt_min_array = []
x_min_array = []



def c(c_m):
    r = []
    for x in range(0, broj_generacija * velicina_populacije):
        sum = 0
        for k in range(0, broj_simulacija):
            sum += c_m[k][x]
        sum /= broj_simulacija
        r.append(sum)
    return r

def f1(x):
    sum = 0
    for i in range(0, broj_fajlova):
        if x[i] == 1:
            sum += files_size[i]
    return memory - sum

def f2(x):
    sum = 0
    for i in range(0, broj_fajlova):
        if x[i] == 2:
            sum += files_size[i]
    return memory - sum

def f(x):
    f_1 = f1(x)
    f_2 = f2(x)
    if f_1 >= 0 and f_2 >= 0:
        return f_1 + f_2
    else:
        return memory*2



for k in range(0, broj_simulacija):

    x_min = []
    for p in range(0, broj_fajlova):
        x_min.append(0)
    fopt_min = f(x_min)

    populacija = []
    for i in range(0, 20000):
        jedinka = []
        for i in range(0, 64):
            broj = random.randint(0, 2)
            jedinka.append(broj)
        populacija.append((jedinka, f(jedinka)))


    for g in range(0, broj_generacija):

        if fopt_min < 1500:
            for i in range(0, velicina_populacije):
                cumulative_minimum[k].append(fopt_min)
            continue

        populacija.sort(key=lambda x: x[1])
        x_najboljih = []
        for i in range(0, 100):
            x_najboljih.append(populacija[i])
        nova_populacija = []

        for i in range(0, velicina_populacije):

            if fopt_min < 1500:
                cumulative_minimum[k].append(fopt_min)
                continue

            radnom_roditelj1_index = random.randint(0, 99)
            roditelj1 = x_najboljih[radnom_roditelj1_index][0]

            radnom_roditelj2_index = random.randint(0, 99)
            roditelj2 = x_najboljih[radnom_roditelj2_index][0]


            dete = []
            for j in range(0, broj_fajlova):
                if random.randint(0,1) == 0:
                    dete.append(roditelj1[j])
                else:
                    dete.append(roditelj2[j])

                if verovatnoca > random.randint(0, 99):
                    dete[j] = random.randint(0, 2)

            dete_f = f(dete)
            if fopt_min > dete_f:
                fopt_min = dete_f
                x_min = dete.copy()

            nova_populacija.append((dete, dete_f))
            cumulative_minimum[k].append(fopt_min)

        populacija = nova_populacija.copy()

    x_min_array.append(x_min)
    fopt_min_array.append(fopt_min)
    print("Zavrsio: " + str(k+1))


for k2 in range(0, broj_simulacija):
    plt.plot(range(0, velicina_populacije * broj_generacija), cumulative_minimum[k2])
plt.yscale('log')
plt.xscale('log')
plt.title("Kumulativni minimum (log-log)")
plt.xlabel("Iteracija")
plt.ylabel("Minimum")
plt.show()

x_final = c(cumulative_minimum)
plt.plot(range(0, velicina_populacije * broj_generacija), x_final)
plt.yscale('log')
plt.xscale('log')
plt.title("Srednje najbolje (log-log)")
plt.xlabel("Iteracija")
plt.ylabel("Minimum")
plt.show()

for k3 in range(0, broj_simulacija):
    print(x_min_array[k3])
    print(fopt_min_array[k3])
    print("------------------------------------")

