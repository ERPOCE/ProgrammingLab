# Importo il modulo numpy
import numpy as np

# Creo il vettore con i numeri primi fino a 20
primi = np.array([2, 3, 5, 7, 11, 13, 17, 19])

# Seleziono i numeri primi > 10 e li salvo in un altro vettore
maggiori = primi[primi > 10]
print(maggiori)

# Seleziono i numeri primi pari e li salvo in un altro vettore
pari = primi[primi % 2 == 0]
print(pari)