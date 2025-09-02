# Importo le librerie necessarie
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Ricopio il dataset
df = pd.read_csv('https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv')

# Seleziono le colonne interessate con i valori della cilindrata e del consumo
# X è la variabile indipendente (cilindrata) mentre y quella dipendente (consumo)
# NOTA BENE: devo mettere 2 [[]] per X dato che a sklearn serve un dataframe di 2 dimensioni per calcolare il modello di regressione lineare
# Perciò usando [[]] assegno ad ogni valore di X un ulteriore valore pari a 1, ad indicare che ci sono X campioni con 1 feature
X = df[['disp']]
y = df['mpg']

# Creo il modello di regressione lineare tramite sklearn e poi inserisco le variabili nell'argomento
modello = LinearRegression()
modello.fit(X, y)

# Stampo il coefficiente angolare e intercetta della retta. NOTA BENE: .4f serve a formattare il numero con 5 cifre decimali
print(f"Coefficiente angolare: {modello.coef_[0]:.5f}")
print(f"Intercetta: {modello.intercept_:.5f}")

# Creo le previsioni sui valori di x
y_prevista = modello.predict(X)

# Visualizzazione del modello
plt.scatter(X, y, color='blue', label='Dati reali')
plt.plot(X, y_prevista, color='red', label='Linea di regressione')
plt.xlabel('Cilindrata')
plt.ylabel('Consumo')
plt.title('Regressione Lineare')
plt.legend()
plt.show()