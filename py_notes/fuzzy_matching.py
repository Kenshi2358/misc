"""
Fuzzy matching example.

Using fuzz.ratio, a score of 100 is a perfect score and the strings match exactly.


"""
from thefuzz import fuzz

str1 = "cat"
str2 = "cat in the hat"

result1 = fuzz.ratio(str1, str2)
result2 = fuzz.partial_ratio(str1, str2)

print(f"The simple ratio similarity score is: {result1}")
print(f"The partial ratio similarity score is: {result2}")
