# Cálculo Simples

valor_1 = input().split(" ")
valor_2 = input().split(" ")

resultado = float(valor_1[1])*float(valor_1[2]) + float(valor_2[1])*float(valor_2[2])

print(f"VALOR A PAGAR: R$ {resultado:.2f}")