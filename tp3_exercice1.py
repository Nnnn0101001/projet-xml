import numpy as np
class Enregistrement:
    def __init__(self,temperature,humidite,precipitations,vent,pression,indice_uv):
        self.__temperature=temperature 
        self.__humidite=humidite 
        self.__precipitations=precipitations 
        self.__vent=vent 
        self.__pression= pression 
        self.__indice_uv= indice_uv


    def __str__(self):
        return f"la temperature: {self.__temperature}\nl'humidite: {self.__humidite}\nles precpitations: {self.__precepitation}\nle vent: {self.__vent}\n la pression: {self.__pression}\nl'indice de l'uv: {self.__indice_uv}"

    def getTemperature(self): return self.__temperature
    def setTemperature(self,new_val):self.__temperature=new_val
    def getHumidite(self): return self.__humidite
    def setHumidite(self,new_val):self.__humidite=new_val
    def getPrecipitations(self): return self.__precipitations
    def setPrecipitations(self,new_val):self.__precipitations=new_val
    def getVent(self): return self.__vent
    def setvent(self,new_val):self.__vent=new_val
    def getPression(self):return self.__pression
    def setPression(self,new_val):self.__pression=new_val
    def getIndiceUV(self): return self.__indice_uv
    def setIndiceUV(self,new_val):self.__indice_uv=new_val

    def score(self):
        sc=0
        T=self.__temperature 
        H=self.__humidite
        P=self.__precipitations
        V=self.__vent
        Pr=self.__pression
        UV=self.__indice_uv
        if np.isnan(T):sc+=0
        elif 18<=T<=28:sc+=25
        elif 10<=T<18 or 28<T<=32:sc+=15
        else: sc+=5
        if np.isnan(H):sc+=0
        elif 40<=H<=70:sc+=15
        elif 30<=H<=40 or 70<H<=80:sc+=8
        else: sc+=3
        if np.isnan(P):sc+=0
        elif 0<=P<=2:sc+=15
        elif 2<P<=10:sc+=8
        else: sc+=0
        if np.isnan(V):sc+=0
        elif 0<=V<=30:sc+=15
        elif 30<V<=60:sc+=8
        else: sc+=0
        if np.isnan(Pr):sc+=0
        elif 1010<=Pr<=1025:sc+=15
        elif 1000<=Pr<1010 or 1025<Pr<=1035:sc+=8
        else: sc+=3
        if np.isnan(UV):sc+=0
        elif 0<=UV<=5:sc+=15
        elif 5<UV<=7:sc+=8
        else: sc+=2
        return sc
    
