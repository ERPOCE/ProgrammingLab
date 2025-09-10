# Importo le librerie necessarie
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ricopio il dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Controllo il numero di righe e colonne del dataset
print("Numero di righe e colonne: ", df.shape)

# Controllo e conto i valori mancanti delle colonne
print("\nValori mancanti per colonna: ")
print(df.isnull().sum())

# Sostituisco ogni valore mancante nella colonna 'Embarked' con il valore più frequente
rimpiazzo_embarked = df['Embarked'].mode()[0]
df['Embarked'].fillna(rimpiazzo_embarked, inplace=True)

# Rimuovo ogni riga dove non è presente il valore 'Age' 
df = df.dropna(subset=['Age'])

# Controllo la presenza di righe duplicate
print("\nNumero di righe duplicate: ", df.duplicated().sum())

# Calcolo l'età media dei passeggeri per ogni classe
media_eta = df.groupby('Pclass')['Age'].mean()
print("\nEtà media per classe:\n", media_eta)

# In caso non ci fossero i valori dell'età, inserisco il valore medio
df['Age'] = df.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.mean()))

# Plot della distribuzione dell'età per classe
sns.histplot(
    data=df,
    x="Age",
    hue="Pclass",
    kde=True,
    element="step"
    )

plt.title("Distribuzione dell'età per classe")
plt.show()

# Plot della distribuzione dell'età per classe, mostrando i dati sia per uomini che donne
sns.displot(
    data=df,
    x="Age",
    hue="Sex",
    col="Pclass",
    bins=20,
    kde=True,
    element="step"
)

plt.subplots_adjust(top=0.8)
plt.suptitle("Distribuzione dell'età per classe e sesso", fontsize=14)
plt.show()