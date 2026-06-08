## Shallow Copy
dado_01 = {
    'c1': 10,
    'c2': 11,
    'l1': [0, 1, 2],
}

# dado_02 = dado_01
dado_02 = dado_01.copy()

# Dado imutável
dado_02['c1'] = 35
dado_02['c2'] = 36

# Dado mutável
dado_02['l1'][1] = 999999

print(f"Dado_01: {dado_01}")
print(f"Dado_02: {dado_02}\n")

## Deep Copy
import copy

dado_01 = {
    'c1': 10,
    'c2': 11,
    'l1': [0, 1, 2],
}

dado_02 = copy.deepcopy(dado_01)

# "Cópia profundo"
dado_02['c1'] = 35
dado_02['c2'] = 36
dado_02['l1'][1] = 999999

print(f"Dado_01: {dado_01}")
print(f"Dado_02: {dado_02}")
