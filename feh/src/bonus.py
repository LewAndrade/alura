from random import choice

# contagem de cu numa lista de tamanho 69

def jeito_do_fe():
    lista = []
    contagem = []
    for i in range(69):
        lista.append(choice(["banana", "abacate", "porra", "cu"]))
    for i in lista:
        if i == "cu":
            contagem.append(i)
    print(len(contagem))

def jeito_da_lew():
    print(len([i for i in [choice(["banana", "abacate", "porra", "cu"]) for i in range(69)] if i == "cu"]))

def jeito_da_ellie():
    print("cu")