# ==========================================================
#  30 Days of Python - Day 24: Statistics (com bibliotecas)
# ==========================================================
#  Destaques do dia:
# - Biblioteca statistics (nativa do Python)
# - Biblioteca numpy (numérica e vetorial)
# - Comparação entre cálculos manuais e automáticos
# ==========================================================

import math
from collections import Counter
import statistics
import numpy as np

# ----------------------------------------------------------
#  Conjunto de dados (exemplo)
# ----------------------------------------------------------
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# ==========================================================
#  PARTE 1 - CÁLCULOS MANUAIS (baseados no dia 24)
# ==========================================================
n = len(ages)
mean_manual = sum(ages) / n

sorted_ages = sorted(ages)
mid = n // 2
if n % 2 != 0:
    median_manual = sorted_ages[mid]
else:
    median_manual = (sorted_ages[mid - 1] + sorted_ages[mid]) / 2

mode_manual = Counter(ages).most_common(1)[0][0]
range_manual = max(ages) - min(ages)
variance_manual = sum((x - mean_manual) ** 2 for x in ages) / (n - 1)
std_manual = math.sqrt(variance_manual)

# ==========================================================
#  PARTE 2 - USANDO MÓDULO STATISTICS
# ==========================================================
mean_stat = statistics.mean(ages)
median_stat = statistics.median(ages)
mode_stat = statistics.mode(ages)
variance_stat = statistics.variance(ages)
std_stat = statistics.stdev(ages)

# ==========================================================
#  PARTE 3 - USANDO NUMPY (mais rápido e vetorial)
# ==========================================================
ages_np = np.array(ages)

mean_np = np.mean(ages_np)
median_np = np.median(ages_np)
mode_np = np.bincount(ages_np).argmax()   # ou scipy.stats.mode se quiser mais completo
variance_np = np.var(ages_np, ddof=1)     # ddof=1 para amostral
std_np = np.std(ages_np, ddof=1)
range_np = np.ptp(ages_np)                # peak to peak (max - min)

# ==========================================================
# 📊 RESULTADOS COMPARADOS
# ==========================================================
print("=== Dados ===")
print(ages)
print("\n=== Cálculos manuais ===")
print(f"Média: {mean_manual:.2f}")
print(f"Mediana: {median_manual}")
print(f"Moda: {mode_manual}")
print(f"Amplitude: {range_manual}")
print(f"Variância: {variance_manual:.2f}")
print(f"Desvio padrão: {std_manual:.2f}")

print("\n=== Com módulo statistics ===")
print(f"Média: {mean_stat:.2f}")
print(f"Mediana: {median_stat}")
print(f"Moda: {mode_stat}")
print(f"Variância: {variance_stat:.2f}")
print(f"Desvio padrão: {std_stat:.2f}")

print("\n=== Com NumPy ===")
print(f"Média: {mean_np:.2f}")
print(f"Mediana: {median_np}")
print(f"Moda: {mode_np}")
print(f"Amplitude: {range_np}")
print(f"Variância: {variance_np:.2f}")
print(f"Desvio padrão: {std_np:.2f}")
