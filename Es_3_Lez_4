# Importo le librerie necessarie
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ricopio il dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Conteggio dei campioni per ogni specie
print("Numero dei campioni per specie: ")
print(df['species'].value_counts(), "\n")

# Calcolo la lunghezza e larghezza media dei petali per ogni specie
print("Lunghezza e larghezza media dei petali per ogni specie: ")
print(df.groupby('species')[['petal_length', 'petal_width']].mean(), "\n")

# Scatterplot per le dimensioni dei petali per ogni specie
plt.figure(figsize=(8,6))
sns.scatterplot(
    data=df,
    x="petal_length",
    y="petal_width",
    hue="species",
    s=70
    )
plt.title("Dimensioni dei petali per specie")
plt.show()

# Creo una nuova colonna per l'area del petalo
df['petal_area'] = df['petal_length'] * df['petal_width']
print("Prime righe con la nuova colonna per l'area del petalo: ")
print(df.head(10), "\n")

# Analizzo l'area del petalo per ogni specie
print("Media dell'area del petalo per ogni specie: ")
print(df.groupby('species')['petal_area'].mean(), "\n")

# Boxplot per la distribuzione dell'area dei petali per ogni specie
plt.figure(figsize=(8,6))
sns.boxplot(
    data=df,
    x="species",
    y="petal_area"
    )
plt.title("Distribuzione dell'area del petalo per specie")
plt.show()