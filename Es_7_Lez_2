import numpy as np

survey_matrix = np.array([ [25, 40000, 10], [32, 52000, 12], [40, 63000, 14], [29, 47000, 11], [35, 58000, 13] ])

intervistati_oltre_12 = survey_matrix[survey_matrix[:, 2] >= 12]

redditi_filtrati = survey_matrix[survey_matrix[:, 2] >= 12, 1]

media = survey_matrix[survey_matrix[:, 2] >= 12, 1].mean()

print("\nIntervistati con almeno 12 anni di istruzione:\n", intervistati_oltre_12)
print("\nI redditi filtrati in base alla prima selezione: ", redditi_filtrati)
print("\nLa media dei redditi: ", media)