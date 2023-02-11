import matplotlib.pyplot as plt
import numpy as np
import random
import math

fajlovi = [173669, 275487, 1197613, 1549805, 502334, 217684, 1796841, 274708, 631252, 148665, 150254, 4784408, 344759, 440109, 4198037, 329673, 28602, 144173, 1461469, 187895, 369313, 959307, 1482335, 2772513, 1313997, 254845, 486167, 2667146, 264004, 297223, 94694, 1757457, 576203, 8577828, 498382, 8478177, 123575, 4062389, 3001419, 196884, 617991, 421056, 3017627, 131936, 1152730, 2676649, 656678, 4519834, 201919, 56080, 2142553, 326263, 8172117, 2304253, 4761871, 205387, 6148422, 414559, 2893305, 2158562, 465972, 304078, 1841018, 1915571]
resenje_prev = []

for i in range(64): #random resenje generisemo
    resenje_prev.append(random.randint(0, 2))

T_poc = 64*1024*1024
T = T_poc
max_br_iter = 100000
memorija = 2**25

min_h = 1
max_h = 8
curr_h = max_h

def f1(resenje):
    rez = 2**25
    for i in range(len(resenje)):
        if resenje[i] == 1:
            rez -= fajlovi[i]
    return rez

def f2(resenje):
    rez = 2**25
    for i in range(len(resenje)):
        if resenje[i] == 2:
            rez -= fajlovi[i]
    return rez

def f(resenje):
    f1_rez = f1(resenje)
    f2_rez = f2(resenje)

    if f1_rez < 0 or f2_rez < 0:
        return 2**26
    else:
        return f1_rez + f2_rez

def srednje_resenje(kumulativni_min): #srednji min za sve iteracije
    resenje = []
    for i in range(10*max_br_iter):
        zbir: float = 0
        for pokretanje in range(20): #za svako pokretanje
            zbir += kumulativni_min[pokretanje][i]
        zbir /= 20
        resenje.append(zbir)
    return resenje

minimumi=[]
for m in range(20):
    minimumi.append([])

min_resenje = resenje_prev
f_opt_rez_prev = f(resenje_prev)
min_f_opt = f_opt_rez_prev

for broj_pustanja in range(20):
    print(min_f_opt)
    #if min_f_opt < 1500:
    #    break

    resenje_prev = []

    for i in range(64):  # random resenje generisemo
        resenje_prev.append(random.randint(0, 2))

    f_opt_rez_prev = f(resenje_prev)

    kreniIzNajbolje = False

    min_f_opt_curr_pokretanje: int = 1e9

    for kaljenje_iter in range(10):
        T = T_poc
        curr_h = max_h

        if kreniIzNajbolje:
            resenje_prev = min_resenje
            f_opt_rez_prev = min_f_opt

        kreniIzNajbolje = True

        for iter in range(1, max_br_iter + 1):
            if min_f_opt_curr_pokretanje <= 1500:
                minimumi[broj_pustanja].append(min_f_opt_curr_pokretanje)
                continue

            resenje_curr = resenje_prev.copy()

            poz_za_promeniti = random.sample(range(0, len(resenje_prev)), curr_h)
            for poz in poz_za_promeniti:
                moguce_vrednosti = [0, 1, 2]
                moguce_vrednosti.remove(resenje_curr[poz]) #necemo da menjamo s onim sto je vec na toj poz
                resenje_curr[poz] = random.choice(moguce_vrednosti)

            f_opt_rez_curr = f(resenje_curr)

            delta_E = f_opt_rez_curr - f_opt_rez_prev

            if delta_E < 0: #prihvatamo
                f_opt_rez_prev = f_opt_rez_curr
                resenje_prev = resenje_curr
            else:
                p_vrv = 0.5 if delta_E == 0 else math.e**(-delta_E/T)
                rand_br = random.random()

                if rand_br <= p_vrv: #prihvatamo
                    f_opt_rez_prev = f_opt_rez_curr
                    resenje_prev = resenje_curr

            if f_opt_rez_curr < min_f_opt_curr_pokretanje:
                min_f_opt_curr_pokretanje = f_opt_rez_curr
                if min_f_opt_curr_pokretanje < min_f_opt:
                    min_f_opt = min_f_opt_curr_pokretanje

            T *= 0.95 #hladimo
            curr_h = round((min_h - max_h)/(max_br_iter-1)*(iter-1) + max_h)

            minimumi[broj_pustanja].append(min_f_opt_curr_pokretanje)

    plt.plot(range(10*max_br_iter), minimumi[broj_pustanja], label='pokretanje ' + str(broj_pustanja))

plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

plt.plot(range(10*max_br_iter), srednje_resenje(minimumi))
plt.xscale('log')
plt.yscale('log')
plt.show()

print(min_f_opt)
print(min_resenje)