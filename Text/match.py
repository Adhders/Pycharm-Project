from fuzzywuzzy import fuzz
from fuzzywuzzy import process

### https://github.com/seatgeek/fuzzywuzzy

# Simple Ratio
a=fuzz.ratio('12345 7890','345 90')
print(a)

# Partial Ratio
b=fuzz.partial_ratio('12345 7890','345 78')
print(b)

# Token Sort Ratio
c=fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
d=fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
print(c,d)

# Token Set Ratio
e=fuzz.token_sort_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")
f=fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")
print(e,f)

# Process
choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
l=process.extract("new york jets", choices, limit=2)
m=process.extractOne("cowboys", choices)
n=process.extractOne("cowboys",choices,scorer=fuzz.token_sort_ratio)
print(l,m,n)