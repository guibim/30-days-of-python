#1 
import requests
import statistics
from collections import Counter
import re

url = "https://www.gutenberg.org/cache/epub/1112/pg1112.txt"
text = requests.get(url).text

# Limpeza básica
words = re.findall(r'\b[a-zA-Z]+\b', text.lower())


counter = Counter(words)
top_10 = counter.most_common(10)

print("As 10 palavras mais frequentes:")
for word, freq in top_10:
    print(f"{word}: {freq}")


#2 
import requests
import statistics
from collections import Counter

# ============ Read data from The Cat API ============
cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
data = response.json()


weights = []
lifespans = []
countries = []
breeds = []

for cat in data:

    if 'weight' in cat and 'metric' in cat['weight']:
        w = cat['weight']['metric']
        if w and ' - ' in w:
            low, high = w.split(' - ')
            weights.append((float(low) + float(high)) / 2)

  
    if 'life_span' in cat:
        ls = cat['life_span']
        if ' - ' in ls:
            low, high = ls.split(' - ')
            lifespans.append((float(low) + float(high)) / 2)
        else:
            lifespans.append(float(ls))

   
    countries.append(cat.get('origin', 'Unknown'))
    breeds.append(cat['name'])


def describe(values):
    return {
        'min': min(values),
        'max': max(values),
        'mean': statistics.mean(values),
        'median': statistics.median(values),
        'stdev': statistics.stdev(values)
    }

weight_stats = describe(weights)
lifespan_stats = describe(lifespans)

print("Weight (kg) stats:", weight_stats)
print("Lifespan (years) stats:", lifespan_stats)


country_counts = Counter(countries)

print("\nFrequency Table (Country → #Breeds):")
for country, count in country_counts.most_common():
    print(f"{country:25s}: {count}")


# 3

URL = "https://restcountries.com/v3.1/all?fields=name,area,languages"


resp = requests.get(URL, timeout=30)
resp.raise_for_status()
countries = resp.json()

areas = []
for c in countries:
    name = c.get("name", {}).get("common") or c.get("name", {}).get("official")
    area = c.get("area")
    if name is not None and isinstance(area, (int, float)):
        areas.append((name, float(area)))

top10_by_area = sorted(areas, key=lambda x: x[1], reverse=True)[:10]


lang_counter = Counter()
unique_langs = set()

for c in countries:
    langs = c.get("languages") or {}
    
    for lname in langs.values():
        if lname:
            lang_counter[lname] += 1
            unique_langs.add(lname)

top10_langs = lang_counter.most_common(10)
total_unique_languages = len(unique_langs)


print("=== 10 Largest Countries (by area) ===")
for i, (name, area) in enumerate(top10_by_area, 1):
    print(f"{i:2d}. {name} — {area:,.0f} km²")

print("\n=== 10 Most Common Languages (by # of countries listing it) ===")
for i, (lname, count) in enumerate(top10_langs, 1):
    print(f"{i:2d}. {lname}: {count}")

print(f"\nTotal unique languages in API: {total_unique_languages}")
