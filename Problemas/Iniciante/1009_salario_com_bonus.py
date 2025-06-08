# Salário  com Bônus

nome = input()
salario_fixo = float(input())
vendas_efetuadas = float(input())

comissao = (15*vendas_efetuadas)/100

print(f"TOTAL = R$ {salario_fixo+comissao:.2f}")