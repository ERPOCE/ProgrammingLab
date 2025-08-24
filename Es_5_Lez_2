# Importo il modulo numpy
import numpy as np 

# Creo il vettore con i valori float degli stipendi
stipendi = np.array([50000, 105250, 55000, 89000], dtype = float)

# Sommo tutti i valori del vettore
costo_totale_iniziale = stipendi.sum()
print("\nIl costo totale degli stipendi all'inizio: ", costo_totale_iniziale)

# Applico un aumento del 15% allo stipendio del CEO
stipendi[1] = stipendi[1] * 1.15
print("\nStipendi dopo l'aumento al CEO:\n", stipendi)

# Applico un aumento del 20% allo stipendio più basso
stipendi[0] = stipendi[0] * 1.2
print("\nStipendi dopo l'aumento al salario minore:\n", stipendi)

# Applico un aumento del 10% ai 2 stipendi rimasti
stipendi[2:] *= 1.10
print("\nStipendi dopo l'aumento ai 2 salari rimasti invariati:\n", stipendi)

# Calcolo la somma dei valori dopo le modifiche apportate
costo_totale_finale = stipendi.sum()
print("\nIl costo totale degli stipendi alla fine: ", costo_totale_finale)