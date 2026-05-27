import math

PI = math.pi

def area_do_circulo(raio: float) -> float:
    """
    Função para calcular e retornar a área do círculo.
    """
    return PI * (raio ** 2)

def volume_da_esfera(raio: float) -> float:
    """
    Função para calcular e retornar o volume da esfera.
    """
    return ( 4 * PI * (raio ** 3) ) / 3

def hipotenusa(cateto_a, cateto_b) -> float:
    """
    Função para calcular e retornar a hipotenusa de um triângulo, usando
    os catetos conhecidos.
    """
    return ( (cateto_a**2) + (cateto_b**2) ) ** (1/2)