# ==========================================================
#  30 Days of Python - Day 25: Pandas (versão simples)
# ==========================================================
#  Destaques do dia:
# - Series e DataFrame
# - Leitura e escrita de CSV
# - Seleção (colunas/linhas) com [] / .loc / .iloc
# - Filtro com condições
# - Operações em colunas (criar/transformar)
# - Estatísticas rápidas: .describe()
# - Tratamento de valores ausentes (NaN)
# - Agrupamento e agregações: .groupby().agg()
# ==========================================================

import pandas as pd

# ----------------------------------------------------------
#  1) Criando uma Series e um DataFrame
# ----------------------------------------------------------
s = pd.Series([10, 20, 30], name="scores")
print("Series:\n", s, "\n")

data = {
    "name": ["Alice", "Bob", "Carol", "Dan", "Eva"],
    "age":  [23, 35, 29, None, 41],          # None -> vira NaN
    "city": ["SP", "RJ", "SP", "BH", "RJ"],
    "salary": [4500, 7200, 5200, 6100, None] # exemplo com NaN
}
df = pd.DataFrame(data)
print("DataFrame:\n", df, "\n")

# ----------------------------------------------------------
# 2) Visão geral rápida
# ----------------------------------------------------------
print("Head (primeiras linhas):\n", df.head(), "\n")
print("Info (tipos e nulos):")
df.info()
print("\nDescribe (estatísticas numéricas):\n", df.describe(numeric_only=True), "\n")

# ----------------------------------------------------------
#  3) Seleção de colunas e linhas
# ----------------------------------------------------------
# Coluna única
print("Coluna 'age':\n", df["age"], "\n")

# Múltiplas colunas
print("Colunas ['name','city']:\n", df[["name", "city"]], "\n")

# Seleção por rótulo (loc): linhas 0..2 e colunas name..age
print("loc (linhas 0..2, colunas name..age):\n", df.loc[0:2, ["name", "age"]], "\n")

# Seleção por posição (iloc): primeiras 3 linhas, colunas 0 e 2
print("iloc (linhas 0..2, colunas 0 e 2):\n", df.iloc[0:3, [0, 2]], "\n")

# ----------------------------------------------------------
#  4) Filtro com condições (boolean mask)
# ----------------------------------------------------------
# Pessoas da cidade "RJ"
rj = df[df["city"] == "RJ"]
print("Filtro city == 'RJ':\n", rj, "\n")

# Idade >= 30 (cuidando dos NaNs automaticamente)
older_30 = df[df["age"] >= 30]
print("Filtro age >= 30:\n", older_30, "\n")

# Combinando condições (use parênteses!)
sp_high_salary = df[(df["city"] == "SP") & (df["salary"] > 5000)]
print("SP e salary > 5000:\n", sp_high_salary, "\n")

# ----------------------------------------------------------
#  5) Criando/transformando colunas
# ----------------------------------------------------------
# Criar coluna com faixa salarial simples
df["salary_level"] = pd.cut(df["salary"], bins=[0, 5000, 7000, float("inf")],
                            labels=["low", "mid", "high"])
print("Com 'salary_level':\n", df, "\n")

# Aumentar salário em 10% (sem afetar NaNs)
df["salary_plus_10"] = df["salary"] * 1.10
print("Com 'salary_plus_10':\n", df, "\n")

# Preencher NaN de idade com média (exemplo de imputação simples)
age_mean = df["age"].mean()
df["age_filled"] = df["age"].fillna(age_mean)
print(f"Idade média usada para fillna: {age_mean:.2f}")
print("Com 'age_filled':\n", df, "\n")

# ----------------------------------------------------------
#  6) Tratamento de valores ausentes
# ----------------------------------------------------------
print("Contagem de nulos por coluna:\n", df.isna().sum(), "\n")

# Opção A: descartar linhas com qualquer NaN em 'salary'
drop_salary_na = df.dropna(subset=["salary"])
print("dropna em salary:\n", drop_salary_na, "\n")

# Opção B: preencher NaN de salary com mediana
salary_median = df["salary"].median()
df["salary_filled"] = df["salary"].fillna(salary_median)
print(f"Mediana de salary para fillna: {salary_median:.2f}")
print("Com 'salary_filled':\n", df, "\n")

# ----------------------------------------------------------
#  7) Agrupamento e agregações
# ----------------------------------------------------------
# Média de salário por cidade (usando a coluna preenchida)
group_city = df.groupby("city", dropna=False).agg(
    avg_salary=("salary_filled", "mean"),
    count=("name", "count")
).reset_index()
print("Média de salário por cidade:\n", group_city, "\n")

# Várias agregações por cidade
multi_agg = df.groupby("city", dropna=False).agg(
    min_age=("age_filled", "min"),
    max_age=("age_filled", "max"),
    avg_age=("age_filled", "mean")
).round(2).reset_index()
print("Idade (min/max/média) por cidade:\n", multi_agg, "\n")

# ----------------------------------------------------------
#  8) Leitura e escrita de CSV
#     (Demonstração simples: salvar e ler de volta)
# ----------------------------------------------------------
df.to_csv("people_example.csv", index=False, encoding="utf-8")
print("Arquivo 'people_example.csv' salvo.\n")

loaded = pd.read_csv("people_example.csv")
print("CSV recarregado:\n", loaded.head(), "\n")

# ----------------------------------------------------------
#  9) Extra: merge (junção) simples
# ----------------------------------------------------------
cities_info = pd.DataFrame({
    "city": ["SP", "RJ", "BH"],
    "state": ["São Paulo", "Rio de Janeiro", "Minas Gerais"]
})
merged = df.merge(cities_info, on="city", how="left")
print("Merge com info de estados:\n", merged[["name", "city", "state"]], "\n")
