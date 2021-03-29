''' repetição '''

# while
# loop infinito
while True:
    print("cu grande")

# contagem regressiva com input 
contagem = int(input("contagem regressiva de: "))
while contagem >= 0:
    print("rodada: ", contagem)
    contagem = contagem - 1
    
# contagem progressiva com variavel
contador = 1
destino = 10

while contador <= destino:
    print(contador)
    contador = contador + 1

# loop que para quando o usuario escolhe sair
variavel = "CONTINUAR"

while variavel != "SAIR":
    print("vou continuar até voce chorar")
    variavel = input("se quiser parar, digite SAIR:").strip().upper()

print("voce saiu")

# loop for

# percorrendo range()
for contador in range(1, 10 + 1):
    print(contador)

# percorrendo lista[]
lista_str = ["ellie", "LEW", "cu", "cUnDa", "fred", "CrysCrys"]

for item in lista_str:
    print(item)