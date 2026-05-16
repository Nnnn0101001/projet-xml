def maxm(l):
    max=l[0]
    for x in l[1:]:
        if x>max:max=x
    return max
def minm(l):
    max=l[0]
    for x in l[1:]:
        if x<max:max=x
    return max
def moyenne(l):
    counter,s=0,0
    for x in l:
        counter+=1
        s+=x
    return s/counter if l else 0
def mediane(l):
    l=sorted(l)
    n=len(l)
    if n%2!=0: return l[n//2]
    else:return moyenne([l[n/2-1],l[n/2]])
def variance(l):
    n=len(l)
    v=0
    for x in l:
        v+=(x-moyenne(l))**2
    return v/n
def ecart_type(l):
    import math
    return math.sqrt(variance(l))
def etendue(l):
    return maxm(l)-minm(l)
def resume_statistique(l):
    return {'minimum':minm(l),
            'maximum':maxm(l),
            'moyenne':moyenne(l),
            'mediane':mediane(l),
            'varince':variance(l),
            'ecart type':ecart_type(l),
            'etendue':etendue(l)}

import random 
data={} 
for jour in range(1,31):
    data.update({jour:{
        "temperature": random.randint(0, 40), # Température entre 0 et 40°C  
        "humidite": random.randint(40, 90), # Humidité entre 40% et 90%  
        "precipitations": random.randint(0, 20), # Précipitations entre 0 et 20 mm  
        "vent": random.randint(0, 100) # Vitesse du vent entre 0 et 100 km/h  
    }} )
def temperatures_uniques(data):
    tems=set()
    for jour in range(1,31):
        tems.add(data[jour]["temperature"])
    return tems
def jour_pluviex(data):
    jrs=[]
    for jour in range(1,31):
        if data[jour]['precipitations']>0:
            jrs.append(jour)
    return jrs
def jours_extems(data):
    jrs=[]
    for jour in range(1,31):
        t=data[jour]['temperature']
        if t<5 or t>35:jrs.append(jour)
    return jrs
def temperature_moyenne(data):
    s=0
    for jour in range(1,31):
        s+=data[jour]['temperature']
    return s/30
def score(data):
    sc=[]
    for jour in range(1,31):
        score=0
        t=data[jour]['temperature']
        h=data[jour]['humidite']
        p=data[jour]['precipitations']
        v=data[jour]['vent']
        if 18<=t<=28:score+=40
        elif 10<=t<=18 or 28<t<=23:score+=30
        else:score+=10
        if 40<=h<=70:score+=20
        elif 30<=t<40 or 70<=t<=80:score+=10
        else:score+=5
        if 0<=t<=2:score+=20
        elif 2<t<=10:score+=10
        else:score+=0
        if 0<=t<=30:score+=20
        elif 30<t<=60 :score+=10
        else:score+=0
        sc.append((jour,score))
    return sc
score_janvier= score(data)
scores=[score_janvier[i][1] for i in range(30)]
meillieur_jrs=[score_janvier[i] for i in range(30) if score_janvier[i][1]==maxm(scores)]
pire_jrs=[score_janvier[i] for i in range(30) if score_janvier[i][1]==minm(scores)]

