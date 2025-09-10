# Importo le librerie necessarie
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# Ricopio il dataset
csv_path = "imdb_top_1000.csv"
df = pd.read_csv(csv_path)

# Mostro quanti valori mancano per colonna
print("\nValori mancanti per colonna:\n", df.isnull().sum())
# Cancello i valori NaN e anche la colonna "Overview"
df = df.dropna()
df = df.drop(columns="Overview")

# Creo una colonna "main_genre" ricavando il primo genere citato nella colonna "Genre" dopo che li ho separati tramite ","
df["main_genre"] = df["Genre"].str.split(",").str[0].str.strip()

# Conto quante volte compaioni i generi nella colonna "main_genre" e stampo i 5 generi più frequenti
top_5_generi = df["main_genre"].value_counts().head(5)
print("\nI 5 generi più frequenti:\n", top_5_generi)

# Pulisco le varie colonne "Star" da spazi involontari, ecc
for attore in ["Star1", "Star2", "Star3", "Star4"]:
    df[attore] = df[attore].astype(str).str.strip()

# Conto quante volte compaiono i vari nomi degli attori e restituisco quello più frequente
star_1_frequente = df["Star1"].value_counts().idxmax()
print("\nL'attore che compare di più in Star1 è: ", star_1_frequente)

# Metto in una lista che poi scorro le nomenclature delle colonne
lista_colonne = ["Star1", "Star2", "Star3", "Star4"]
# Unisco le colonne in un'unica colonna, rinumerando l'indice
attori_ogni_film = pd.concat([df[colonna] for colonna in lista_colonne], ignore_index=True)
# Conto ogni nome di attori nella colonna e restituisco quello più frequente
star_con_piu_film = attori_ogni_film.value_counts().idxmax()
print("\nL'attore che compare in più film è: ", star_con_piu_film)

# Raggruppo tutto il dataframe tramite "main_genre", che grazie a "as_index=False" rimanga come colonna e non come indice
# .agg() mi permette di calcolare la media di ogni gruppo all'interno. Creo 2 colonne chiamate IMDB_media e Gross_Media che contengono le medie delle colonne iniziali per ogni genere
# Ordino in maniera decrescente le righe in base alla colonna IMDB_media
raggruppo = (df.groupby("main_genre", as_index=False).agg(IMDB_media=("IMDB_Rating", "mean"), Gross_media=("Gross", "mean")).sort_values("IMDB_media", ascending=False))

# Stampo a schermo le prime 10 righe con i valori medi, arrotondati a 3 decimali
print("\nLe prime 10 righe col IMDB_rating medio e Gross medio per genere:\n")
print(raggruppo.head(10).round(3))

# Creo lo scatterplot con la media IMDB sull'asse x e con la media Gross sull'asse y
plt.figure()
plt.scatter(raggruppo["IMDB_media"], raggruppo["Gross_media"])

# Aggiungo le etichette ai punti, spostandole di 0,01 affinché non si sovrappongano
for _, row in raggruppo.iterrows():
    plt.text(row["IMDB_media"] + 0.01, row["Gross_media"], row["main_genre"], fontsize=8)
plt.xlabel("IMDB_Rating medio")
plt.ylabel("Gross medio")
plt.title("Grafico delle medie IMDB e Gross per main:genre")
# Comando per far gestire gli spazi cosicché non ci siano problemi grafici
plt.tight_layout()
plt.show()

# Estraggo come lista i nomi dei 5 generi più frequenti, che avevo calcolato all'inizio
nomi_top_5 = top_5_generi.index.tolist()
# Creo una copia di ogni film appartenente ai 5 generi, così ho un nuovo df contenente solo i generi interessati
df_top_5 = df[df["main_genre"].isin(nomi_top_5)].copy()

# Creo un plot a violino per mostrare la distribuzione di IMDB_Rating
plt.figure()
# Creo un vettore per ognuno dei 5 generi contenente ogni IMDB_Rating dei film di quei generi
dati_imdb = [df_top_5[df_top_5["main_genre"] == genere]["IMDB_Rating"].values for genere in nomi_top_5]
# "showmeans=True" traccia la media, "howextrema=True" mostra i valori minimi e massimi
plt.violinplot(dati_imdb, showmeans=True, showextrema=True)
# Metto i nomi dei generi sotto i violini
plt.xticks(range(1, len(nomi_top_5) + 1), nomi_top_5)
plt.ylabel("IMDB_Rating")
plt.title("Distribuzione IMDB_Rating per i 5 main_genre più grandi")
plt.grid(True)
# Uso di nuovo questo comando per evitare problemi con la spaziatura
plt.tight_layout()
plt.show()

# Faccio la stessa identica cosa ma questa volta il grafico riguarda i dati di Gross
plt.figure()
dati_gross = [df_top_5[df_top_5["main_genre"] == genere]["Gross"].values for genere in nomi_top_5]
plt.violinplot(dati_gross, showmeans=True, showextrema=True)
plt.xticks(range(1, len(nomi_top_5) + 1), nomi_top_5)
plt.ylabel("Gross")
plt.title("Distribuzione Gross per i 5 main_genre più grandi")
plt.grid(True)
plt.tight_layout()
plt.show()