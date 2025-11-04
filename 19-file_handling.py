# =========================
# 30DaysOfPython – FILE HANDLING (resumo)
# =========================
# ✅ Conceito:
# Manipular arquivos (criar, ler, escrever, apagar) em Python com a função open().
#
# 📄 open('arquivo', modo)
#  "r" = ler (erro se não existir) | padrão
#  "a" = append (adiciona ao final, cria se não existir)
#  "w" = write (sobrescreve, cria se não existir)
#  "x" = create (erro se já existir)
#  "t" = texto (padrão)
#  "b" = binário (ex.: imagens)
#
# ⚙️ Leitura:
# f = open('arquivo.txt')
# f.read()        -> lê tudo (string)
# f.readline()    -> lê 1 linha
# f.readlines()   -> lista com todas as linhas
# f.close()       -> fecha o arquivo (boa prática)
#
# 💡 Alternativa segura:
# with open('arquivo.txt') as f:
#     conteudo = f.read()
# (fecha automaticamente)
#
# ✍️ Escrita/Atualização:
# "a" → adiciona ao fim
# "w" → sobrescreve
# with open('arq.txt', 'a') as f: f.write('texto')
#
# 🗑️ Deletar:
# import os
# if os.path.exists('arq.txt'):
#     os.remove('arq.txt')
# else:
#     print('Arquivo não existe')
#
# =========================
# 🔹 FORMATS
# =========================
# .TXT → texto comum
#
# .JSON → JavaScript Object Notation
# import json
# json.loads(str_json)  -> JSON → dict
# json.dumps(dict)      -> dict → JSON (string)
# json.dump(dict, f)    -> salva em arquivo
#
# .CSV → dados separados por vírgula
# import csv
# with open('arq.csv') as f:
#     reader = csv.reader(f)
#     for row in reader: print(row)
#
# .XLSX → Excel (requer xlrd)
# import xlrd
# book = xlrd.open_workbook('arquivo.xls')
#
# .XML → estrutura hierárquica semelhante ao HTML
# import xml.etree.ElementTree as ET
# tree = ET.parse('arquivo.xml')
# root = tree.getroot()
# for child in root: print(child.tag)
#
# ✅ Resumo Final:
# - open() → cria/abre arquivos em vários modos
# - with → fecha automático
# - os.remove() → apaga
# - json, csv, xlrd, xml.etree → módulos para diferentes formatos
