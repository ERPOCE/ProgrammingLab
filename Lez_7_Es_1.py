# Importo le librerie necessarie
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import math

# Ricopio il DataFrame
csv_path = "data.csv"
df = pd.read_csv(csv_path)

# Converto la colonna "date" in oggetti datetime, ordinandoli in ordine cronologico e rimuovendo la colonna dell'indice
df["date"] = pd.to_datetime(df["date"], format="%Y-%m")
df = df.sort_values("date").reset_index(drop=True)

# Aggiungo una colonna chiamata "mese_numerico" contentente il numero di mesi trascorsi dall'inizio, servirà come asse x
origin = pd.Timestamp("1949-01-01")
df["mese_numerico"] = (df["date"].dt.year - origin.year) * 12 + (df["date"].dt.month - 1)

# Creo dei vettori numpy che contengono il numero di passeggeri (y) e i mesi (x)
x = df["mese_numerico"].to_numpy(dtype=float)
y = df["passengers"].to_numpy(dtype=float)

# Dopo qualche ora di tentativi, ho scoperto grazie a qualche ricerca come verificare che ci siano solamente valori validi
# "Controllo" è un array booleano che seleziona solamente i valori validi, cosè posso rimuovere i valori non finiti
Controllo = np.isfinite(x) & np.isfinite(y)
x = x[Controllo]
y = y[Controllo]

# Normalizzo i dati relativi ai mesi per evitare errori (che ho tristemente avuto)
x_media = x.mean()
x_std = x.std()
x_normalizzata = (x - x_media) / x_std

# Calcolo la regressione polinomiale di secondo grado
coefficienti = np.polyfit(x_normalizzata, y, deg=2)
y_predetta = np.polyval(coefficienti, x_normalizzata)

# Calcolo la RMSE
rmse = math.sqrt(np.mean((y - y_predetta) ** 2))

# Parte utile per rendere "curva" la funzione. Creo una lista di mesi interi dal minimo al massimo
x_grafico = np.arange(int(df["mese_numerico"].min()), int(df["mese_numerico"].max()) + 1)
# Normalizzo anche la x del grafico per poter usare lo stesso polinomio
x_grafico_normalizzata = (x_grafico - x_media) / x_std
# Trovo i valori stimati del polinomio
y_grafico = np.polyval(coefficienti, x_grafico_normalizzata)
# Converto i mesi numerici in date effettive da inserire nel grafico
date_grafico = [origin + pd.DateOffset(months=int(m)) for m in x_grafico]

# Creo il grafico usando Plotly, inizialmente è vuoto
grafico = go.Figure()

# Aggiungo le parti relative ai dati reali originali
grafico.add_trace(go.Scatter(x=df["date"], y=df["passengers"], mode="markers", name="Dati reali"))

# Aggiungo le parti relative alla curva del polinomio 
grafico.add_trace(go.Scatter(x=date_grafico, y=y_grafico, mode="lines", name="Regressione polinomiale di grado 2"))

# Aggiungo i titoli degli assi e dek grafico stesso
grafico.update_layout(title=f"Andamento regressione polinomiale di grado 2 (RMSE = {rmse:.3f})", xaxis_title="Data in mesi", yaxis_title="Passeggeri")

grafico.show()