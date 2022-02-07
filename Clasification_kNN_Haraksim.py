'''
created by: Daniel Haraksim
project: Classification
description: Goal of this assignement was to classify randomly generated color points with k-NN algorithm
'''
import copy
import random
import math
import time
from collections import Counter
import matplotlib.pyplot as plt

#0-red,1-green,2-blue,3-purp

pocet_bodov = 5000 * 4

#start points
body = {
    (-4500, -4400): 0,
    (-4100, -3000): 0,
    (-1800, -2400): 0,
    (-2500, -3400): 0,
    (-2000, -1400): 0,
    (+4500, -4400): 1,
    (+4100, -3000): 1,
    (+1800, -2400): 1,
    (+2500, -3400): 1,
    (+2000, -1400): 1,
    (-4500, +4400): 2,
    (-4100, +3000): 2,
    (-1800, +2400): 2,
    (-2500, +3400): 2,
    (-2000, +1400): 2,
    (+4500, +4400): 3,
    (+4100, +3000): 3,
    (+1800, +2400): 3,
    (+2500, +3400): 3,
    (+2000, +1400): 3,
}

x_graf = []
y_graf = []
farba_graf = []

for key in body.keys():
    x_graf.append(key[0])
    y_graf.append(key[1])
for value in body.values():
    if value == 0:
        farba_graf.append('red')
    if value == 1:
        farba_graf.append('green')
    if value == 2:
        farba_graf.append('blue')
    if value == 3:
        farba_graf.append('purple')


#generating of random points in assigned intervals
def generuj_body(farba):
    cislo = random.randint(0,100)
    if farba == 0:
        if 0 <= cislo <= 99:
            x = random.randint(-5000,500)
            y = random.randint(-5000,500)
        else:
            x = random.randint(-5000,5000)
            y = random.randint(-5000,5000)
        return x, y

    elif farba == 1:
        if 0 <= cislo <= 99:
            x = random.randint(-500,5000)
            y = random.randint(-5000,500)
        else:
            x = random.randint(-5000,5000)
            y = random.randint(-5000,5000)
        return x, y

    elif farba == 2:
        if 0 <= cislo <= 99:
            x = random.randint(-5000,500)
            y = random.randint(-500,5000)
        else:
            x = random.randint(-5000,5000)
            y = random.randint(-5000,5000)
        return x, y

    elif farba == 3:
        if 0 <= cislo <= 99:
            x = random.randint(-500,5000)
            y = random.randint(-500,5000)
        else:
            x = random.randint(-5000,5000)
            y = random.randint(-5000,5000)
        return x, y

#calculating distance between generated points with euclidean distance formula and sorting them in ascending order
def vzdialenost_funkcia(body, bod):
    vzdialenosti = []

    for key in body.keys():
        bod_dict = key
        euclidean = math.sqrt((bod[0]-bod_dict[0])**2 + (bod[1]-bod_dict[1])**2)
        value = (euclidean,key)
        vzdialenosti.append(value)
    vzdialenosti.sort()
    return vzdialenosti

#classification with k-NN algorithm
def classify(vzdialenosti_list, k, body_dict):
    farby = []
    najblizsie = []
    for i in range(k):
        najblizsie.append(vzdialenosti_list[i]) #finding k nearest neighbors in distance list
    if k == 1:
        key = najblizsie[0][1]
        farba = body_dict.get(key)
    else :
        for j in range(k):
            key = najblizsie[j][1]
            farby.append(body_dict.get(key))
        count = Counter(farby)
        farba = count.most_common(1)[0][0]

    return farba

#variables for graph visualization
kcka = (1,3,7,15)
x_graf_final = []
y_graf_final = []
farba_graf_final = []
x2_graf_final = []
y2_graf_final = []
farba2_graf_final = []
x3_graf_final = []
y3_graf_final = []
farba3_graf_final = []
x4_graf_final = []
y4_graf_final = []
farba4_graf_final = []
fig, axs = plt.subplots(2, 2)


