"""
Chegou a hora de criar a sua primeira classe, a classe Conta. Para tal, crie o arquivo conta.py e siga os passos abaixo:

1 - Defina a classe, utilizando a palavra-chave class, e em seguida defina o seu nome.

2 - Defina a função construtora da classe, recebendo uma referência do próprio objeto como argumento.

3 - Receba também como argumento os valores dos atributos da classe, isto é, numero, titular, saldo e limite.

4 - Através da referência do objeto, defina os atributos numero, titular, saldo e limite com os respectivos valores
recebidos como argumento.


Para transferir um valor de uma conta para outra, crie o método transfere, que recebe como argumento uma referência
do próprio objeto, o valor a ser transferido, e a conta de destino. Esse método sacará o valor da conta atual e o
depositará na conta de destino.

### Verificando o saque ### Então, crie o método pode_sacar, que recebe o valor a ser sacado por argumento e verifica
se há dinheiro suficiente na conta para o saque ser realizado, isto é, o valor do saque tem que ser menor ou igual ao
saldo mais o limite da conta.

E no método saca, faça um if para verificar se realmente o valor pode ser sacado da conta, se sim, o saque é feito,
se não, imprima uma mensagem externando que o valor passou o limite.

Por fim, como o método pode_sacar foi criado apenas para uma verificação interna, não faz sentido ele ser utilizado
fora da classe, então torne-o privado.


Métodos estáticos Estamos criando contas de um único banco, o Banco do Brasil, que possui um código, o 001. Como esse
código independe da conta, faz sentido acessá-lo sem termos um objeto da classe Conta.

Para isso, crie o método estático codigo_banco, que retorna o código do banco. E crie também o método estático
codigos_bancos, que retorna um dicionário com os códigos dos bancos BB, Caixa e Bradesco, que são 001, 104 e 237,
respectivamente.
"""


class Conta:
    # atributo estatico
    coisa_favorita = "cu"

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def extrato(self):
        print(f"{self.__titular} seu saldo é: {self.__saldo}")

    def deposito(self, valor):
        self.__saldo += valor

    def __pode_vazar(self, valor):
        return valor <= self.saldo + self.limite

    def saque(self, valor):
        if self.__pode_vazar(valor):
            self.__saldo -= valor
        else:
            print('tu é pobre bro!')

    def transferir(self, valor, destino):
        if self.__pode_vazar(valor):
            print(f"enviando R${valor} para a conta de: {destino.titular}")
            self.saque(valor)
            destino.deposito(valor)
        else:
            print("tu é probre 'bro!")

    @staticmethod
    def fala_cu():
        print("cu²")
