# Importo le librerie necessarie
import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

# Carico e ricopio il dataset
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Pulisco i nomi delle colonne per evitare errori
df.columns = df.columns.str.strip().str.lower()

# COnverto la data
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

# Rimuovo le righe senza stipendio o paese
df = df.dropna(subset=['salary_year_avg', 'job_country'])

# Controllo e salvo i dati per ogni singolo paese
dati_paesi = df.groupby("job_country").agg(
    avg_salary=("salary_year_avg", "mean"),
    job_count=("job_title", "count"),
    min_salary=("salary_year_avg", "min"),
    max_salary=("salary_year_avg", "max")
).reset_index()

# Ordino i paesi in ordine decrescente in base al salario medio
paesi_ordinati = dati_paesi.sort_values(by="avg_salary", ascending=False)
print(paesi_ordinati)

# Calcolo lo stipendio medio per titolo di lavoro in modo da creare un grafico
avg_salary_job = df.groupby("job_title_short")["salary_year_avg"].mean().sort_values(ascending=False)

# Grafico a barre orizzontali (top 20 lavori più pagati)
avg_salary_job.head(20).plot(kind="barh", color="skyblue")
plt.title("Stipendio medio annuale per titolo di lavoro (top 20)")
plt.xlabel("Stipendio medio annuale")
plt.ylabel("Titolo di lavoro")
plt.gca().invert_yaxis()
plt.show()