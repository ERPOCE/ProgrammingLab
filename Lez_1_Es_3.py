# Importo il modulo numpy
import numpy as np

# Creo un array di una dimensione
primo_arr = np.arange(1, 13)

# Creo un secondo array tramite slicing
secondo_arr = primo_arr[6:10]

# Creo un terzo array capovolgendo l'ordine del primo array
terzo_arr = primo_arr[::-1]

# Divido i valori del primo array con quelli del terzo
divisione = primo_arr / terzo_arr

print(f"\nIl primo array: {primo_arr}.\n")
print(f"Il secondo array: {secondo_arr}.\n")
print(f"Il terzo array: {terzo_arr}.\n")
print(f"Il risultato delle divisioni: {divisione}.\n")

# Creo le stesse cose, ma usando delle liste anziché gli array con numpy
prima_lista = list(range(1, 13))

seconda_lista = prima_lista[6:10]

terza_lista = prima_lista[::-1]

# Con le liste non posso usare lo stesso metodo consentito da numpy, quindi uso una list comprehension
seconda_divisione = [x / y for x, y in zip(prima_lista, terza_lista)]