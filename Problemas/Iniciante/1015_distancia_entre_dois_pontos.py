# Distância Entre Dois Pontos
'''
entrada
1.0 7.0
5.0 9.0
saida
4.4721
'''

import math

x1,y1 = map(float, input().split())
x2,y2 = map(float, input().split())

distancia = math.sqrt(((x2-x1) ** 2) + ((y2-y1) ** 2))

print(f"{distancia:.4f}")