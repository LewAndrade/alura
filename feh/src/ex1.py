#  1. Simulador de Dado

# Objetivo: Seu script deve gerar um valor aleatório entre 1 e 6(ou uma faixa que você definir)
# e permitir que o usuário rode o script quantas vezes quiser.

# Habilidades praticas a aplicar:

#     Tratamento de exceções
#     Condicionais If/Else
#     Input de dados
#     Geração de valores
#     Print

# Detalhes e boas Práticas: Você deve desenvolver um projeto em Python que irá rodar inicialmente
# na linha de comando e que, ao ser executado, deverá pergunta o seguinte ao usuário: “Você
# gostaria de jogar o dado?” Ou alguma variação dessa pergunta. Depois de ter feito essa pergunta,
# o seu programa precisa avaliar a resposta que foi digitado pelo usuário.

# Um passo importante aqui é que, quando digo avaliar quero dizer que você precisa receber o valor,
#  tratar quando ele(a) disser que sim ou que não. Seu programa depois deverá fazer a ação necessária
#  de acordo com a resposta que foi entrada pelo usuário. Seu script não deve quebrar ou para de
#  funcionar caso o usuário entre algo que não seja esperado, como, por exemplo, um número.
#  Trate as exceções ou erros para que seu script rode liso e sem problemas.

# Caso a resposta a pergunta inicial tenha sido “sim” ou positiva de alguma forma, gere um valor
# aleatoriamente entre 1 e 6(você pode claro alterar essa faixa) e exiba o número no console para
# o usuário. Na sequência pergunte se ele(a) quer rodar o script novamente e trate essa situação
# para que continue rodando enquanto a resposta for positiva, fechando apenas quando for um “não”.

# "Vocẽ gostaria de rodar o dado ?"
# "se o valor for positivo, continua, se não fecha"
# "se positivo gera valor aleatorio de 1 a 6"

### JEITO DO FE ###
def jeito_do_fe():
    from random import randint

    def randomiza_dado():
        print(randint(1, 6))
        pass

    def pergunta(is_first_time):
        positivo = ["sim", "si", "s", "yes", "yup", "yah", "oh yeh"]

        if is_first_time:
            print("Vocẽ gostaria de rodar o dado?")
        else:
            print("Vocẽ gostaria de rodar o dado novamente?")

        escolha = input("> ").lower()

        return escolha in positivo

    is_first_time = True

    while pergunta(is_first_time):
        randomiza_dado()
        is_first_time = False
    else:
        print("vai te fuder então")


## JEITO DA LEW ###
def jeito_da_lew():
    from random import randint

    def randomiza_dado():
        return randint(1, 6)

    def validar_resposta(is_first_time):
        positivo = ["sim", "si", "s", "yes", "yup", "yah", "oh yeh"]

        print("Vocẽ gostaria de rodar o dado?" if is_first_time else "Vocẽ gostaria de rodar o dado novamente?")
        escolha = input("> ").lower()

        return escolha in positivo

    is_first_time = True

    while validar_resposta(is_first_time):
        print(f"O dado deu: {randomiza_dado()}")
        is_first_time = False
    else:
        print("vai te fuder então")
