# Importo la libreria numpy
import numpy as np 

# Creo l'array coi valori forniti dall'esercizio. I valori li inserisco come float per poter svolgere dei calcoli
spese_annuali = np.array([3200, 2750, 4100, 3600, 2950, 5100, 4400], dtype=float)

# Calcolo la somma di tutte le spese e le stampo a schermo
somma_iniziale = np.sum(spese_annuali)
print(f"La spesa totale complessiva: {somma_iniziale} euro")

# Stampo a schermo le spese annuali prima del calcolo della detrazione fiscale del 15%
print("Le spese annuali prima della detrazione fiscale:\n", spese_annuali)

# Applico una riduzione del 15% ai valori inferiori a 3000, poi stampo a schermo il vettore dopo tali modifiche
spese_annuali[spese_annuali < 3000] *= 0.85
print("Le spese annuali dopo la detrazione fiscale del 15%:\n", spese_annuali)

# Calcolo la somma dopo le riduzioni e ricavo quanto ha risparmiato l'intero gruppo con le detrazioni del 15%
somma_finale = np.sum(spese_annuali)
risparmio = somma_iniziale - somma_finale
print(f"Il gruppo dopo la detrazione ha risparmiato: {risparmio} euro")