class Station:

    def __init__(self,nom,localisation):
        self.__nom=nom
        self.__localisation=localisation
        self.__data={}

    def __str__(self):
        return f"nom: {self.__nom}\nlocalisation: {self.__localisation}"
    
    def getNom(self):return self.__nom
    def setNom(self,new_val):self.__nom=new_val
    def getLocalisation(self):return self.__localisation
    def setLocalisation(self,new_val):self.__localisation=new_val
    def getData(self): return self.__data


    def chargerDonnees(self):

        import random
        annee=[("janvier",31), 
        ("fevrier",29), 
        ("mars",31), 
        ("avril",30), 
        ("mai",31), 
        ("juin",30), 
        ("juillet",31), 
        ("aout",31), 
        ("septembre",30), 
        ("octobre",31), 
        ("novembre",30), 
        ("decembre",31)] 
        for mois,jours in annee:
            self.__data[mois]={}
            for jour in range(1,jours+1):
                self.__data[mois][jour]=Enregistrement(
                    random.choice([np.nan, random.randint(0, 40)]), # temperature
                    random.choice([np.nan, random.randint(0, 100)]), # humidite
                    random.choice([np.nan, random.randint(0, 20)]), # precipitations
                    random.choice([np.nan, random.randint(0, 100)]), # vent
                    random.choice([np.nan, random.randint(980, 1040)]), # pression
                    random.choice([np.nan, random.randint(0, 11)]) # indice_uv
                )

    def temperature_uniques(self,mois):
        temperatures=set()
        for enregistrement in self.__data[mois].values():
            tem=enregistrement.getTemperature()
            temperatures.add(tem)
        return temperatures
        
    def temperature_moyenne(self,mois):
        my=0
        counter=0
        for enrg in self.__data[mois].values():
            if not np.isnan(enrg.getTemperature()):
                my+=enrg.getTemperature()
                counter+=1
        return my/counter if counter>0 else 0

    def jours_pluvieux(self,mois):
        jrs=[]
        Nb_jr=0
        for engs in self.__data[mois].values():
            Nb_jr+=1
            P=engs.getPrecipitations()
            if not np.isnan(P) and P>0:
                jrs.append(Nb_jr)
        return jrs

    def jours_extemes(self,mois):
        jrs=[]
        Nb_jr=0
        for engs in self.__data[mois].values():
            Nb_jr+=1
            T=engs.getTemperature()
            if not np.isnan(T) and (T<5 or T>35):
                jrs.append(Nb_jr)
        return jrs
    
    def humidite_moyenne(self,mois):
        my=0
        counter=0
        for enrg in self.__data[mois].values():
            if not np.isnan(enrg.getHumidite()):
                my+=enrg.getHumidite()
                counter+=1
        return my/counter if counter>0 else 0
    
    def precipitations_totales(self,mois):
        sum=0
        for enrg in self.__data[mois].values():
            if not np.isnan(enrg.getPrecipitatins()):
                sum+=enrg.getPrecipitatins()
        return sum
    
    def jours_beaux(self,mois):
        jrs=[]
        Nb_jr=0
        for engs in self.__data[mois].values():
            Nb_jr+=1
            if engs.score()>=80:
                jrs.append(Nb_jr)
        return jrs

    def score_moyen(self,mois):
        sum=0
        counter=0
        for engs in self.__data[mois].values():
            counter+=1
            sum+=engs.score()
        return sum/counter
    
    def mois_beau(self):
        score_max=0
        plus_BM=''
        for mois,eng_jours in self.__data.items():
            score_mois=0
            for eng in eng_jours.values():
                score_mois+=eng.score()
            if score_mois>score_max:
                score_max=score_mois
                plus_BM=mois
    
        return plus_BM
    
    def exporter_csv(self):
        import csv
        nom=self.__nom
        station=[]
        for mois,engs_jrs in self.__data.items():
            for jour,eng in engs_jrs.items():
                station.append({
                    'nom':nom,
                    'mois':mois,
                    'jour':jour,
                    'score':eng.score(),
                    'temperature':eng.getTemperature(),
                    'humidite':eng.getHumidite(),
                    'precipitations':eng.getPrecipitations(),
                    'vent':eng.getVent(),
                    'pression':eng.getPression(),
                    'indice_uv':eng.getIndiceUV()
                })
        keys=station[0].keys()
        with open(f"C:/Users/nadya/OneDrive/nadyas/{nom}.csv",'w',encoding='utf-8-sig',newline='') as file:
            dic_file=csv.DictWriter(file,keys)
            dic_file.writeheader()
            dic_file.writerows(station)
        return 'file created :)'

#test test    
s_casa=Station('Station_casa',(33.57, -7.58, 4))
s_fes=Station('Station_fes',(34.03, -5.00, 410))
s_rabat=Station('Station_rabat',(34.02, -6.84, 21))
s_marrakech=Station('Station_marrakech',(31.63, -7.98, 466))
s_casa.chargerDonnees()
s_fes.chargerDonnees()
s_rabat.chargerDonnees()
s_marrakech.chargerDonnees()
# print(s_casa.temperature_moyenne('janvier'))
# print(s_marrakech.getData()['mars'][1].getTemperature())
# print(s_marrakech.temperature_uniques('mars'))

#Générer les fichiers csv
import pickle
stations=[s_casa,s_marrakech,s_rabat,s_fes]
for station in stations:
    station.exporter_csv()
with open("stations.pkl",'wb') as file_pkl:
    pickle.dump(stations,file_pkl)
    