import sys

def comprimento(raio) -> float:
    return round(2 * 3.14 * raio,2)

print(comprimento(float(sys.argv[1])))
