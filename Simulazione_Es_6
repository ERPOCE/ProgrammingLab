import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

np.random.seed(0)

x = np.linspace(0, 10, 100)
y = 3 * x + 2 + np.random.normal(0, 1, 100)

def retta(x, a, b):
    return a * x + b

def fit_line(x, y):

    parametri, _ = curve_fit(retta, x, y)
    a_stimata, b_stimata = parametri

    formula_retta = f"y = {a_stimata:.2f} * x + {b_stimata:.2f}"

    return (a_stimata, b_stimata, formula_retta)

a, b, formula = fit_line(x, y)

y_stimata = retta(x, a, b)

plt.figure(figsize=(12,6))
plt.plot(x, y_stimata, color="blue", label=formula)
plt.xlabel("Asse x")
plt.ylabel("Asse y")
plt.title("Grafico della retta stimata")
plt.tight_layout()
plt.grid(True)
plt.legend()
plt.show()