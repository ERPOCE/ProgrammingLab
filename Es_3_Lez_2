# Importo il modulo numpy
import numpy as np 

# Creo una matrice 2D con 10 righe e 3 colonne
# I valori sono generati randomicamente tra 0 e 1
matrice = np.random.rand(10, 3)
print("Matrice iniziale:\n", matrice)

# Sottraggo ad ogni valore 0.5 e calcolo il valore assoluto
# I valori più bassi rappresentano i numeri più vicini a 0.5
numeri_selezionati = np.abs(matrice - 0.5).argmin(axis = 1)

# Creo un array 1D con tutti i valori selezionati prima
risultato = matrice[np.arange(matrice.shape[0]), numeri_selezionati]
print("\nI valori più vicini a 0.5 per riga:\n", risultato)