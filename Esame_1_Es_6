# Importo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

# Genero i 2 array forniti per l'esercizio
x = np.linspace(0, 5, 80)
y = 2.5 * x + 1.2 + np.random.normal(0, 0.5, 80)

# Definisco una funzione per la retta che poi uso con curve_fit
def retta(x, a, b):
    return a * x + b

# Stimo i parametri della retta che meglio approssimano i dati e li inserisco in un array
parametri_stimati, _ = curve_fit(retta, x, y)

# Creo 2 variabili singole a cui associare i parametri stimati contenuti nell'array
a_stimata, b_stimata = parametri_stimati

# Calcolo la retta stimata usando la funzione "retta" in cui inserisco i valori ottimali
retta_stimata = retta(x, a_stimata, b_stimata)

# Calcolo sia la MAE che la RMSE 
mae = np.mean(np.abs(y - retta_stimata))
rmse = math.sqrt(np.mean((y - retta_stimata) ** 2))

# Stampo sia i parametri stimati che la MAE e la RMSE arrotondando a 3 decimali
print(f"\nI parametri stimati della retta: a = {a_stimata:.3f}, b = {b_stimata:.3f}")
print(f"\nValore della MAE: {mae:.3f}")
print(f"\nValore della RMSE: {rmse:.3f}")

# Creo il plot in cui inserisco sia i dati osservati come punti nel grafico sia la retta stimata 
plt.figure()
plt.scatter(x, y, label="Dati osservati")
plt.plot(x, retta_stimata, color="red", label="Retta stimata")
plt.title("Plot della retta stimata e dei dati reali")
plt.xlabel("Asse x")
plt.ylabel("Asse y")
plt.legend()
plt.show()