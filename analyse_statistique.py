#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Configuration pour les graphiques
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# 1. Génération de la population (10 000 individus)
np.random.seed(42)  # Pour la reproductibilité
# Génération d'une population avec distribution normale (moyenne=2000, écart-type=500)
population = np.random.normal(loc=2000, scale=500, size=10000)

# Paramètres réels de la population
vraie_moyenne = np.mean(population)
vrai_ecart_type = np.std(population)

print(f"Paramètres réels de la population:")
print(f"Moyenne: {vraie_moyenne:.2f}")
print(f"Écart-type: {vrai_ecart_type:.2f}")

# 2. Extraction d'un échantillon aléatoire (100 individus)
echantillon = np.random.choice(population, size=100, replace=False)

# 3. Calcul des statistiques de l'échantillon
moyenne_echantillon = np.mean(echantillon)
ecart_type_echantillon = np.std(echantillon, ddof=1)  # ddof=1 pour l'écart-type non biaisé

print(f"\nStatistiques de l'échantillon:")
print(f"Moyenne: {moyenne_echantillon:.2f}")
print(f"Écart-type: {ecart_type_echantillon:.2f}")

# 4. Calcul de l'intervalle de confiance à 95%
# On utilise la distribution t de Student car l'écart-type de la population est inconnu
n = len(echantillon)
degres_liberte = n - 1
alpha = 0.05
t_critique = stats.t.ppf(1 - alpha/2, degres_liberte)
marge_erreur = t_critique * (ecart_type_echantillon / np.sqrt(n))

intervalle_confiance = (moyenne_echantillon - marge_erreur, moyenne_echantillon + marge_erreur)

print(f"\nIntervalle de confiance à 95%:")
print(f"[{intervalle_confiance[0]:.2f} ; {intervalle_confiance[1]:.2f}]")

# 5. Test d'hypothèse (t-test)
# H0: la moyenne réelle est égale à 2000
# H1: la moyenne réelle est différente de 2000
valeur_test = 2000
t_stat, p_value = stats.ttest_1samp(echantillon, valeur_test)

print(f"\nTest d'hypothèse (t-test):")
print(f"Hypothèse nulle (H0): la moyenne réelle est égale à {valeur_test}")
print(f"Statistique t: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    conclusion = f"On rejette H0. Il y a une différence significative entre la moyenne de l'échantillon et {valeur_test}."
else:
    conclusion = f"On ne rejette pas H0. Il n'y a pas de preuve statistique que la moyenne réelle est différente de {valeur_test}."

print(f"Conclusion: {conclusion}")

# 6. Visualisations

# Figure 1: Population totale
plt.figure(1)
plt.hist(population, bins=50, alpha=0.7, color='skyblue', edgecolor='black')
plt.axvline(vraie_moyenne, color='red', linestyle='--', linewidth=2, label=f'Moyenne réelle: {vraie_moyenne:.2f}')
plt.axvline(valeur_test, color='green', linestyle='-', linewidth=2, label=f'Valeur testée: {valeur_test}')
plt.title('Distribution de la population totale (N=10 000)')
plt.xlabel('Valeur')
plt.ylabel('Fréquence')
plt.legend()
plt.savefig('population_totale.png')

# Figure 2: Échantillon
plt.figure(2)
plt.hist(echantillon, bins=20, alpha=0.7, color='lightgreen', edgecolor='black')
plt.axvline(moyenne_echantillon, color='blue', linestyle='--', linewidth=2, label=f'Moyenne échantillon: {moyenne_echantillon:.2f}')
plt.axvline(valeur_test, color='green', linestyle='-', linewidth=2, label=f'Valeur testée: {valeur_test}')
plt.title('Distribution de l\'échantillon (n=100)')
plt.xlabel('Valeur')
plt.ylabel('Fréquence')
plt.legend()
plt.savefig('echantillon.png')

# Figure 3: Intervalle de confiance
plt.figure(3)
plt.hist(echantillon, bins=20, alpha=0.5, color='lightgreen', edgecolor='black')
plt.axvline(moyenne_echantillon, color='blue', linestyle='--', linewidth=2, label=f'Moyenne échantillon: {moyenne_echantillon:.2f}')
plt.axvline(intervalle_confiance[0], color='purple', linestyle='-', linewidth=2, label=f'IC 95% min: {intervalle_confiance[0]:.2f}')
plt.axvline(intervalle_confiance[1], color='purple', linestyle='-', linewidth=2, label=f'IC 95% max: {intervalle_confiance[1]:.2f}')
plt.axvline(valeur_test, color='green', linestyle='-', linewidth=2, label=f'Valeur testée: {valeur_test}')
plt.title('Échantillon avec intervalle de confiance à 95%')
plt.xlabel('Valeur')
plt.ylabel('Fréquence')
plt.legend()
plt.savefig('intervalle_confiance.png')

# Figure 4: Comparaison des distributions
plt.figure(4, figsize=(14, 8))
plt.hist(population, bins=50, alpha=0.5, color='skyblue', edgecolor='black', density=True, label='Population')
plt.hist(echantillon, bins=20, alpha=0.5, color='lightgreen', edgecolor='black', density=True, label='Échantillon')
plt.axvline(vraie_moyenne, color='red', linestyle='--', linewidth=2, label=f'Moyenne réelle: {vraie_moyenne:.2f}')
plt.axvline(moyenne_echantillon, color='blue', linestyle='--', linewidth=2, label=f'Moyenne échantillon: {moyenne_echantillon:.2f}')
plt.axvline(valeur_test, color='green', linestyle='-', linewidth=2, label=f'Valeur testée: {valeur_test}')
plt.title('Comparaison des distributions (population vs échantillon)')
plt.xlabel('Valeur')
plt.ylabel('Densité')
plt.legend()
plt.savefig('comparaison_distributions.png')

print("\nLes graphiques ont été enregistrés dans le répertoire courant.") 