# Importo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt

# Creo le variabili e associo le probabilità modificate a testa e croce
numero_lanci = 1000
testa = 1/3
croce = 2/3

# Estraggo 1000 lanci di moneta dove testa = 1 e croce = 0
lanci = np.random.choice([1, 0], size=numero_lanci, p=[testa, croce])

# Calcolo la proporzione cumulativa di testa rispetto a croce (devo sempre calcolare i valori vecchi insieme a quelli nuovi)
percentuali = [lanci[:x].mean() for x in range(50, numero_lanci + 1, 50)]

# Creo il grafico in cui sull'asse delle x ci saranno i salti di 50 valori e sull'asse delle y la proporzione di testa
# Inserisco a 0,33333 una linea tratteggiata per indicare la probabilità teorica che esca testa
x = np.arange(50, numero_lanci + 1, 50)
plt.plot(x, percentuali, marker="o", linestyle="-")
plt.axhline(testa, color="red", linestyle="--", label=f"Probabilità testa = {testa:.5f}")
plt.xlabel("Numero di lanci della moneta")
plt.ylabel("Proporzione di testa")
plt.title("Proporzione cumulativa di testa ogni 50 lanci")
plt.legend()
plt.grid(True)
plt.show()