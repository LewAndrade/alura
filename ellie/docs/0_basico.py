""" coisas que o python entende """
print('ela disse: # print(5+2.0)')

''' tipos de dados (data types) '''
# strings ou str, tipo texto
print("dentro de aspas")

# int integer/inteiro numero sem ponto
print(5)

# float (floating point)/(ponto flutuante)
print(502.0)

# bool (boolean)/(booleano) verdadeiro ou falso
print(True)

''' conversão de tipos '''
var = "3"  # é string
var_soq_numero = int(var)  # agora é numero
var_soq_float = float(var)  # agora é float
print(type(var), "e", type(var_soq_numero), "e", type(var_soq_float))

''' mais detalhes do print() '''
qualidade1 = "bonita"
qualidade2 = "cheirosa"
qualidade3 = "gostosa"
defeito = "amar demais"
print(f"A ellie, é {qualidade1}, é {qualidade2} e é {qualidade3}, mas tem seu defeito...., e seu defeito é {defeito}")

''' pegar input do usuario '''
ellie = input("esse é o input: ")  # pega o input
print(f"você escreveu: {ellie}")  # cospe o input
