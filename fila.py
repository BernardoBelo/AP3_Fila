from no import No

class Fila:
    def __init__(self):
        self.cabeca = None
        self._tamanho = 0

    def enfileirar(self, elemento):
        if self.cabeca:
            ponteiro = self.cabeca
            while(ponteiro.proximo):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = No(elemento)
        else:
            self.cabeca = No(elemento)
        self._tamanho = self._tamanho + 1

    def __len__(self):
        return self._tamanho

    def _getnode(self, indice):
        ponteiro = self.cabeca
        for i in range(indice):
            if ponteiro:
                ponteiro = ponteiro.proximo
            else:
                raise IndexError("Índice da fila fora de alcance")
        return ponteiro

    def __getitem__(self, indice):
        ponteiro = self._getnode(indice)
        if ponteiro:
            return ponteiro.dado
        else:
            raise IndexError("Índice da fila fora de alcance")

    def __setitem__(self, indice, elemento):
        ponteiro = self._getnode(indice)
        if ponteiro:
            ponteiro.dado = elemento
        else:
            raise IndexError("Índice da fila fora de alcance")
    
    def indice(self, elemento):
        ponteiro = self.cabeca
        i = 0
        while(ponteiro):
            if ponteiro.dado == elemento:
                return i
            ponteiro = ponteiro.proximo
            i = i + 1
        raise ValueError("{} não está na fila".format(elemento))

    def inserir(self, indice, elemento):
        no = No(elemento)
        if indice == 0:
            no.proximo = self.cabeca
            self.cabeca = no
        else:
            ponteiro = self._getnode(indice - 1)
            no.proximo = ponteiro.proximo
            ponteiro.proximo = no
        self._tamanho = self._tamanho + 1

    def desenfileirar(self):
        if self._tamanho > 0:
            elemento = self.cabeca.dado
            self.cabeca = self.cabeca.proximo
            self._tamanho = self._tamanho - 1
            return elemento
        
        raise IndexError("A fila está vazia!")

    def remover(self, elemento):
        if self.cabeca == None:
            raise ValueError("{} não está na fila".format(elemento))
        elif self.cabeca.dado == elemento:
            self.cabeca = self.cabeca.proximo
            self._tamanho = self._tamanho - 1
            return True
        else:
            ancestor = self.cabeca
            ponteiro = self.cabeca.proximo
            while(ponteiro):
                if ponteiro.dado == elemento:
                    ancestor.proximo = ponteiro.proximo
                    ponteiro.proximo = None
                ancestor = ponteiro
                ponteiro = ponteiro.proximo
            self._tamanho = self._tamanho - 1
            return True
        raise ValueError("{} não está na fila".format(elemento))
                 
    def __repr__(self):
        r = ""
        ponteiro = self.cabeca
        while(ponteiro):
            r = r + str(ponteiro.dado) + " - "
            ponteiro = ponteiro.proximo
        return r
    
    def __str__(self):
        return self.__repr__()




"""



/// Ao Iniciar o terminal digite o código abaixo para poder iniciar o Python

    python

/// Utilize o código abaixo para poder iniciar a classe Fila do arquivo fila.py:

    from fila import Fila

/// Crie uma fila com um nome qualquer e em seguida inicie a classe:

    nomeDaFila = Fila()

/// Para saber a quantidade de elementos presentes na fila, informe o código abaixo:
    
    len(nomeDaFila)

/// Para saber quais elementos e ordem que a fila se encontra digite o código abaixo:

    nomeDaFila

/// Para enfileirar um número na fila utilize o código abaixo:

    nomeDaFila.enfileirar(valor)

/// Para desenfileirar o primeiro número da fila utilize o código abaixo:

    nomeDaFila.desenfileirar()

/// Para inserir um número em uma posição especifica da fila, utilize o código abaixo:

    nomeDaFila.inserir(posição, valor)

/// Pare remover um número em específico da fila, utilize o código abaixo:

    nomeDaFila.remove(valor)



"""

















