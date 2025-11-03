print("="*72)
print("DIA 15 — TIPOS DE ERROS EM PYTHON (exemplos guiados)")
print("="*72)

# ---------------------------------------------------------------------------
# 1) SyntaxError
# ---------------------------------------------------------------------------
# Ocorre quando o Python não consegue interpretar o código (antes mesmo de executar).
# Esse tipo de erro NÃO pode ser capturado com try/except, pois impede o script de rodar.
# Exemplo (ERRADO – descomente para ver o erro):
# print 'olá mundo'   # Em Python 3, é obrigatório usar parênteses -> SyntaxError
#
# Versão correta:
print("\n[SyntaxError] -> Exemplo corrigido: print('olá mundo')")
print('olá mundo')

# ---------------------------------------------------------------------------
# 2) NameError
# ---------------------------------------------------------------------------
# Acontece quando tentamos usar uma variável ou função que ainda não foi definida.
print("\n[NameError] -> Demonstração segura com try/except")
try:
    # ERRADO (descomente para ver o erro real): print(idade)
    # Vamos provocar o erro de forma controlada:
    print(idade)  # noqa: F821  # intencionalmente não definida
except NameError as e:
    print("Capturado:", repr(e))
    idade = 25
    print("Correção: definir o nome antes de usar -> idade =", idade)

# ---------------------------------------------------------------------------
# 3) IndexError
# ---------------------------------------------------------------------------
# Ocorre ao tentar acessar um índice inexistente em uma lista ou tupla.
print("\n[IndexError] -> Demonstração segura com try/except")
numeros = [1, 2, 3, 4, 5]
try:
    print(numeros[5])  # índices válidos: 0..4
except IndexError as e:
    print("Capturado:", repr(e))
    print("Correção: usar um índice válido, ex.: numeros[-1] ->", numeros[-1])

# ---------------------------------------------------------------------------
# 4) ModuleNotFoundError
# ---------------------------------------------------------------------------
# Acontece quando tentamos importar um módulo inexistente (geralmente erro de digitação).
print("\n[ModuleNotFoundError] -> Exemplo comentado (para manter o script rodando)")
# ERRADO (descomente para ver o erro): import maths  # o correto é 'math'
import math
print("Importação correta funciona. math.sqrt(9) ->", math.sqrt(9))

# ---------------------------------------------------------------------------
# 5) AttributeError
# ---------------------------------------------------------------------------
# Erro ao tentar acessar um atributo que não existe em um objeto ou módulo.
print("\n[AttributeError] -> Demonstração segura com try/except")
try:
    print(math.PI)  # ERRADO: o nome correto é 'pi', não 'PI'
except AttributeError as e:
    print("Capturado:", repr(e))
    print("Correção: usar o nome certo -> math.pi =", math.pi)

# ---------------------------------------------------------------------------
# 6) KeyError
# ---------------------------------------------------------------------------
# Ocorre ao tentar acessar uma chave inexistente em um dicionário.
print("\n[KeyError] -> Demonstração segura com try/except e .get()")
usuario = {'nome': 'Asab', 'idade': 250, 'pais': 'Finlândia'}
try:
    print(usuario['pais_errado'])  # chave incorreta
except KeyError as e:
    print("Capturado:", repr(e))
    print("Correção: usar a chave correta -> usuario['pais'] =", usuario['pais'])
    # Ou usar .get() com valor padrão:
    print("Ou usar .get('pais_errado', 'N/A') ->", usuario.get('pais_errado', 'N/A'))

# ---------------------------------------------------------------------------
# 7) TypeError
# ---------------------------------------------------------------------------
# Acontece quando tentamos operar com tipos incompatíveis.
print("\n[TypeError] -> Demonstração segura com try/except e conversão de tipo")
try:
    print(4 + '3')  # int + str -> TypeError
except TypeError as e:
    print("Capturado:", repr(e))
    print("Correção A: converter '3' para int -> 4 + int('3') =", 4 + int('3'))
    print("Correção B: converter 4 para str -> str(4) + '3' =", str(4) + '3')

# ---------------------------------------------------------------------------
# 8) ImportError
# ---------------------------------------------------------------------------
# Acontece ao importar um módulo válido, mas tentando trazer um símbolo inexistente.
print("\n[ImportError] -> Exemplo comentado e correção")
# ERRADO (descomente para ver o erro): from math import power
from math import pow  # nome correto
print("math.pow funciona: pow(2, 3) ->", pow(2, 3))

# ---------------------------------------------------------------------------
# 9) ValueError
# ---------------------------------------------------------------------------
# Ocorre quando uma função recebe o tipo certo de argumento, mas com valor inválido.
print("\n[ValueError] -> Demonstração segura com try/except")
try:
    print(int('12a'))  # valor inválido para conversão
except ValueError as e:
    print("Capturado:", repr(e))
    print("Correção: passar apenas números -> int('12') =", int('12'))

# ---------------------------------------------------------------------------
# 10) ZeroDivisionError
# ---------------------------------------------------------------------------
# Acontece ao tentar dividir um número por zero.
print("\n[ZeroDivisionError] -> Demonstração segura com try/except")
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print("Capturado:", repr(e))
    print("Correção: verificar o divisor antes de dividir.")

print("\nTudo concluído! Leia os comentários acima e descomente as linhas para ver os tracebacks reais.")
print("="*72)
