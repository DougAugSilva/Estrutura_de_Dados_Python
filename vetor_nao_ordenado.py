import numpy as np   #importa a biblioteca numpy

class VetorNaoOrdenado:  #define a classe de vetor não ordenado
    def __init__(self, capacidade):  
        self.capacidade = capacidade  #capacidade de armazenamento do vetor
        self.ultima_posicao = -1  #define o ponteiro de leitura das entradas do vetor
        self.valores = np.empty(self.capacidade, dtype = int)  #define os tipos de entradas do veto

    def insere(self, valor): #definindo a função
            if self.ultima_posicao == self.capacidade -1:
                print("Capacidade máxima atingida") #caso o vetor esteja coimpleto
            else:
                self.ultima_posicao +=1  #move o ponteiro nas entradas do vetor
                self.valores[self.ultima_posicao] = valor

    def imprime(self):   #definindo função 
        if self.ultima_posicao == -1:   #caso o ponteiro permaneça na posição inicial, o vetor esta vazio
            print("O vetor está sem dados")
        else:     #caso contrario imprime as entradas do vetor
            for i in range(self.ultima_posicao +1):
                print(i, "-" , self.valores[i])
    
    def pesquisar(self, valor): #definindo a função 
      for i in range(self.ultima_posicao + 1): #define a posição inicial do ponteiro de leitura do vetor
        if valor == self.valores[i]:
           return i  #caso o elemento exista ele retorna o elemento
      return -1  #caso o elemento não exista no vetor
    
    def excluir(self, valor): #definindo função
      posicao = self.pesquisar(valor) #primeiro pesquisamos o item a ser excluido no vetor
      if posicao == -1: #caso o item não exista, retorna o valor -1
        return -1
      else: #caso o item exista, exclui o item e remanja os demais
        for i in range(posicao, self.ultima_posicao):
          self.valores[i] = self.valores[i + 1]
#testando funções
vetor = VetorNaoOrdenado(5)

vetor.insere(5)
vetor.insere(9)
vetor.insere(2)
vetor.insere(8)
vetor.insere(1)
vetor.imprime()

vetor.excluir(5)
vetor.imprime()

vetor.pesquisar(8)

