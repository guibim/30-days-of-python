# regex = regular expression

import re
from collections import Counter

# re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
# re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
# re.findall: Returns a list containing all matches
# re.split: Takes a string, splits it at the match points, returns a list
# re.sub: Replaces one or many matches within a string]
# findall() returns all the matches as a list

# What is the most frequent word in the following paragraph?
paragraph = """I love teaching. If you do not love teaching what else can you love.
I love Python if you do not love something which can give you all the
capabilities to develop an application what else can you love."""

# Deixa tudo minúsculo e remove pontos
text = paragraph.lower().replace(".", "")

# Divide em palavras
words = text.split()

# Conta e acha a mais comum
most_common = max(set(words), key=words.count)

print("Palavra mais frequente:", most_common)
print("Frequência:", words.count(most_common))
