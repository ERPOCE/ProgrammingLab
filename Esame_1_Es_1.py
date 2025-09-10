# Importo la libreria numpy
import numpy as np 

# Creo il vettore con tutti i prezzi
prezzi = np.array([14.99, 22.50, 9.75, 18.00, 31.20, 12.80, 24.90, 8.40, 19.99, 27.30])

# Calcolo il prezzo medio e lo stampo a schermo arrotondando i decimali
prezzo_medio = np.mean(prezzi)
print(f"\nLa media dei prezzi è la seguente: {prezzo_medio:.3f}")

# Creo un nuovo vettore in cui inserisco i prezzi superiori alla media e li riduco del 10%
prezzi_maggiori = prezzi[prezzi > prezzo_medio]
prezzi_maggiori *= 0.9
print("\nEcco i nuovi prezzi superiori alla media scontati del 10%:\n", prezzi_maggiori)