# Importo la libreria numpy
import numpy as np 

# Creo il vettore con i dati fornitomi, aggiungo il formato float per poter lavorare
canoni = np.array([720, 980, 650, 1200], dtype=float)

# Sommo i vari costi prima delle modifiche
spesa_tot_iniziale = np.sum(canoni)

# Calcolo la percentuale di quanto influisce sulla somma complessiva l'affitto più alto
percentuale_prima = np.round(canoni[3:] / spesa_tot_iniziale * 100, 3)

# Eseguo le moodifiche da apportare ai vari affitti
canoni[3:] *= 1.12

canoni[2:3] *= 0.9

canoni[:2] *= 1.05

# Sommo i vari costi ora modificati
spesa_tot_finale = np.sum(canoni)

# Calcolo la percentuale dell'influenza sui costi dell'affitto più alto
percentuale_dopo = np.round(canoni[3:] / spesa_tot_finale * 100, 3)

# Calcolo la differenza assoluta delle percentuali dell'affitto più alto
differenza_assoluta = percentuale_dopo - percentuale_prima

# Stampo a schermo tutti i dati richiesti
print("\nGli affitti dopo le modifiche: ", canoni)
print(f"\nLa spesa totale iniziale: {spesa_tot_iniziale} euro.")
print(f"\nLa spesa totale dopo ogni variazione: {spesa_tot_finale} euro.")
print(f"\nL'affitto più alto era il {percentuale_prima} %")
print(f"\nL'affitto più alto è il {percentuale_dopo} %")
print(f"\nErgo, l'influenza sul costo complessivo dell'affitto più alto è del {differenza_assoluta} %\n")