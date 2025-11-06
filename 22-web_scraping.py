# ============================================
# 30 Days of Python — Dia 22 (Resumo): Web Scraping
# ============================================
# OBJETIVO
# - Extrair dados de páginas web de forma programática e estruturada.
#
# PRINCIPAIS FERRAMENTAS
# - requests: realizar requisições HTTP (GET/POST), cabeçalhos, status codes.
# - BeautifulSoup (bs4) / lxml: fazer parsing de HTML e navegar/selecionar elementos.
# - pandas.read_html: extrair tabelas diretamente de HTML.
# - (Opcional) Selenium/Playwright: páginas dinâmicas (JS pesado, scroll, botões).
#
# FLUXO BÁSICO
# 1) Definir o alvo e inspecionar o HTML no navegador (tags, classes, ids, estruturas).
# 2) Fazer GET com headers (User-Agent) e validar status_code (200).
# 3) Parsear HTML (BeautifulSoup/lxml) e localizar nós (select, find, find_all).
# 4) Limpar texto (strip, regex, remoção de notas/footers) e normalizar campos.
# 5) Salvar dados (JSON/CSV/Parquet/DB) com schema consistente.
#
# BOAS PRÁTICAS E ÉTICA
# - Respeitar robots.txt e Termos de Uso; não coletar dados sensíveis/pessoais.
# - Usar User-Agent explícito; aplicar backoff/delay entre requisições (educação).
# - Limitar taxa (rate limiting) e páginas por sessão; evitar sobrecarregar o site.
# - Tratar encoding (UTF-8), links relativos, paginação e erros de rede.
#
# TRATAMENTO DE ERROS (ROBUSTEZ)
# - Tentar novamente (retries) em 429/5xx com backoff exponencial.
# - Capturar exceções de parsing (elementos ausentes mudam com o tempo).
# - Validar mínimo de campos antes de salvar (ex.: título + url).
#
# PADRÕES DE SELEÇÃO
# - CSS selectors (soup.select("table.data > tr td:nth-child(2)")).
# - Busca semântica (por texto, atributos: class/id/data-*) e hierarquia (parent/next_sibling).
# - Para tabelas simples, preferir pandas.read_html; para estrutura irregular, BeautifulSoup.
#
# DADOS DINÂMICOS
# - Se o conteúdo é renderizado via JS/API: buscar endpoints JSON no DevTools (Network) ou usar Selenium.
#
# ARMAZENAMENTO
# - JSON: flexível, bom para APIs; CSV: leve e interoperável; Parquet: colunar e eficiente; DB (SQLite/Postgres) para histórico.
#
# CHECKLIST RÁPIDO
# [ ] Conferir robots.txt
# [ ] Definir User-Agent e timeout
# [ ] Tratar status_code e redirecionamentos
# [ ] Seletores estáveis (classes/id) e limpeza de texto
# [ ] Paginação / limites de coleta
# [ ] Salvar com schema consistente
# [ ] Log básico do processo (quantidade de itens, tempo, erros)
#
# MINI ESQUELETO (referência)
# import requests, pandas as pd
# from bs4 import BeautifulSoup
#
# url = "https://exemplo.com"
# headers = {"User-Agent": "Mozilla/5.0 ..."}
# r = requests.get(url, headers=headers, timeout=30)
# r.raise_for_status()
#
# soup = BeautifulSoup(r.text, "html.parser")
# itens = []
# for card in soup.select(".card-item"):
#     titulo = card.select_one(".title").get_text(strip=True) if card.select_one(".title") else ""
#     link = card.select_one("a")["href"] if card.select_one("a") else ""
#     itens.append({"titulo": titulo, "link": link})
#
# # Ex.: salvar JSON
# import json, os
# os.makedirs("data", exist_ok=True)
# with open("data/itens.json", "w", encoding="utf-8") as f:
#     json.dump(itens, f, ensure_ascii=False, indent=2)
#
# Observação: para páginas que mudam com JavaScript, buscar endpoints JSON em Network
# ou usar Selenium/Playwright (com parcimônia).
