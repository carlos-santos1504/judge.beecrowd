# O Maior
'''
entrada
7 14 106

saida
106 eh o maior
'''
a,b,c = map(int,input().split())

MaiorA_B = (a+b+abs(a-b))/2
MaiorAB_C = (MaiorA_B+c+abs(MaiorA_B-c))/2
print(f"{MaiorAB_C:.0f} eh o maior")