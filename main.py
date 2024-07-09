# Autor: Bryan Castillo
# Fecha" 08/07/2024
# Version: 3.12.3 64-bit


from operaciones import Matematicas, geometria

print(Matematicas.suma(3, 5))
print(Matematicas.resta(3, 5))
print(Matematicas.multiplicacion(3, 5))
print(Matematicas.division(3, 5))

print(geometria.area_circulo(5))
print(geometria.perimetro_circulo(5))
print(geometria.area_rectangulo(3, 5))
print(geometria.perimetro_rectangulo(3, 5))


import operaciones.Matematicas as Matematicas
import operaciones.geometria as geometria

print(Matematicas.multiplicacion(10, 5))
print(Matematicas.division(10, 5))
print(geometria.area_rectangulo(10, 5))
print(geometria.perimetro_rectangulo(10, 5))
