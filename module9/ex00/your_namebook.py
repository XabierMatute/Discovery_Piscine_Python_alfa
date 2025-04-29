#!/usr/bin/python3
def array_of_names(d):
    a = []
    for name in d:
        a.append(name.capitalize() + ' ' + d[name].capitalize())
    return a

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))