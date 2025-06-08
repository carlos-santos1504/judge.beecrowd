# Média 2

def erro():
    print("Por favor insira o valor de 1 a 10")
    print("------------------------------")
    print("Reiniciando programa")

def calcular():
    print("------------------------------")
    print("Iniciando o calculo de media 2")
    print("Informe o primeiro valor")
    a = float(input())
    if(a<0 or a>10):
        erro()
        calcular()  
    print("Informe o segundo valor")  
    b = float(input())
    if(b<0 or b>10):
        erro()
        calcular()    
    print("Informe o terceiro valor")
    c = float(input())
    if(c<0 or c>10):
        erro()
        calcular()    
    
    media = ((a*2)/10 + (b*3)/10 + (c*5)/10)

    print(f"MEDIA = {media:.1f}")

calcular()
