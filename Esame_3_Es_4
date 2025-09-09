# Importo le librerie necessarie
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# Ricopio il dataset
csv_path = "movies.csv"
df = pd.read_csv(csv_path)

# Cancello le colonne con dati mancanti
df = df.dropna()

# Creo una colonna chiamata "roi" sottraendo il budget alla revenue e dividendo il risultato per il budget
df["roi"] = (df["revenue"] - df["budget"]) / df["budget"]

# Uso "df.nlargest" per trovare in ordine decrescente i 10 roi più alti dato che mi serve più avanti
# Uso "df[np.isfinite(df["roi"])]" per escludere i valori infiniti o NaN della colonna "roi" (non era richiesto correggere i valori 0 della colonna "budget" o altro)
# Stampo a schermo i primi 5 dei 10 film poiché sono quelli col valore più alto (ordine decrescente)
top_10_roi = df[np.isfinite(df["roi"])].nlargest(10 , "roi")
print("\nI 5 film con il ROI più alto:\n", top_10_roi[["original_title", "roi"]].head(5))

# Filtro in un DataFrame tutti i film che hanno un budget di oltre 50 milioni e un voto medio superiore a 7
film_filtrati = df[(df["budget"] > 50000000) & (df["vote_average"] > 7)]

# Creo un grafico a barre dei 10 film col roi più alto
plt.figure(figsize=(12,6))
plt.bar(top_10_roi["original_title"], top_10_roi["roi"])
plt.xlabel("Nomi dei film")
plt.ylabel("ROI (return on investment)")
plt.title("Grafico a barre dei 10 film col ROI più alto")
# Inclino i nomi dei film così non si sovrappongono
plt.xticks(rotation=45, ha="right")
plt.grid(True)
plt.tight_layout()
plt.show()

# Creo uno scatter plot del budget vs revenue i cui colori dei punti rappresentano il voto medio
plt.figure(figsize=(12,6))
# "c=df["vote_average"]" rappresenta i colori dei punti, alpha=0.7 ritengo che in questo caso sia la trasparenza ideale (non si capiva nulla prima)
plt.scatter(df["budget"], df["revenue"], c=df["vote_average"], alpha=0.7)
plt.xlabel("Asse con il budget")
plt.ylabel("Asse con la revenue")
plt.title("Scatter plot del budget e della revenue con i colori per i voti medi")
# Mostro la gradazione del colore in base al voto medio
plt.colorbar(label="Voto medio")
plt.tight_layout()
plt.show()