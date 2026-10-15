"""Modelo físico en unidades SI, independiente del motor de animación."""

from math import sqrt


def posicion_a(t):
    return 25 * t


def posicion_b(t):
    return 60 - 10 * t + 2 * t**2


def posicion_c(t):
    return 150 + 6 * t**2 - (2 / 3) * t**3


def velocidad_b(t):
    return -10 + 4 * t


def velocidad_c(t):
    return 12 * t - 2 * t**2


def aceleracion_c(t):
    return 12 - 4 * t


def encuentros_ab():
    """Instantes de igualdad de posiciones, sin redondear resultados intermedios."""
    return (35 - sqrt(745)) / 4, (35 + sqrt(745)) / 4
