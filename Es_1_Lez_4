# Importo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt


# Funzione per il lancio della moneta (numero int) e ritorna un float
def frequenza_testa(N: int) -> float:

    # Creo un vettore di lunghezza N contenente solo 0 (croce) e 1 (testa) a random
    lanci = np.random.randint(0, 2, N)

    # Ritorno in percentuale la media del vettore (quindi solo teste poiché croce = 0)
    return (np.sum(lanci) / N) * 100


# Creo un array con 100 interi distribuiti uniformemente tra 10 e 20000
campioni = np.linspace(10, 20000, 100, dtype=int)

# Calcolo la frequenza percentuale di testa per ogni N del vettore
frequenze = [frequenza_testa(N) for N in campioni]

# Creo il plot del numero medio di teste rispetto ai campioni. I valori sono i punti collegati dalla linea
plt.plot(campioni, frequenze, marker="o", linestyle="-")

# Aggiungo una linea a quota 50 per rappresentare il valore atteso in percentuale (testa il 50% delle volte)
plt.axhline(50, color="red", linestyle="--", label="Valore atteso (50%)")

# Aggiungo il titolo e le etichette
plt.title("Frequenza % di Testa al variare del numero di lanci")
plt.xlabel("Numero di lanci")
plt.ylabel("Frequenza % di Testa")

# Aggiungo sia la legenda che una griglia per la lettura dei valori
plt.legend()
plt.grid(True)
plt.show()