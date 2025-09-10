# Importo le librerie necessarie
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# Ricopio il file CSV in un DataFrame per lavorare sui dati
df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv")

# Devo determinare i 10 paesi col consumo di alcol più alto
# Creo un nuovo DataFrame selezionando in ordine decrescente i paesi col consumo più alto
top_10 = df.sort_values("total_litres_of_pure_alcohol", ascending = False).head(10)
print("La lista dei 10 paesi col consumo di alcol più alto:\n")
print(top_10[["country", "total_litres_of_pure_alcohol"]])

# Devo calcolare la media del consumo di birra, vino e distillati
# Calcolo e stampo le medie aritmetiche delle singole colonne
media_birra = df["beer_servings"].mean()
media_vino = df["wine_servings"].mean()
media_distillati = df["spirit_servings"].mean()
print("\nMedia del consumo di birra: ", media_birra)
print("\nMedia del consumo di vino: ", media_vino)
print("\nMedia del consumo di distillati: ", media_distillati)

# Devo creare una nuova colonna alcohol_index
# Sommo tutti i valori delle 3 colonne per farne una media totale
df["alcohol_index"] = (df["beer_servings"] + df["wine_servings"] + df["spirit_servings"]) / 3

# Devo determinare il paese col valore massimo di alcohol_index
# Uso .loc per selezionare una riga dal DataFrame grazie all'indice della riga
# L'indice in questione lo trovo utilizzando .idxmax() che restituisce l'indice della riga di alcohol_index col valore massimo
paese_indice_max = df.loc[df["alcohol_index"].idxmax()]
print("\nIl paese con l'indice del consumo totale di alcol più alto: ")
print(paese_indice_max[["country", "alcohol_index"]])

# Uso un filtro booleano per determinare i paesi con più di 100 birre consumate
# Stampo i paesi filtrati con i loro consumi di birre
birre_100 = df[df["beer_servings"] > 100]
print("\nI paesi col consumo di birre superiore a 100: ")
print(birre_100[["country", "beer_servings"]])

# Devo creare un bar chart dei 10 paesi con più consumo totale di alcol
# Creo un grafico a barre dove sull'asse delle X ci sono i paesi e su quello delle Y i consumi per persona
# Ruoto i nomi dei paesi di 45° e metto i titoli per gli assi solo per chiarezza nella lettura
plt.bar(top_10["country"], top_10["total_litres_of_pure_alcohol"], color=["blue", "green"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 paesi per consumo totale di alcol in litri")
plt.ylabel("Litri di alcol per persona")
plt.xlabel("Paese")
plt.show()

# Devo creare un line plot con i consumi di vino di ogni paese
# Creo una copia ordinata dei paesi del DataFrame in base ai consumi di vino in ordine crescente
# Aggiungo le etichette per chiarezza nella lettura
wine_sorted = df.sort_values("wine_servings")
plt.plot(wine_sorted["country"], wine_sorted["wine_servings"], color="red")
plt.xticks(rotation=90)
plt.title("Consumo di vino per paese")
plt.ylabel("Wine servings")
plt.xlabel("Paese")
plt.show()