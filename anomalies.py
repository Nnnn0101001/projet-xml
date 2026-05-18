import pandas as pd
from sklearn.ensemble import IsolationForest

df=pd.read_csv('supermarket_sales.csv')
print("\n\t\t→ DETECTION D'ANOMALIES\n")
colonnes_anomalie=['Unit price','Quantity','Total']
X_anomalie=df[colonnes_anomalie]
modele_anomalie=IsolationForest(contamination=0.05,random_state=42)
df['anomalie']=modele_anomalie.fit_predict(X_anomalie)
anomalies=df[df['anomalie']==-1]
normales=df[df['anomalie']==1]
print('les ventes normales: ',len(normales))
print('les ventes anormales: ',len(anomalies))
print('\n\t\texemples de ventes anomalies détectées:')
print(anomalies[['Branch','Product line','Unit price','Quantity','Total']].head(5).to_string(index=False))

resultats = df[[
    'Invoice ID','Branch','City','Customer type','Gender',
    'Product line','Unit price','Quantity','Total',
    'Date','Payment','Rating','anomalie']].copy()
resultats['anomalie'] = resultats['anomalie'].map({1: 'Normal', -1: 'Anomalie'})
resultats.to_csv('resultats_ml.csv', index=False)
