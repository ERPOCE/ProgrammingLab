# Importo la libreria numpy
import numpy as np 

# Creo una matrice 7x7 con media = 0 e std = 5. Uso .seed per avere sempre gli stessi valori
np.random.seed(0)
matrice = np.random.normal(loc=0, scale=5, size=(7, 7))

# Prendo l'indice del valore più lontano da 0 per ogni riga della matrice usando il valore assoluto
indice_massimi_assoluti = np.abs(matrice).argmax(axis=1)

# Ricopio i numeri di riga della matrice in un vettore
righe = np.arange(matrice.shape[0])

# Creo un vettore il quale prende come valori i numeri che corrispondo ad un determinato indice per riga
# Così facendo, questo vettore possiede i numeri originali senza alterazioni di segno per via del valore assoluto
valori_massimi = matrice[righe, indice_massimi_assoluti]

# Conto il numero di righe contenenti dei valori positivi sommando i numeri maggiori di 0 nel vettore
conta_righe_positive = np.sum(valori_massimi > 0)

# Stampo a schermo la matrice originale, i valori più distanti da 0 e il numero di righe contenenti un valore positivo
print("\nLa matrice originale:\n", matrice)
print("\nI valori più distanti da 0 per ogni riga:\n", valori_massimi)
print("\nNumero di righe col valore più lontano da 0 positivo: ", conta_righe_positive)