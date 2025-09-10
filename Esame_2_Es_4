# Importo le librerie necessarie
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# Ricopio il dataset separando le colonne usando il ";" anziché la "," classica
csv_path = "cereal.csv"
df = pd.read_csv(csv_path, sep=";")

# Creo una nuova colonna calcolando la somma delle proteine e delle fibre per poi dividerla per le calorie
df["nutri_score"] = (df["protein"] + df["fiber"]) / df["calories"]

# Trovo i 5 cereali con il nutriscore più alto e li stampo insieme al nome
top_5_nutriscore = df.nlargest(5, "nutri_score")
print("\nI 5 cereali col nutriscore più alto:\n", top_5_nutriscore[["name", "nutri_score"]])

# Filtro i cereali con meno di 120 calorie e con più di 2 g di fibre, poi le stampo a schermo
cereali_filtrati = df[(df["calories"] < 120) & (df["fiber"] > 2)]
print("\nEcco i cereali con meno di 120 calorie e più di 2 grammi di fibre:\n", cereali_filtrati)

# Grafico a barre dei 10 cereali col nutri_score più elevato. I nomi dei cereali sono sull'asse x
# I valori del nutri_score sull'asse y
top_10_nutriscore = df.nlargest(10, "nutri_score")
plt.figure(figsize=(12,6))
plt.bar(top_10_nutriscore["name"], top_10_nutriscore["nutri_score"])
plt.xlabel("Nomi dei cereali")
plt.ylabel("Valore del nutri_score")
plt.title("I 10 cereali con più nutrienti positivi per caloria")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.grid(True)
plt.show()

# Scatterplot dove l'asse delle x corrisponde alle calorie, l'asse y al nutri_score mentre il colore dei punti alle proteine
plt.figure(figsize=(12,6))
plt.scatter(df["calories"], df["nutri_score"], c=df["protein"], alpha=0.8)
plt.xlabel("Calorie")
plt.ylabel("Valore del nutri_score")
plt.title("Scatter plot delle proteine tra calorie e nutri_score")
plt.grid(True)
plt.colorbar(label="Proteine")
plt.show()