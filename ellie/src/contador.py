def pergunta_loop(vezes):
    if vezes == 0:
        print("voce quer começar a contar sim ou nao?")
        resp = input("> ").lower().strip()
        return resp
    elif vezes == 1:
        print(f"voce ja contou {vezes} vez ainda quer contar sim ou nao?")
        resp = input("> ").lower().strip()
        return resp
    else:
        print(f"voce ja contou {vezes} vezes ainda quer contar sim ou nao?")
        resp = input("> ").lower().strip()
        return resp


def conta_ate(destino):
    for contador in range(1, destino + 1):
        print(contador)


def pega_destino():
    resp = input("qual o numero de destino? ")
    if resp.isdigit():
        return int(resp)
    else:
        while not resp.isdigit():
            print("nao entendi... tem que ser numero puta!!! (ps: inteiro ok?)")
            resp = input("qual o numero de destino? ")
        return int(resp)


def pega_destino_lew() -> int:
    resp = str(input("qual o numero de destino? "))
    if resp.isdigit():
        return int(resp)
    else:
        print("nao entendi... tem que ser numero puta!!! (ps: inteiro ok?)")
        pega_destino()


def contador_da_ellie():
    vezes = 0
    while pergunta_loop(vezes) == "sim":
        destino = pega_destino()
        conta_ate(destino)
        print(f"pronto, terminei de contar até {destino}")
        vezes = vezes + 1
    else:
        if vezes == 0:
            print("vai tomar no cu entao >:c")
        else:
            print("obrigada, por ter usado o melhor contador do mundo :3")


print(pega_destino_lew())
