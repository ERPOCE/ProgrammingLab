# Importo le librerie necessarie
import numpy as np 
import matplotlib.pyplot as plt

# Creo le variabili con le percentuali di uscita e una con il numero di lanci da effetturare
rosso = 3/5
blu = 2/5
numero_lanci = 100

# Creo una funzione che restituisce un vettore contenente solamente 0 e 1 per indicare il risultato di ogni estrazione
def estrazione(N):
    lanci = np.random.choice([1, 0], size=N, p=[rosso, blu])
    return lanci

# Effettuo le 100 estrazioni e calcolo la proporzione cumulativa delle estrazioni rosse
lanci = estrazione(numero_lanci)
proporzione = [lanci[:x].mean() for x in range(10, numero_lanci + 1, 10)]

# Creo il grafico dell'andamento della proporzione cumulativa in funzione del numero di estrazioni
# Ad altezza 0,6 ho inserito una linea che rappresenta la percentuale teorica delle estrazioni rosse
x = np.arange(10, numero_lanci + 1, 10)
plt.figure(figsize=(12,6))
plt.plot(x, proporzione, marker="o", linestyle="-", label="Percentuali delle estrazioni")
plt.axhline(rosso, linestyle="--", color="red", label="Retta della percentuale teorica")
plt.xlabel("Numero di estrazioni")
plt.ylabel("Proporzione delle palline rosse")
plt.title("Andamento della proporzione cumulativa in funzione del numero di estrazioni")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()