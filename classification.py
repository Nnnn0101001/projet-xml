from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import pandas as pd

df=pd.read_csv('supermarket_sales.csv')
print("\n\t\t→ SEGMENTATION DES CLIENTS\n")
df['Gender_num']=LabelEncoder().fit_transform(df['Gender'])
x_cluster=df[['Unit price','Quantity','Total','Rating','Gender_num']]
modele_kmeans=KMeans(n_clusters=3,random_state=42,n_init=10)
df['segment']=modele_kmeans.fit_predict(x_cluster)
caracters=['Petit acheteur','Acheteur moyen','Gros acheteur']
moyennes=df.groupby('segment')['Total'].mean().sort_values()
segments={}
for i, seg in enumerate(moyennes.index):
    segments[seg]=caracters[i]
df['nom_segment']=df['segment'].map(segments)


print("\tresultats de segementation:")
for caracter in caracters:
    groupe=df[df['nom_segment']==caracter]
    print(f"\n  {caracter.upper()}")
    print(f"Nombre de clients: {len(groupe)}")
    print(f"Total moyen dépensé: {groupe['Total'].mean():.2f} DH")
    print(f"Quantite moyenne: {groupe['Quantity'].mean():.1f} articles")
    print(f"Rating moyen: {groupe['Rating'].mean():.1f} / 10")


print("\n\tRépartition des segments par catégorie :")
tab = df.groupby(['Product line','nom_segment']).size().unstack(fill_value=0).to_string()
print(tab)


df2=pd.read_csv('resultats_ml.csv')
df2['nom_segment']=df['nom_segment']
df2.to_csv('resultats_ml.csv',index=False)
