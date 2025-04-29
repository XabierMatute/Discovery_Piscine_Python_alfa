#!/usr/bin/python3
import statistics

# def famous_births(d):
#     for famous in sorted(d.keys(), key=lambda name: d[name]["date_of_birth"]):
#         print(f'{d[famous]["name"]} is a great scientist born in {d[famous]["date_of_birth"]}.')

def famous_births(d):
    for famous in sorted(d.values(), key=lambda f: f["date_of_birth"]):
        print(f'{famous["name"]} is a great scientist born in {famous["date_of_birth"]}.')


women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)