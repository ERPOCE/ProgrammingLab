# Importo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Creo gli array coi valori
temp_max = np.array([17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18])
temp_min = np.array([-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58])
months = np.arange(12)

# Funzione sinusoidale per modellare la stagionalità
def sinusoidale(x, A, B, C, D):
    return A * np.sin(B * (x + C)) + D

# Fit per le temperature massime
# Curve_fit restituisce 2 valori e ci interessa solo il primo, perciò metto , _ per indicare che ignoro il secondo valore restituito
parametri_max, _ = curve_fit(sinusoidale, months, temp_max, p0=[(temp_max.max() - temp_max.min()) / 2, 2*np.pi/12, 0, temp_max.mean()])
# L'asterisco serve per scrivere una versione più corta di un intero array in un argomento di funzioni: scrivere *parametri_max
# Equivale a scrivere fit_max = sinusoidale(months, parametri_max[0], parametri_max[1], parametri_max[2], parametri_max[3])
fit_max = sinusoidale(months, *parametri_max)

# Fit per le temperature minime
parametri_min, _ = curve_fit(sinusoidale, months, temp_min, p0=[(temp_min.max() - temp_min.min()) / 2, 2*np.pi/12, 0, temp_min.mean()])
fit_min = sinusoidale(months, *parametri_min)

# Funzioni per calcolare MAE e RMSE
def mae(valori_veri, valori_fittati):
    return np.mean(np.abs(valori_veri - valori_fittati))

def rmse(valori_veri, valori_fittati):
    return np.sqrt(np.mean((valori_veri - valori_fittati) ** 2))

# Calcolo la MAE e la RMSE per i 2 vettori di valori
mae_max = mae(temp_max, fit_max)
rmse_max = rmse(temp_max, fit_max)

mae_min = mae(temp_min, fit_min)
rmse_min = rmse(temp_min, fit_min)

# Stampo a schermo la MAE e la RMSE delle temperature registrate
print("\nTemperature massime:")
print(f"MAE = {mae_max:.2f}, RMSE = {rmse_max:.2f}")

print("\nTemperature minime:")
print(f"MAE = {mae_min:.2f}, RMSE = {rmse_min:.2f}")

# Svolgendo l'esercizio, ho notato che le funzioni fittate erano spigolose
# Dopo aver osservato la correzione in classe, ho capito che dovevo inserire più punti tra i mesi
# Per esempio, 30 punti in un mese per rappresentare i giorni. Così facendo, la funzione diviene più sinuosa
# Perciò creo un vettore molto più denso di punti
mesi_densi = np.linspace(0, 11, 12*30)  # 360 punti totali

# Calcolo le curve lisce
fit_max_curva = sinusoidale(mesi_densi, *parametri_max)
fit_min_curva = sinusoidale(mesi_densi, *parametri_min)

# Plot con i fit dei dati
plt.figure(figsize=(8,6))
plt.plot(months, temp_max, "ro", label="Temperature massime")
plt.plot(mesi_densi, fit_max_curva, "r-", label="Fit temperature massime")
plt.plot(months, temp_min, "bo", label="Temperature minime")
plt.plot(mesi_densi, fit_min_curva, "b-", label="Fit temperature minime")
plt.xlabel("Mese")
plt.ylabel("Temperatura °C")
plt.legend()
plt.grid(True)
plt.show()