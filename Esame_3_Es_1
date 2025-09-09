# Importo la libreria numpy
import numpy as np 

# Creo il vettore con le ore di sonno
sonno = np.array([6.5, 5.0, 7.8, 8.2, 4.9, 6.0, 7.0, 7.5, 6.8, 5.5, 8.0, 6.3, 7.2, 5.8])

# Creo un array composto solo da zeri della stessa lugnhezza di "sonno"
punteggio = np.zeros(sonno.size)

# Creo un ciclo dove inserisco dei punteggi in base alle condizioni dell'esercizio
# Non c'era scritto se il vettore dei punteggi dovesse averli in ordine di notte o meno, quindi ho preferito crearlo con la stessa sequenza
for x in range(0, sonno.size):
    if sonno[x] < 6:
        punteggio[x] = 1

    elif sonno[x] < 8:
        punteggio[x] = 2

    else:
        punteggio[x] = 3

# Calcolo quante volte compaiono i punteggi nel vettore "punteggio"
percentuale_1 = np.sum(punteggio == 1)
percentuale_2 = np.sum(punteggio == 2)
percentuale_3 = np.sum(punteggio == 3)

# Trasformo il numero dei punteggi in percentuali che poi stampo a schermo
percentuale_1 *= 100 / sonno.size
percentuale_2 *= 100 / sonno.size
percentuale_3 *= 100 / sonno.size

print("\nLe percentuali dei punteggi delle notti:\n")
print("Punteggio 1: ", percentuale_1)
print("\nPunteggio 2: ", percentuale_2)
print("\nPunteggio 3: ", percentuale_3)