# Importo le librerie necessarie
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ricopio il dataset
url = 'https://zenodo.org/record/5898311/files/vgsales.csv'
df = pd.read_csv(url)
print(df.head())

# Calcolo il numero di videogiochi pubblicati in totale
numero_giochi = df.shape[0]
print("\nNumero di videogiochi pubblicati: ", numero_giochi)

# Creo un bar plot per momstrare i generi più popolari
generi_più_popolari = df['Genre'].value_counts()
plt.figure(figsize=(8,6))
plt.bar(generi_più_popolari.index, generi_più_popolari.values)
plt.xticks(rotation=45)
plt.title("Generi più popolari nei videogiochi")
plt.xlabel("Genere")
plt.ylabel("Numero di giochi")
plt.show()

# Creo un plot per mostrare il numero di giochi usciti per ogni anno
giochi_per_anno = df['Year'].value_counts().sort_index()
plt.figure(figsize=(8,6))
plt.plot(giochi_per_anno.index, giochi_per_anno.values, marker="o")
plt.title("Evoluzione del numero di giochi pubblicati nel tempo")
plt.xlabel("Anno")
plt.ylabel("Numero di giochi")
plt.grid(True)
plt.show()

# Versione ricreata da me del bar plot mostrato nel file degli esercizi
generi_scelti = ["Action", "Misc", "Role-Playing", "Shooter", "Sports"]
df_filtrato = df[df["Genre"].isin(generi_scelti)]
vendite_genere = df_filtrato.groupby("Genre")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum()
vendite_genere.plot(kind="bar", stacked=True, figsize=(8,6))
plt.title("Vendite per regione per genere")
plt.xlabel("Genere")
plt.ylabel("Milioni di unità")
plt.legend(title="Regione")
plt.show()