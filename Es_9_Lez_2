# Importo il modulo random
import random as rm

# Creo una lista contenente tutte le parole da inserire a random nella frase
lista_parole = [
    'INSEDIAMENTO', 'SEPARAZIONE', 'DIFFERENZA', 'APPLICAZIONE', 'ATTEGGIAMENTO', 'VERDURA', 'IMPERO', 'RICEVIMENTO',
    'IGNORANZA', 'BIOGRAFIA', 'VISIONE', 'AGENTE DI POLIZIA', 'PROVA', 'PRESTAZIONE', 'PRESENTAZIONE', 'PARENTE',
    'GIUSTIFICAZIONE', 'FILOSOFIA', 'DIREZIONE', 'BENEFICIARIO', 'BATTERIA', 'CERIMONIA', 'AGONIA', 'RECUPERO',
    'ALFABETIZZAZIONE', 'CONSEGNA', 'SERBATOIO', 'VOLONTARIO', 'DEPOSITO', 'BIRILLO DA BOWLING', 'NEMICO', 'ANNUNCIO',
    'CARAMELLA ZUCCHERATA', 'FULMINE', 'PALLONCINO', 'COPERTA', 'SCOPERTA', 'PENALITÀ', 'GENERALE', 'ALPACA',
    'VANTAGGIO', 'HOT DOG', 'ABITO', 'MATEMATICA', 'VARIANTE'
]

# Estraggo 5 parole dalla lista, .choices permette il reinserimento
parole_casuali = rm.choices(lista_parole, k = 5)

# Frase da completare con le parole randomiche
frase = (
    "In epoche passate, viveva una donna saggia che era molto orgogliosa dell'antico __ che proteggeva. "
    "Quando un anziano del villaggio venne a chiederle consiglio su come garantire al meglio un raccolto abbondante "
    "e le offrì il __ come dono, i suoi occhi si spalancarono e lei esclamò una sola parola, \"__\".\n"
    "Radunò il villaggio e, per i successivi 100 giorni, su sua richiesta, gli abitanti cercarono nella foresta un __. "
    "Nel 101° giorno, il bambino più giovane del villaggio trovò ciò che stavano cercando e tutti corsero dalla donna saggia per donarglielo. "
    "Con un sorriso da un orecchio all’altro, e cantando canti di festa, la donna saggia guardò i suoi compaesani e disse: "
    "\"Ora è giunto il tempo del banchetto - nessuno rimarrà mai più senza _!\" Ci fu grande gioia e celebrazione."
)

# Ciclo per sostituire un __ alla volta per iterazione, cosicché non vengano sovrascritte le parole inserite
frase_finale = frase
for parola in parole_casuali:
    frase_finale = frase_finale.replace("__", parola, 1)

# Stampo la frase finale completa
print(frase_finale)