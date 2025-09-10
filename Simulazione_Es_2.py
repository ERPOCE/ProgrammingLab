# Importo le librerie necessarie
import numpy as np 
import matplotlib.pyplot as plt

# Imposto il seed per avere sempre gli stessi dati generati
np.random.seed(0)

# Creo una funzione che restituisce 2 vettori con la media e la std delle posizioni degli N camminatori
def cammino_media_std(n: int, N: int):
   
   # Genero una matrice le cui righe sono i camminatori e le colonne sono i passi generati
    passi = np.random.choice([1, -1], size=(N, n))

    # Creo una matrice di uguali dimensioni in cui sommo per ogni riga i passi generati in modo tale da avere le posizioni. 
    # Per esempio: [+1, +1, -1, +1, +1, ...] diventa [1, 2, 1, 2, 3, ...]
    posizioni = np.cumsum(passi, axis=1)

    # Calcolo la media e la deviazione standard per ogni colonna, ovvero per ogni posizione in cui si trovano tutti i camminatori ad ogni passo
    media_per_passo = posizioni.mean(axis=0)
    std_per_passo   = posizioni.std(axis=0, ddof=0)
    
    # Ritorno i 2 array 1D contenenti le medie appena calcolate
    return media_per_passo, std_per_passo

# Assegno a 2 array i valori tramite la funzione creata
media_per_passo, std_per_passo = cammino_media_std(100, 50)

# Creo una lista di 100 valori che userò come asse x nei grafici per rappresentare i passi
x = np.arange(1, 101)

# Grafico della retta ottenuta con le medie delle posizioni di tutti i camminatori
plt.figure(figsize=(12,6))
plt.plot(x, media_per_passo, marker="o", linestyle="-", color="blue", label="Retta delle medie")
plt.xlabel("Passi percorsi")
plt.ylabel("Distanza percorsa dal punto iniziale 0")
plt.title("Grafico della media delle posizioni dei camminatori")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Grafico dell'andamento della deviazione standard. Ho inserito anche una curva che rappresenta la deviazione standard teorica
plt.figure()
plt.plot(x, std_per_passo, label="Deviazione standard osservata")
plt.plot(x, np.sqrt(x), linestyle="--", label="Valore teorico della deviazione standard")
plt.xlabel("Passi") 
plt.ylabel("Deviazione standard") 
plt.title("Grafico dell'andamento della deviazione standard")
plt.grid(True)
plt.legend() 
plt.tight_layout() 
plt.show()