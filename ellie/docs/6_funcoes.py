''' funcoes '''
# def declaclara funcao
# faz alguma coisa sem receber nada
def falar_cu():
    print("cu")

# funcao faz alguma coisa recebendo algo
def printa_soma(x, y):
    print(x + y)

# funcao retorna alguma coisa
def soma(x, y):
    soma = x + y
    return soma 

def area_triangulo(base, altura):
    return (base * altura) / 2


## exemplo
base_triangulo = int(input("base: "))
altura_triangulo = int(input("altura: "))

# chamar usa o funcao()
area_triangulo = area_triangulo(base_triangulo, altura_triangulo)


print(f"ahh, sea área do seu triangulo é {area_triangulo}")