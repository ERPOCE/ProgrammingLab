import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")

print("\nNumero di righe e colonne del dataset: ", df.shape)

print("\nValori mancanti per colonna:\n", df.isnull().sum())

sex_frequente = df["sex"].mode(dropna=True)[0]

print("\nColonna 'sex' prima delle modifiche:\n", df["sex"])

df["sex"] = df["sex"].fillna(sex_frequente)

print("\nColonna 'sex' dopo le modifiche:\n", df["sex"])

df = df.dropna(subset="body_mass_g")

print("\nNumero di righe duplicate: ", df.duplicated().sum())

massa_corporea_media = df.groupby("species")["body_mass_g"].mean()


df["body_mass_g"] = df["body_mass_g"].fillna(df.groupby("species")["body_mass_g"].transform("mean"))

massa_corporea_media = df.groupby("species")["body_mass_g"].mean()

df.boxplot(column="body_mass_g", by="species")
plt.xlabel("Le varie specie")
plt.ylabel("Valore della massa corporea")
plt.title("Grafico della distribuzione della massa corporea tra le specie")
plt.tight_layout()
plt.show()

sns.boxplot(data=df, x="species", y="body_mass_g", hue="sex")
plt.xlabel("Le varie pecie")
plt.ylabel("Valore della massa corporea")
plt.title("Grafico della distribuzione della massa corporea tra le specie e sessi")
plt.legend(title="Sesso")
plt.tight_layout()
plt.show()