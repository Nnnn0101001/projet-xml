from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import IsolationForest
import pandas as pd

df=pd.read_csv('supermarket_sales.csv')

""""moyenne simple VS  ML RandomForestRegressor"""

# moyenne simple
moyenne=df['Total'].mean()
erreur_mean=abs(df['Total']-moyenne).mean()
print("\n\tMoyenne simple")
print(f'prediction constante: {moyenne:.2f} DH')
print(f'erreur: {erreur_mean:.2f} DH')
print(f"probleme: ignore le prix et la quantite reels et toute vente vaut en moyenne")

# ML RandomForestRegressor
x_prediction=df[['Unit price','Quantity']]
y_prediction=df['Total']
modele_prediction=RandomForestRegressor(random_state=42)
prediction_ML=modele_prediction.fit(x_prediction,y_prediction)
score_R2=modele_prediction.score(x_prediction,y_prediction)
erreur_ML=abs(df['Total']-prediction_ML).mean()
print("\n\tML RandomForestRegressor")
print(f'score ML: {score_R2:.2f}')
print(f"erreur ML: {erreur_ML:.2f} DH")
print(f"elle adapte la prediction au prix ET a la quantite")


""""methode IQR (ecart interquartile) VS ML IsolationForest"""

#methode IQR (ecart interquartile)
#les quartiles:
Q1=df['Total'].quantile(0.25)
Q3=df['Total'].quantile(0.75)
IQR=Q3-Q1
limite_basse=Q1-1.5*IQR
limite_haute=Q3+1.5*IQR
anomalies_IQR=df[(df['Total']<limite_basse)|(df['Total']>limite_haute)]
print("\n\tMethode classique: IQR sur colonne Total")
print(f"Q1: {Q1:.2f} DH")
print(f"Q3: {Q3:.2f} DH")
print(f"IQR: {IQR:.2f} DH")
print(f"Limite basse: {limite_basse:.2f} DH")
print(f"Limite haute: {limite_haute:.2f} DH")
print(f"Anomalies detectees: {len(anomalies_IQR)}")
print(f"Probleme: regarde UNE seule colonne (Total)")

# ML IsolationForest
colonnes_anomalie=['Unit price','Quantity','Total']
X_anomalie=df[colonnes_anomalie]
modele_anomalie=IsolationForest(contamination=0.05,random_state=42)
df['anomalie']=modele_anomalie.fit_predict(X_anomalie)
anomalies_ML=df[df['anomalie']==-1]
print("\n\tML IsolationForest")
print(f"Anomalies detectees: {len(anomalies_ML)}")
print(f"Colonnes analysees: Unit price, Quantity, Total")
print(f"avantage : detecte des combinaisons suspectes")
print(f"Exemple : Quantite=95 avec Total=690 DH => suspect meme sile Total seul semble dans la normale")
