# Importo il modulo numpy
import numpy as np 

# Creo il vettore con tutte le letture delle frequenze cardiache
bpm = np.array([68, 65, 77, 110, 160, 161, 162, 161, 160, 161, 162, 163, 164, 163, 162, 100, 90, 97, 72, 60, 70])

# Trovo e stampo il valore minimo
minimo = bpm.min()
print("\nLa frequenza cardiaca minima: ", minimo)

# Trovo e stampo il valore massimo
massimo = bpm.max()
print("\nLa frequenza caridaca massima: ", massimo)

# Creo un vettore i cui valori sono True se la lettura è > 120, sennò è False
sopra_120 = bpm > 120
print("\nI valori True rappresenta la frequenza superiore a 120:\n", sopra_120)

# Calcolo la percentuale delle letture superiori a 120 
percentuale = sopra_120.mean() * 100
print(f"\nPercentuale di letture durante l'esercizio fisico: {percentuale} %\n")