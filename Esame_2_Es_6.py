# Importo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

# Creo i valori seguendo le indicazioni dell'esercizio
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = -3.5 * x + 2 + np.random.normal(0, 10, 100)

# Definisco la funzione della retta
def retta(x, a, b):
    return a * x + b

# Stimo i parametri della retta e trovo la matrice di covarianza
parametri, covarianza = curve_fit(retta, x, y)
a_stimata, b_stimata = parametri
print(f"\nI parametri stimati: a = {a_stimata}, b = {b_stimata}.\n")

# Calcolo l'errore standard di a e b
errore_std = np.sqrt(np.diag(covarianza))

# Calcolo l'intervallo di confidenza al 95% dei parametri a e b
intervallo_a = [a_stimata - (1.96 * errore_std[0]), a_stimata + (1.96 * errore_std[0])]
intervallo_b = [b_stimata - (1.96 * errore_std[1]), b_stimata + (1.96 * errore_std[1])]

# Per stampare a schermo, converto in float normali i valori calcolati per l'intervallo di confidenza
intervallo_a = [float(x) for x in intervallo_a]
intervallo_b = [float(x) for x in intervallo_b]
print("Ecco l'intervallo di confidenza al 95% di a:", intervallo_a)
print("\nEcco l'intervallo di confidenza al 95% di b:", intervallo_b)

# Genero 100 valori per x_stimata in modo che ci siano abbastanza dati 
x_stimata = np.linspace(0, 10, 100)
y_stimata = retta(x_stimata, a_stimata, b_stimata)

# Creo le 2 rette che fanno da limiti per l'intervallo di confidenza, una superiore ed una inferiore
limite_sopra = retta(x_stimata, intervallo_a[1], intervallo_b[1])
limite_sotto = retta(x_stimata, intervallo_a[0], intervallo_b[0])

# Inserisco nel grafico i punti orginali
plt.scatter(x, y, label="Dati")
# Creo la retta stimata
plt.plot(x_stimata, y_stimata, color='r', label="Retta stimata")
# Coloro l'area interna alle 2 rette limite che ho creato poco fa
plt.fill_between(x_stimata, limite_sotto, limite_sopra, color='r', alpha=0.3, label="Intervallo di confidenza al 95%")
plt.xlabel("Asse x")
plt.ylabel("Asse y")
plt.title("Retta stimata insieme al suo intervallo di confidenza")
plt.grid(True)
plt.legend()
plt.show()