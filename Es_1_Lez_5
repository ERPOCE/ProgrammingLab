# Importo le librerie necessarie
import numpy as np 
import pandas as pd

# Creo il dataframe
sales = pd.DataFrame(
    data={
        "employee": [
            "Katrina",
            "Guanyu",
            "Jan",
            "Roman",
            "Jacqueline",
            "Paola",
            "Esperanza",
            "Alaina",
            "Egweyn",
        ],
        "sales": [14, 17, 6, 12, 8, 3, 7, 15, 5],
        "year": [2018, 2019, 2020, 2018, 2020, 2019, 2019, 2020, 2020],
    }
)

# Non mi dilungherò sul riportare le indicazioni da svolgere, mostrerò a schermo le richieste con i print
# Avrei anche potuto creare delle funzioni e usare .apply(), ma le richieste erano troppo semplici per necessitare tale metodo

print("\nLe vendite superiori a 10:\n", sales.query("sales > 10"))

print("\nI dati registrati nel 2018:\n", sales.query("year == 2018"))

print("\nLe vendite superiori a 13 nel 2018:\n", sales.query("sales > 13 and year == 2018"))

print("\nTutti i dati tranne quelli relativi alle vendite maggiori di 13 nel 2018:")
print(sales.query("not (sales > 13 and year == 2018)"))

print("\nI dati le cui vendite divise per 3 sono maggiori di 3:\n", sales.query("sales / 3 > 3"))

# Unico commento che ritengo necessario: usando la formula ... > "J", mostravo a schermo anche i nomi che iniziano con "J"
# A quanto pare, risultano "maggiori di J". Per evitare il problema, ho messo ... > "K", così mostra a schermo tutti i nomi corretti
print("\nI dipendenti i cui nomi iniziano dopo la 'J':\n",sales.query("employee > 'K'"))