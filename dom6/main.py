import math
import numpy as np
import matplotlib.pyplot as plt
import random
import scipy

racunar_servis_vreme = [[5,7,4,10], [6,12,8,15], [13,14,9,17]]
racunar_servis_cena = [[10,8,6,9],[18,20,15,17],[15,16,13,17]]

broj_zahteva1 = 1000
broj_zahteva2 = 600
broj_zahteva3 = 500
trajanje = 48*60


koeficijenti = racunar_servis_cena[0] + racunar_servis_cena[1] + racunar_servis_cena[2]
linearni_koeficijenti_min = [ -1 * x for x in koeficijenti]

linearni_koeficijenti_nejed =[
 [1,1,1,1,0,0,0,0,0,0,0,0],
 [0,0,0,0,1,1,1,1,0,0,0,0],
 [0,0,0,0,0,0,0,0,1,1,1,1],
 [racunar_servis_vreme[0][0],0,0,0,racunar_servis_vreme[1][0],0,0,0,racunar_servis_vreme[2][0],0,0,0],
 [0,racunar_servis_vreme[0][1],0,0,0,racunar_servis_vreme[1][1],0,0,0,racunar_servis_vreme[2][1],0,0],
 [0,0,racunar_servis_vreme[0][2],0,0,0,racunar_servis_vreme[1][2],0,0,0,racunar_servis_vreme[2][2],0],
 [0,0,0,racunar_servis_vreme[0][3],0,0,0,racunar_servis_vreme[1][3],0,0,0,racunar_servis_vreme[2][3]]
]

gornje = [broj_zahteva1,broj_zahteva2,broj_zahteva3,trajanje,trajanje,trajanje,trajanje]

simplex = scipy.optimize.linprog(c=linearni_koeficijenti_min,A_ub=linearni_koeficijenti_nejed,b_ub=gornje,method='simplex')







def uslovi(x):
    if x[0] + x[1] + x[2] + x[3] > broj_zahteva1 and \
       x[4] + x[5] + x[6] + x[7] > broj_zahteva2 and \
       x[8] + x[9] + x[10] + x[11] > broj_zahteva3 and \
       x[0] * racunar_servis_vreme[0][0] + x[4] * racunar_servis_vreme[1][0] + x[8] * racunar_servis_vreme[2][0] > trajanje and \
       x[1] * racunar_servis_vreme[0][1] + x[5] * racunar_servis_vreme[1][1] + x[9] * racunar_servis_vreme[2][1] > trajanje and \
       x[2] * racunar_servis_vreme[0][2] + x[6]*racunar_servis_vreme[1][2] + x[10]*racunar_servis_vreme[2][2] > trajanje and \
       x[3] * racunar_servis_vreme[0][3] + x[7] * racunar_servis_vreme[1][3] + x[11] * racunar_servis_vreme[2][3] > trajanje:
       return False
    return True





def zaokruzi(rezultat_int,rezultat_bool):

    if uslovi(rezultat_int):
        return rezultat_int
    else:
        for index, val in enumerate(rezultat_bool):
            if rezultat_bool[index] == True and rezultat_int[index] > simplex.x[index]:
                rezultat_int[index] -=  1

    return rezultat_int



rezultat_int=[]
rezultat_bool=[]
for x in simplex.x:
    rezultat_int.append(round(x))

for x in simplex.x:
    rezultat_bool.append(round(x)>x)


print("Zaokruzeno:")
zaokruzeno = zaokruzi(rezultat_int,rezultat_bool)
print(zaokruzeno)

def zarada(C):
    return C[0]*racunar_servis_cena[0][0] + C[1]*racunar_servis_cena[0][1] + C[2]*racunar_servis_cena[0][2] + C[3]*racunar_servis_cena[0][3] + C[4]*racunar_servis_cena[1][0] + C[5]*racunar_servis_cena[1][1] + C[6]*racunar_servis_cena[1][2] + C[7]*racunar_servis_cena[1][3] + C[8]*racunar_servis_cena[2][0] + C[9]*racunar_servis_cena[2][1] + C[10]*racunar_servis_cena[2][2] + C[11]*racunar_servis_cena[2][3]

print("Zarada:")
print(zarada(zaokruzeno))


