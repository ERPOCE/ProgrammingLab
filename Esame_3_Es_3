# Importo la libreria numpy
import numpy as np 

# Creo una matrice con valori casuali tra -20 e 20 inclusi. Uso ".seed" per avere sempre gli stessi valori
np.random.seed(0)
matrice = np.random.randint(-20, 21, size=(8, 8))
print("\nLa matrice generata:\n", matrice)

# Seleziono i valori più vicini a 10 per ogni riga in un array
# Per estrarre dalla matrice mi baso sula formula "matrice[righe, colonne]"
# Per le righe, uso "np.arange(matrice.shape[0])" che mi restituisce la conta da 0 fino al numero massimo escluso 
# Tale numero è il totale delle righe della matrice. Potevo inserire 8 e basta ma così la formula è più generale
# Per le colonne, uso "np.abs(matrice - 10)" che sottrae 10 ad ogni numero della riga per poi farne il valore assoluto
# Dopo aver reso positivi i risultati della sottrazione, uso ".argmin(axis=1)" per trovare la colonna della riga in questione con la distanza minima
valori_selezionati = matrice[np.arange(matrice.shape[0]), np.abs(matrice - 10).argmin(axis=1)]
print("\nI valori più vicini a 10 per ogni riga:\n", valori_selezionati)