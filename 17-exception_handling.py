names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

# Unpack
*nordic_countries, es, ru = names

print("Nordic countries:", nordic_countries)
print("Estonia:", es)
print("Russia:", ru)

# * = unpack string, ** = unpack dictionaries

#para tratar erros: try, except, else, finally

# BOAS PRÁTICAS
# - Capture o erro MAIS ESPECÍFICO que fizer sentido.
# - Não use 'except:' nu — prefira tipos explícitos.
# - Mantenha o bloco try pequeno (isole a linha/trecho que pode falhar).
# - Registre/logue a exceção; não a silencie.
# - Use else/finally para lógica “pós-sucesso” e limpeza de recursos. :contentReference[oaicite:4]{index=4}
#