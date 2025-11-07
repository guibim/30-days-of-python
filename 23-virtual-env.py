# ================================================
# 30 Days of Python - Dia 23: Virtual Environment
# ================================================
# Objetivo:
# Praticar a criação e o uso de ambientes virtuais no Windows.
# Um ambiente virtual permite isolar as dependências de cada projeto,
# evitando conflitos entre versões de bibliotecas e mantendo o sistema limpo.

# ------------------------------------------------
# 1. Criar um ambiente virtual
# ------------------------------------------------
# No terminal (CMD ou PowerShell), dentro da pasta do projeto, execute:
# > python -m venv venv
# Isso cria uma pasta chamada "venv" contendo uma cópia isolada do interpretador Python.

# ------------------------------------------------
# 2. Ativar o ambiente virtual
# ------------------------------------------------
# Para ativar o ambiente no Windows, use:
# > .\venv\Scripts\activate
# O prompt mostrará algo como: (venv) C:\projeto>
# Isso indica que o ambiente virtual está ativo.

# ------------------------------------------------
# 3. Instalar pacotes dentro do ambiente
# ------------------------------------------------
# Qualquer pacote instalado agora será adicionado apenas a este ambiente.
# Exemplo:
# > pip install requests

# Podemos testar o funcionamento com um pequeno script:

import requests

response = requests.get("https://api.github.com")
print("Status da requisição:", response.status_code)
print("Tipo de conteúdo:", response.headers.get("content-type"))

# ------------------------------------------------
# 4. Gerar o arquivo de dependências
# ------------------------------------------------
# Após instalar os pacotes necessários, gere o arquivo de dependências:
# > pip freeze > requirements.txt
# Esse arquivo lista todas as bibliotecas instaladas e suas versões.

# ------------------------------------------------
# 5. Ignorar o ambiente no Git
# ------------------------------------------------
# Para não subir a pasta "venv" ao repositório, adicione ao arquivo .gitignore:
# venv/

# ------------------------------------------------
# 6. Desativar o ambiente
# ------------------------------------------------
# Quando terminar, basta desativar o ambiente virtual:
# > deactivate

# ------------------------------------------------
# 7. Reflexão
# ------------------------------------------------
# Ambientes virtuais são fundamentais para manter projetos Python organizados.
# Eles isolam dependências, evitam conflitos de versão e permitem reproduzir
# exatamente o mesmo ambiente em outros computadores, bastando instalar os
# pacotes listados em requirements.txt.
# Essa prática é padrão profissional em desenvolvimento Python e deve ser usada
# em todos os projetos.

# Fim do arquivo - Day 2
