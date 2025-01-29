import sys

def comprimento(raio: float) -> float:
    """Faz o calculo do comprimento

    Args:
        raio (float): medida do raio a ser utilizada

    Returns:
        float: valor do comprimento
    """
    return round(2 * 3.14 * raio, 2)

print(comprimento(float(sys.argv[1])))
