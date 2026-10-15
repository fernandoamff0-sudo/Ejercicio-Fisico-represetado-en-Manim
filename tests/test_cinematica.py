"""Resultados físicos conocidos; no requieren instalar Manim."""

import unittest

from cinematica import (
    aceleracion_c, encuentros_ab, posicion_a, posicion_b, posicion_c,
    velocidad_b, velocidad_c,
)


class CinematicaTests(unittest.TestCase):
    def test_condiciones_iniciales(self):
        self.assertEqual((posicion_a(0), posicion_b(0), posicion_c(0)), (0, 60, 150))
        self.assertEqual(velocidad_b(0), -10)
        self.assertEqual(velocidad_c(0), 0)

    def test_dos_encuentros(self):
        primero, segundo = encuentros_ab()
        self.assertLess(primero, segundo)
        for t in (primero, segundo):
            self.assertAlmostEqual(posicion_a(t), posicion_b(t), places=10)
        self.assertAlmostEqual(primero, 1.9263279680219094)
        self.assertAlmostEqual(segundo, 15.573672031978091)

    def test_posicion_encuentro_sin_redondeo_intermedio(self):
        t = encuentros_ab()[0]
        self.assertAlmostEqual(posicion_a(t), 48.158199200547735)
        self.assertEqual(f'{posicion_a(t):.2f}', '48.16')

    def test_cambio_sentido_b(self):
        self.assertLess(velocidad_b(2.4), 0)
        self.assertEqual(velocidad_b(2.5), 0)
        self.assertGreater(velocidad_b(2.6), 0)
        self.assertEqual(posicion_b(2.5), 47.5)

    def test_maximo_velocidad_c(self):
        self.assertEqual(aceleracion_c(3), 0)
        self.assertEqual(velocidad_c(3), 18)
        self.assertLess(velocidad_c(2.9), 18)
        self.assertLess(velocidad_c(3.1), 18)

    def test_cambio_sentido_c(self):
        self.assertGreater(velocidad_c(5.9), 0)
        self.assertEqual(velocidad_c(6), 0)
        self.assertLess(velocidad_c(6.1), 0)
        self.assertEqual(posicion_c(6), 222)

    def test_retorno_c_y_separacion(self):
        self.assertEqual(posicion_c(9), 150)
        self.assertEqual((posicion_a(9), posicion_b(9)), (225, 132))
        self.assertEqual(abs(posicion_a(9) - posicion_b(9)), 93)

    def test_velocidad_es_derivada_de_posicion(self):
        h = 1e-5
        for posicion, velocidad in ((posicion_b, velocidad_b), (posicion_c, velocidad_c)):
            for t in (0, 2.5, 3, 6, 9):
                derivada = (posicion(t + h) - posicion(t - h)) / (2 * h)
                self.assertAlmostEqual(derivada, velocidad(t), places=6)


if __name__ == '__main__':
    unittest.main()
