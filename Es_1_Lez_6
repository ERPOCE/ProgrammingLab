# Importo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# Genero 1000 valori casuali da una distribuzione gamma con parametro di forma pari a 1
# Solo per rendere più leggibile il codice, creo una variabile pari a 1 da usare quando serve il parametro di forma
shape = 1
data = gamma.rvs(shape, size=1000)

# Creo 200 punti tra 0 e il valore casuale massimo generato in 'data'
x = np.linspace(0, np.max(data), 200)
# Calcolo la PDF, ovvero la funzione densità di probabilità in ogni punto di 'x'
pdf = gamma.pdf(x, shape)

# Creo l'istogramma del campione con 1000 valori casuali e sovrappongo la PDF della distribuzione
plt.hist(data, bins=100, density=True, alpha=0.5, color='skyblue', label="Istogramma dei campioni")
plt.plot(x, pdf, 'r-', lw=2, label=f"PDF della distribuzione")
plt.title("Distribuzione Gamma con PDF")
plt.xlabel("Valore")
plt.ylabel("Densità")
plt.legend()
plt.show()

# Stimo il parametro di forma dal campione usando .fit()
shape_fittata, loc_fittata, scale_fittata = gamma.fit(data)
print("\nParametro di forma stimato: ", shape_fittata)
print("\nPosizione stimata: ", loc_fittata)
print("\nScala stimata: ", scale_fittata)

# Traccio la CDF, ovvero la funzione di distribuzione cumulativa
plt.figure()
# Calcolo la CDF. NOTA BENE: di default, loc=0 e scale=1 quindi non serve specificare
cdf = gamma.cdf(x, shape)
plt.plot(x, cdf, 'r-', lw=2, label="CDF")
plt.title("Funzione di distribuzione cumulativa (CDF)")
plt.xlabel("Valore")
plt.ylabel("Probabilità comulativa")
plt.legend()
plt.show()

# Calcolo la varianza, sia quella ricavata da operazioni sui dati sia quella teorica della distribuzione gamma
# Per la prima varianza, devo specificare ddof=1 poiché lavoro su un campione simulato di 1000 valori
varianza_dati = np.var(data, ddof=1)
varianza_teorica = gamma.var(shape)
print("\nVarianza campionaria: ", varianza_dati)
print("\nVarianza teorica: ", varianza_teorica)