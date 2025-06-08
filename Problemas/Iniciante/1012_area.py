# Área: https://judge.beecrowd.com/pt/problems/view/1012
'''
entrada: 
3.0 4.0 5.2

saida: 
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000
'''

a, b, c = map(float, input().split())

print(f"TRIANGULO: {a*c/2:.3f}")
print(f"CIRCULO: {3.14159 * c ** 2:.3f}")
print(f"TRAPEZIO: {((a + b) * c) / 2:.3f}")
print(f"QUADRADO: {b ** 2:.3f}")
print(f"RETANGULO: {a * b:.3f}")
