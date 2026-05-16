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
    def  setData(self,new_val):self.__data=new_val


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
        # (temperature, humidite, precipitations, vent, pression, indice_uv) 
        moyennes = { 
            "janvier": (12, 75, 5, 18, 1018, 2), 
            "fevrier": (13, 72, 4, 18, 1017, 3), 
            "mars": (16, 68, 3, 17, 1016, 4), 
            "avril": (18, 63, 3, 16, 1015, 5), 
            "mai": (22, 58, 2, 15, 1014, 7), 
            "juin": (26, 52, 1, 14, 1013, 9), 
            "juillet": (30, 45, 0.5, 13, 1012, 10), 
            "aout": (31, 47, 0.5, 13, 1012, 10), 
            "septembre": (27, 55, 2, 14, 1014, 8), 
            "octobre": (22, 63, 3, 15, 1015, 5), 
            "novembre": (17, 70, 4, 17, 1017, 3), 
            "decembre": (13, 76, 5, 18, 1018, 2) 
        } 
        for year in range(2023,2026):
            for mois,jours in annee:
                self.__data[year]={}
                self.__data[year][mois]={}
                for jour in range(1,jours+1):
                    self.__data[year][mois][jour]=Enregistrement(
                        random.choice([np.nan, np.clip(np.random.normal(moyennes[mois][0], 3), -5, 45)]), # temperature
                        random.choice([np.nan, np.clip(np.random.normal(moyennes[mois][1], 10), 0,100)]), # humidite
                        random.choice([np.nan, np.clip(np.random.normal(moyennes[mois][2], 2), -0, 50)]), # precipitations
                        random.choice([np.nan, np.clip(np.random.normal(moyennes[mois][3], 15), 0, 150)]), # vent
                        random.choice([np.nan, np.clip(np.random.normal(moyennes[mois][4], 5), 950, 1050)]), # pression
                        random.choice([np.nan, np.clip(np.random.normal(moyennes[mois][5], 2), 0, 15)]) # indice_uv
                    )

    def temperature_uniques(self,year,mois):
        temperatures=set()
        for enregistrement in self.__data[year][mois].values():
            tem=enregistrement.getTemperature()
            temperatures.add(tem)
        return temperatures
        
    def temperature_moyenne(self,year,mois):
        my=0
        counter=0
        for enrg in self.__data[year][mois].values():
            if not np.isnan(enrg.getTemperature()):
                my+=enrg.getTemperature()
                counter+=1
        return my/counter if counter>0 else 0

    def jours_pluvieux(self,year,mois):
        jrs=[]
        Nb_jr=0
        for engs in self.__data[year][mois].values():
            Nb_jr+=1
            P=engs.getPrecipitations()
            if not np.isnan(P) and P>0:
                jrs.append(Nb_jr)
        return jrs

    def jours_extemes(self,year,mois):
        jrs=[]
        Nb_jr=0
        for engs in self.__data[year][mois].values():
            Nb_jr+=1
            T=engs.getTemperature()
            if not np.isnan(T) and (T<5 or T>35):
                jrs.append(Nb_jr)
        return jrs
    
    def humidite_moyenne(self,year,mois):
        my=0
        counter=0
        for enrg in self.__data[year][mois].values():
            if not np.isnan(enrg.getHumidite()):
                my+=enrg.getHumidite()
                counter+=1
        return my/counter if counter>0 else 0
    
    def precipitations_totales(self,year,mois):
        sum=0
        for enrg in self.__data[year][mois].values():
            if not np.isnan(enrg.getPrecipitatins()):
                sum+=enrg.getPrecipitatins()
        return sum
    
    def jours_beaux(self,year,mois):
        jrs=[]
        Nb_jr=0
        for engs in self.__data[year][mois].values():
            Nb_jr+=1
            if engs.score()>=80:
                jrs.append(Nb_jr)
        return jrs

    def score_moyen(self,year,mois):
        sum=0
        counter=0
        for engs in self.__data[year][mois].values():
            counter+=1
            sum+=engs.score()
        return sum/counter
    
    def mois_beau(self,year):
        score_max=0
        plus_BM=''
        for mois,eng_jours in self.__data[year].items():
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
        for year in range(2023,2026):
            for mois,engs_jrs in self.__data[year].items():
                for jour,eng in engs_jrs.items():
                    station.append({
                        'annee':year,
                        'nom':nom,
                        'mois':mois,
                        'jour':jour,
                        'temperature':eng.getTemperature(),
                        'humidite':eng.getHumidite(),
                        'precipitations':eng.getPrecipitations(),
                        'vent':eng.getVent(),
                        'pression':eng.getPression(),
                        'indice_uv':eng.getIndiceUV(),
                        'score':eng.score()
                    })
        keys=station[0].keys()
        with open(f"C:/Users/nadya/OneDrive/nadyas/{nom}.csv",'w',encoding='utf-8-sig',newline='') as file:
            dic_file=csv.DictWriter(file,keys)
            dic_file.writeheader()
            dic_file.writerows(station)
        return 'file created :)'

#test test    
s_casa2=Station('Station_casa2',(33.57, -7.58, 4))
s_fes2=Station('Station_fes2',(34.03, -5.00, 410))
s_rabat2=Station('Station_rabat2',(34.02, -6.84, 21))
s_marrakech2=Station('Station_marrakech2',(31.63, -7.98, 466))


import pickle
stations=[s_casa2,s_marrakech2,s_rabat2,s_fes2]
for station in stations:
    station.chargerDonnees()
    station.exporter_csv()
with open("stations.pkl",'wb') as file_pkl:
    pickle.dump(stations,file_pkl)

