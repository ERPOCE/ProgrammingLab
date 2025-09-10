# Importo la libreria numpy
import numpy as np 

# Imposto il seed
np.random.seed(42)

# Creo l'array con i valori generati a random
a = np.random.normal(loc=0, scale=1, size=(5, 9))

# Creo un array 1D che estrae i valori dal vettore in base all'indice della colonna e della riga
array_valori_scelti = a[np.arange(a.shape[0]), np.abs(a - 0.1).argmin(axis=1)]

# Stampo entrambi i vettori
print("\nLa matrice generata:\n", a)
print("\nI valori più vicini a 0.1: ", array_valori_scelti)