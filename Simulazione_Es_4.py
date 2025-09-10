import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

df = df.dropna(subset=["Age", "Fare", "SibSp", "Parch", "Name"])

top_10_passeggeri = df.nlargest(10, "Fare")

print("\nI 10 passeggeri con la tariffa pagata più alta:\n", top_10_passeggeri[["Name", "Fare"]])

media_eta = df["Age"].mean()
media_tariffa = df["Fare"].mean()
media_sibsp = df["SibSp"].mean()

print("\nLa media dell'età: ", np.round(media_eta))
print("\nLa media della tariffa: ", np.round(media_tariffa, 3))
print("\nLa media della SibSp: ", np.round(media_sibsp, 3))

df["Family_index"] = np.where(df["Fare"] > 0, (df["SibSp"] +df["Parch"]) / df["Fare"], 0)

passeggero_fi_massimo = df.nlargest(1, "Family_index")

print("\nIl passeggero con l'indice massimo di Family_index:\n", passeggero_fi_massimo[["Name", "Family_index"]])

passeggeri_filtrati = df[df["Fare"] > 100]
print("\nI passeggeri con una tariffa superiore a 100:\n", passeggeri_filtrati[["Name", "Fare"]])

plt.bar(top_10_passeggeri["Name"], top_10_passeggeri["Fare"])
plt.xlabel("Nomi dei passeggeri")
plt.ylabel("Spesa per la tariffa")
plt.title("Grafico a barre dei 10 passeggeri con la tariffa più alta")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.grid(True)
plt.show()

ordine_per_tariffa = df.sort_values(by="Fare", ascending=True)
plt.figure(figsize=(12,6))
plt.plot(ordine_per_tariffa["Fare"], ordine_per_tariffa["Age"], linestyle="-", color="blue", label="Linea dell'età dei passeggeri")
plt.xlabel("Spesa per la tariffa")
plt.ylabel("Età dei passeggeri")
plt.title("Grafico a linee dell'età dei passeggeri in ordine crescente di tariffa")
plt.grid(True)
plt.tight_layout()
plt.show()