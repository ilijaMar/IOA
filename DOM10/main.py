import math
import random
import numpy as np


A=(1,4,0)
B=(3,2,0)
C=(2,7,1)
D=(6,3,3)
E=(7,6,5)
F=(5,7,4)

velicina_jata=100

brzina=(0,0,0,0,0,0)
w=0.729
c1=1.494
c2=1.494

def rastojanje(X,Y):
    x1=X[0]
    y1=X[1]
    z1=X[2]

    x2 = Y[0]
    y2 = Y[1]
    z2 = Y[2]

    return math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)


def f(agent):

    S1 = (agent[0],agent[1],agent[2])
    S2 = (agent[3], agent[4], agent[5])
    rastojanjeS1 = rastojanje(S1,A) + rastojanje(S1,B) + rastojanje(S1,C)
    rastojanjeS2 = rastojanje(S2, D) + rastojanje(S2, E) + rastojanje(S2, F)
    rastojanjeS1S2=rastojanje(S1,S2)
    return rastojanjeS1+rastojanjeS2+rastojanjeS1S2



jato=[]
for i in range(0,velicina_jata):
    agent=[]
    koordinate=[]
    for j in range(0,6):
        broj=random.uniform(0,7)
        koordinate.append(broj)
    agent=(koordinate,[0,0,0,0,0,0],koordinate)
    jato.append(agent)




global_best_vrednost=1000000000
global_best_resenje=[]
for i in range(0,velicina_jata):
    tren=f(jato[i][0])
    if tren<global_best_vrednost:
        global_best_vrednost=tren
        global_best_resenje=jato[i][0]

stari_best=0
while stari_best-global_best_vrednost<10**-10:
    for i in range(0,velicina_jata):
        agent=jato[i]


        resenje=np.array(agent[0])
        brzina=np.array(agent[1])
        pb=np.array(agent[2])


        sabirak1=w*brzina
        sabirak2=c1*random.uniform(0,1)*(pb-resenje)
        sabirak3=c2*random.uniform(0,1)*(global_best_resenje-resenje)
        vn = sabirak1 + sabirak2 + sabirak3

        xn = resenje + vn





        for el in vn:

            if el > 0.7:
                el=0.7
            if el<-0.7:
                el=-0.7

        if f(xn)<f(pb):
            pb=xn

        stari_best=global_best_vrednost
        if f(xn)<global_best_vrednost:
            global_best_resenje=xn
            global_best_vrednost=f(xn)

        novi_agent=(xn,vn,pb)
        jato[i]=novi_agent



print(global_best_vrednost)
print(global_best_resenje)