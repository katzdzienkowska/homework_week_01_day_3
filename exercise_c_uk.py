united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
for item in united_kingdom:
    if item.get("capital") == "Swansea":
       item.update({"capital": "Cardiff"})
#prints [{'name': 'Scotland', 'population': 5295000, 'capital': 'Edinburgh'}, {'name': 'Wales', 'population': 3063000, 'capital': 'Cardiff'}, {'name': 'England', 'population': 53010000, 'capital': 'London'}]

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
united_kingdom.append({"name" : "Northern Ireland", "capital" : "Belfast", "population" : int("1,811,000".replace(",",""))})
#prints [{'name': 'Scotland', 'population': 5295000, 'capital': 'Edinburgh'}, {'name': 'Wales', 'population': 3063000, 'capital': 'Cardiff'}, {'name': 'England', 'population': 53010000, 'capital': 'London'}, {'name': 'Northern Ireland', 'capital': 'Belfast', 'population': '1811000'}]

# 3. Use a loop to print the names of all the countries in the UK.
for country in united_kingdom:
  print(country["name"])
#prints:
# Scotland
# Wales
# England
# Northern Ireland

# 4. Use a loop to find the total population of the UK.

total_population = 0

for number in united_kingdom:
  total_population = total_population + number["population"]

print(total_population)
#prints 63179000
