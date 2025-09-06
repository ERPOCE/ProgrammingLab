# Importo le librerie necessarie
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# Ricopio il dataframe
csv_path = "adult_con_titoli.csv"
df = pd.read_csv(csv_path)

# Stampo a schermo il numero di righe e colonne
print("Il numero di righe e colonne: ", df.shape)

# Stampo a schermo quanti valori mancano per colonna
print("Valori mancanti per colonna:\n", df.isnull().sum())

# Anche se non mancano valori, rimpiazzo i valori vuoti con le mode delle 3 colonne richieste dall'esercizio
rimpiazzo_workclass = df["workclass"].mode()[0]
df["workclass"].fillna(rimpiazzo_workclass, inplace=True)

rimpiazzo_occupation = df["occupation"].mode()[0]
df["occupation"].fillna(rimpiazzo_occupation, inplace=True)

rimpiazzo_nativecountry = df["native-country"].mode()[0]
df["native-country"].fillna(rimpiazzo_nativecountry, inplace=True)

# Normalizzo la colonna contenente il sesso delle persone
df["sex"] = df["sex"].astype(str).str.strip().str.lower()

# Normalizzo la colonna contenente il reddito delle persone
df["income"] = df["income"].astype(str).str.strip().str.upper()

# Calcolo e stampo a schermo l'età media dei maschi e delle femmine arrotondandole
eta_media_maschi = df.loc[df["sex"] == "male", "age"].mean()
eta_media_donne  = df.loc[df["sex"] == "female", "age"].mean()
print("L'età media arrotondata dei maschi: ", round(eta_media_maschi))
print("L'età media arrotondata delle donne: ", round(eta_media_donne))

# Calcolo la percentuale dei maschi e delle femmine con oltre 50K di reddito
percentuale_per_sesso = df.groupby("sex")["income"].apply(lambda x: (x == ">50K").mean() * 100)
print("\nLe percentuali dei sessi con oltre 50K di reddito:\n", percentuale_per_sesso)

# Creo una nuova colonna con 3 fasce d'età. NOTA BENE: creo prima le categorie (labels) e gli intervalli (bins)
# float("inf") per indicare infinito, "right=True" indica che viene incluso il limite destro
# "include_lowest=True" indica che nel primo intervallo viene incluso il limite sinistro
labels = ["<30", "30-50", ">50"]
bins = [0, 30, 50, float("inf")]
df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels, right=True, include_lowest=True)

# Calcolo la percentuale di persone nelle fasce d'età con ooltre 50K di reddito
percentuale_per_eta = df.groupby("age_group")["income"].apply(lambda x: (x == ">50K").mean() * 100)
print("\nPercentuale di reddito >50K per fascia di età:\n", percentuale_per_eta)

# Grafico a barre per mostrare le percentuali di persone nelle varie fasce d'età
percentuale_per_eta.plot(kind="bar", color="blue", grid=True)
plt.xlabel("Fascia d'età")
plt.ylabel("% dei redditi superiori a 50K")
plt.title("Percentuale di reddito superiore a 50K per fascia d'età")
plt.xticks(rotation=0)
plt.show()

# Boxplot per mostrare le ore settimanali di lavoro per gruppo di reddito
df.boxplot(column="hours-per-week", by="income", grid=True)
plt.title("Ore settimanali di lavoro per gruppo di reddito")
plt.xlabel("Reddito")
plt.ylabel("Ore alla settimana")
plt.suptitle("")
plt.show()