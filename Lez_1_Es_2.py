# Importo il modulo numpy
import numpy as np

# Creo un array con i numeri primi fino a 10 e controllo la lunghezza usando 2 comdandi diversi
# Faccio notare che ho assegnato gli array alle variabili x, y e z solamente per avere dei print più semplici e leggibili, non era obbligatorio o necessario
num_primi = np.array([2, 3, 5, 7])
x = len(num_primi)
y = num_primi.size
print(f'\nValore determinato con len(): {x}, valore calcolato con .size: {y}.\n')

# Ritengo che la tipologia di dati del vettore sia int poiché non vi sono presenti numeri float o caratteri particolari, ecc...
print(f"La tipologia dei dati contenuti è la seguente: {num_primi.dtype}. \n")


# Versione con la list comprehension
primi_alternativi = np.array([k for k in range(2, 11) if k == 2 or (k % 2 != 0 and all(k % j != 0 for j in range(2, k)))])
z = primi_alternativi
print(f"Ecco l'array creato con la list comprehension: {z}.\n")