nove_body = copy.deepcopy(body)
testovacie_body = copy.deepcopy(body)
testovacie_pole = []
#using additional list to work with
for keys in testovacie_body.keys():
    testovacie_pole.append(keys)
#checking succession of k-NN algorithm by testing the generated points with different k values
for j in range(4):
    testovacie_body = copy.deepcopy(body)
    k = kcka[j]
    x_graf_nove = []
    y_graf_nove = []
    farba_graf_nove = []
    farba = 0
    spravne = 0
    percenta = 0
    if k == 1:
        start = time.time()
        for i in range(pocet_bodov):
            if farba % 4 == 0:
                farba = 0
            bod = generuj_body(farba)
            if bod in nove_body:
                i -= 1
                continue
            testovacie_pole.append(bod)
            vzdialenosti = vzdialenost_funkcia(nove_body, bod)
            farba_klas = classify(vzdialenosti,k,nove_body)
            x_graf_nove.append(bod[0])
            y_graf_nove.append(bod[1])
            if farba_klas == 0:
                farba_graf_nove.append('red')
            elif farba_klas == 1:
                    farba_graf_nove.append('green')
            elif farba_klas == 2:
                    farba_graf_nove.append('blue')
            elif farba_klas == 3:
                    farba_graf_nove.append('purple')
            nove_body[bod] = farba_klas
            if farba_klas == farba:
                spravne += 1

            farba += 1


        end = time.time()

        percenta = spravne/pocet_bodov * 100
        print(len(testovacie_pole))
        print(f"Uspesnost pre k={k} pre pocet bodov {pocet_bodov} je {spravne} co je: {percenta}% za cas {end - start}")
    else:
        start = time.time()
        i = 1
        for i in range(pocet_bodov):
            if farba % 4 == 0:
                farba = 0
            bod = testovacie_pole[i+20]
            vzdialenosti = vzdialenost_funkcia(testovacie_body, bod)
            farba_klas = classify(vzdialenosti, k, testovacie_body)
            x_graf_nove.append(bod[0])
            y_graf_nove.append(bod[1])
            if farba_klas == 0:
                farba_graf_nove.append('red')
            elif farba_klas == 1:
                farba_graf_nove.append('green')
            elif farba_klas == 2:
                farba_graf_nove.append('blue')
            elif farba_klas == 3:
                farba_graf_nove.append('purple')
            testovacie_body[bod] = farba_klas
            if farba_klas == farba:
                spravne += 1

            farba += 1

        end = time.time()

        percenta = spravne / pocet_bodov * 100
        #print(testovacie_body)
        print(f"Uspesnost pre k={k} pre pocet bodov {pocet_bodov} je {spravne} co je: {percenta}% za cas {end - start}")

    if k == 1:
        x_graf_final = x_graf + x_graf_nove
        y_graf_final = y_graf + y_graf_nove
        farba_graf_final = farba_graf + farba_graf_nove

    if k == 3:
        x2_graf_final = x_graf + x_graf_nove
        y2_graf_final = y_graf + y_graf_nove
        farba2_graf_final = farba_graf + farba_graf_nove

    if k == 7:
        x3_graf_final = x_graf + x_graf_nove
        y3_graf_final = y_graf + y_graf_nove
        farba3_graf_final = farba_graf + farba_graf_nove

    if k == 15:
        x4_graf_final = x_graf + x_graf_nove
        y4_graf_final = y_graf + y_graf_nove
        farba4_graf_final = farba_graf + farba_graf_nove

#visualisation
axs[0,0].scatter(x=x_graf_final, y=y_graf_final, s=50, c=farba_graf_final)
axs[0,1].scatter(x=x2_graf_final, y=y2_graf_final, s=50, c=farba2_graf_final)
axs[1,0].scatter(x=x3_graf_final, y=y3_graf_final, s=50, c=farba3_graf_final)
axs[1,1].scatter(x=x4_graf_final, y=y4_graf_final, s=50, c=farba4_graf_final)

axs[0,0].set_title('k = 1')
axs[0,1].set_title('k = 3')
axs[1,0].set_title('k = 7')
axs[1,1].set_title('k = 15')
while True:
    plt.show()