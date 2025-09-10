# Importo il modulo numpy
import numpy as np 

# Creo un array 2D contentente tutti i numeri da 10 fino a 50 escluso
a = np.arange(10, 50).reshape(4, 10)

# Creo un array contente la seconda e la quarta riga del primo array
b = a[[1, 3], :]

# Creo un array contenente solamente la terza riga del primo array
c = a[2, :]

# Stampo i vettori
print("Vettore A:\n", a)
print("Vettore B:\n", b)
print("Vettore C:\n", c)

# Faccio la divione per ogni colonna tra il primo e il terzo array
divisione = a / c
print("Risultato della divisione:\n", divisione)