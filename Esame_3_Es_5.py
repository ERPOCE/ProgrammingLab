# Importo le librerie necessarie
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# Ricopio il dataset
csv_path = "movies.csv"
df = pd.read_csv(csv_path)

# Stampo a shcermo il numero di righe e colonne
print("\nIl numero di righe e colonne del dataset:\n", df.shape)

# Rimuovo la colonna "overview"
df = df.drop(columns="overview")

# Ripulisco la colonna "director"
df["director"] = df["director"].astype(str).str.strip()

# Trovo e stampo a schermo il regista che ha diretto il maggior numero di film (ovvero quello che compare di più nella colonna)
regista_piu_film = df["director"].value_counts().idxmax()
print("\nIl regista che ha diretto il maggior numero di film: ", regista_piu_film)

# Raggruppo ogni regista (anche chi compare più volte) e faccio la media di tutti i "vote_average" ad essi associati
# Ripristino l'indice e ordino i registi in ordine decrescente per poi stampare a schermo i nomi e i voti dei 10 registi con la media più alta
vote_average_medio = df.groupby("director")["vote_average"].mean().reset_index().sort_values(by="vote_average", ascending=False)
print("\nI 10 registi con la media dei voti più alta:\n", vote_average_medio[["director", "vote_average"]].head(10))

# Filtro i nomi dei direttori che compaiono come "nan" (non capisco perché se lo utilizzavo prima non cambiava l'errore del grafico)
df = df[df["director"] != "nan"]

# Seleziono i nomi dei 5 registi con più film e creo un df i cui nomi dei registi sono gli indici
conteggio_film = df["director"].dropna().value_counts().head(5)
top_5_registi = conteggio_film.index

df_top_5 = df[df["director"].isin(top_5_registi)]

# Creo un boxplot dei vote_average dei 5 registi con più film
df_top_5.boxplot(column="vote_average", by="director", grid=False)
plt.xlabel("Registi")
plt.ylabel("vote_average")
plt.title("Distribuzione dei vote_average dei 5 registi con il maggior numero di film diretti")
plt.tight_layout()
plt.show()