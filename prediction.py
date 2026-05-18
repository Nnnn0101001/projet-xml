from sklearn.ensemble import RandomForestRegressor
import pandas as pd

df=pd.read_csv('supermarket_sales.csv')
print("\n\t\t→ PREDICTION DES VENTES\n")
x_prediction=df[['Unit price','Quantity']]
y_prediction=df['Total']
modele_prediction=RandomForestRegressor(random_state=42)
modele_prediction.fit(x_prediction,y_prediction)
print(f'le score de modele est {modele_prediction.score(x_prediction,y_prediction)}')
exemple=pd.DataFrame({
    'Unit price':[25,40,10],
    'Quantity':[1,2,5]
})
predictions=modele_prediction.predict(exemple)
print("\n\t\tExemple de predictions:")
print(f"Prix=25 DH, Quantite=1  → Total predit : {predictions[0]:.2f} DH")
print(f"Prix=40 DH, Quantite=2  → Total predit : {predictions[1]:.2f} DH")
print(f"Prix=10 DH, Quantite=5  → Total predit : {predictions[2]:.2f} DH")
df['Date']=pd.to_datetime(df['Date'])
df['Mois']=df['Date'].dt.month
ventes_par_mois=df.groupby('Mois')['Total'].sum().reset_index()
for _,row in ventes_par_mois.iterrows():
    print(f'\tMois: {int(row['Mois']):02d}: {row['Total']:.2f} DH')