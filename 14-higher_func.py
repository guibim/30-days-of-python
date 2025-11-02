# day14_exercises.py
# 30 Days of Python — Day 14 (Functional Programming)
# Níveis 1 e 2 compactados em um único script executável.

from functools import reduce
from collections import defaultdict
from typing import Iterable, List, Dict, Any

# ----------------------------
# Dados base
# ----------------------------
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ----------------------------
# Level 1
# ----------------------------

def explain_map_filter_reduce() -> Dict[str, str]:
    return {
        "map": "Aplica uma função a cada item de um iterável e retorna os itens transformados.",
        "filter": "Seleciona itens de um iterável para os quais a função/condição retorna True.",
        "reduce": "Reduz um iterável a um único valor acumulado (por ex.: soma, produto).",
    }


def explain_hof_closure_decorator() -> Dict[str, str]:
    return {
        "higher_order_function": "Função que recebe outra função como argumento e/ou retorna uma função.",
        "closure": "Função interna que 'lembra' variáveis do escopo externo mesmo após este escopo ter finalizado.",
        "decorator": "Padrão que envolve uma função para estender/modificar seu comportamento.",
    }


# Funções de exemplo para usar com map, filter, reduce
def square(x: int) -> int:
    return x ** 2


def is_even(x: int) -> bool:
    return x % 2 == 0


def add(a: int, b: int) -> int:
    return a + b


def print_each_country(countries_list: Iterable[str]) -> None:
    for c in countries_list:
        print(c)


def print_each_name(names_list: Iterable[str]) -> None:
    for n in names_list:
        print(n)


def print_each_number(numbers_list: Iterable[int]) -> None:
    for num in numbers_list:
        print(num)


# ----------------------------
# Level 2
# ----------------------------

def map_countries_upper(countries_list: Iterable[str]) -> List[str]:
    return list(map(str.upper, countries_list))


def map_numbers_square(numbers_list: Iterable[int]) -> List[int]:
    return list(map(lambda x: x ** 2, numbers_list))


def map_names_upper(names_list: Iterable[str]) -> List[str]:
    return list(map(str.upper, names_list))


def filter_countries_with_land(countries_list: Iterable[str]) -> List[str]:
    return list(filter(lambda c: 'land' in c.lower(), countries_list))


def filter_countries_exact_len(countries_list: Iterable[str], n: int) -> List[str]:
    return list(filter(lambda c: len(c) == n, countries_list))


def filter_countries_len_at_least(countries_list: Iterable[str], n: int) -> List[str]:
    return list(filter(lambda c: len(c) >= n, countries_list))


def filter_countries_starting_with(countries_list: Iterable[str], letter: str = 'E') -> List[str]:
    return list(filter(lambda c: c.startswith(letter), countries_list))


def chain_iterators_example(numbers_list: Iterable[int]) -> int:
    """
    Exemplo: soma dos quadrados dos pares.
    filter -> map -> reduce
    """
    return reduce(add, map(square, filter(is_even, numbers_list)), 0)


def get_string_lists(lst: Iterable[Any]) -> List[str]:
    """Retorna apenas os itens que são strings."""
    return [item for item in lst if isinstance(item, str)]


def reduce_sum_numbers(numbers_list: Iterable[int]) -> int:
    return reduce(add, numbers_list, 0)


def reduce_countries_sentence(countries_list: List[str]) -> str:
    """
    Concatena os países em uma sentença:
    'Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries'
    """
    if not countries_list:
        return ""
    if len(countries_list) == 1:
        head = countries_list[0]
        return f"{head} is a north European country"
    head = ", ".join(countries_list[:-1])
    tail = countries_list[-1]
    return f"{head}, and {tail} are north European countries"


def categorize_countries(countries_list: Iterable[str], patterns: Iterable[str]) -> Dict[str, List[str]]:
    """
    Retorna países que contêm cada padrão (ex.: 'land', 'ia', 'island', 'stan').
    """
    result: Dict[str, List[str]] = {}
    for p in patterns:
        result[p] = [c for c in countries_list if p.lower() in c.lower()]
    return result


def countries_by_start_letter(countries_list: Iterable[str]) -> Dict[str, int]:
    """
    Dicionário: {letra_inicial: quantidade}
    """
    counts = defaultdict(int)
    for c in countries_list:
        if c:
            counts[c[0].upper()] += 1
    return dict(counts)


def get_first_ten_countries(countries_list: List[str]) -> List[str]:
    return countries_list[:10]


def get_last_ten_countries(countries_list: List[str]) -> List[str]:
    return countries_list[-10:]


# ----------------------------
# Execução de demonstração
# ----------------------------

if __name__ == "__main__":
    print("== Diferenças: map/filter/reduce ==")
    print(explain_map_filter_reduce(), end="\n\n")

    print("== Diferenças: HOF / Closure / Decorator ==")
    print(explain_hof_closure_decorator(), end="\n\n")

    print("== Exemplo de funções chamadas por map/filter/reduce ==")
    print("map(square, numbers):", list(map(square, numbers)))
    print("filter(is_even, numbers):", list(filter(is_even, numbers)))
    print("reduce(add, numbers):", reduce(add, numbers, 0), end="\n\n")

    print("== For loops ==")
    print("Countries:")
    print_each_country(countries)
    print("Names:")
    print_each_name(names)
    print("Numbers:")
    print_each_number(numbers)
    print()

    print("== Level 2: map ==")
    print("Countries upper:", map_countries_upper(countries))
    print("Numbers squared:", map_numbers_square(numbers))
    print("Names upper:", map_names_upper(names), end="\n\n")

    print("== Level 2: filter ==")
    print("Countries with 'land':", filter_countries_with_land(countries))
    print("Countries length == 6:", filter_countries_exact_len(countries, 6))
    print("Countries length >= 6:", filter_countries_len_at_least(countries, 6))
    print("Countries starting with 'E':", filter_countries_starting_with(countries, 'E'), end="\n\n")

    print("== Level 2: chaining iterators ==")
    print("Sum of squares of even numbers:", chain_iterators_example(numbers), end="\n\n")

    print("== Apenas strings de uma lista mista ==")
    mixed = ['Python', 10, True, 'JavaScript', 3.14, 'Go']
    print("String-only:", get_string_lists(mixed), end="\n\n")

    print("== Reduce: soma dos números ==")
    print("Sum:", reduce_sum_numbers(numbers), end="\n\n")

    print("== Reduce: sentença com países ==")
    print(reduce_countries_sentence(countries), end="\n\n")

    print("== Categorize countries (patterns: 'land', 'ia', 'island', 'stan') ==")
    print(categorize_countries(countries, ['land', 'ia', 'island', 'stan']), end="\n\n")

    print("== Dicionário: países por letra inicial ==")
    print(countries_by_start_letter(countries), end="\n\n")

    print("== First ten countries (do dataset dado) ==")
    print(get_first_ten_countries(countries))
    print("== Last ten countries (do dataset dado) ==")
    print(get_last_ten_countries(countries))
