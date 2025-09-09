# Importo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

# Incollo il dataset di coppie fornitomi
x = np.array([
  0.0, 0.3448, 0.6897, 1.0345, 1.3793, 1.7241,
  2.0690, 2.4138, 2.7586, 3.1034, 3.4483, 3.7931,
  4.1379, 4.4828, 4.8276, 5.1724, 5.5172, 5.8621,
  6.2069, 6.5517, 6.8966, 7.2414, 7.5862, 7.9310,
  8.2759, 8.6207, 8.9655, 9.3103, 9.6552, 10.0
])

y = np.array([
   3.99,  3.33,  8.71,  9.83, 10.69, 14.59,
  11.72, 14.87, 16.06, 13.93, 19.61, 19.83,
  18.40, 20.59, 21.45, 26.51, 24.57, 24.94,
  25.55, 27.78, 28.71, 30.87, 34.14, 34.65,
  35.01, 37.94, 38.53, 41.56, 42.28, 42.65
])

# Creo la funzione retta
def retta(x, a, b):
    return a * x + b

# Uso "curve_fit" per stimare i parametri e li assegno a 2 variabili
parametri_stimati, _ = curve_fit(retta, x, y)
a_stimata, b_stimata = parametri_stimati

# Stimo i valori di y usando la funzione "retta" con i parametri stimati
y_stimata = retta(x, a_stimata, b_stimata)

# Calcolo la mae
mae = np.mean(np.abs(y - y_stimata))

# Calcolo la rmse
rmse = math.sqrt(np.mean((y - y_stimata) ** 2))

# Stampo sia i parametri che la mae e la rmse a schermo
print(f"\nI parametri stimati: a = {a_stimata:.4f}, b = {b_stimata:.4f}")
print(f"\nLa MAE: {mae:.4f}, la RMSE: {rmse:.4f}")

# Plot con i punti originali e la retta stimata
plt.figure(figsize=(12,6))
plt.scatter(x, y, color="blue", label="Dati registrati")
plt.plot(x, y_stimata, linestyle="-", color="red", label="Retta stimata")
plt.xlabel("Asse x")
plt.ylabel("Asse y")
plt.title("Grafico dei punti osservati e della retta stimata")
plt.grid(True)
plt.legend()
plt.tight_layout
plt.show()