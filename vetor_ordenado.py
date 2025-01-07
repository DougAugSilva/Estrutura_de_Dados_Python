import numpy as np

#criando a classe do vetor
class VetorOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype = int)

  def imprime(self):
    if self.ultima_posicao == -1:
      print("O vetor está sem dados")
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, "-", self.valores[i])

  def insere(self, valor):   #esta parte do código é semelhante a do vetor não ordenado
    if self.ultima_posicao == self.capacidade-1:
      print("Capacidade máxima atingida")
      return
    posicao = 0      #seta o ponteiro para a posição inicial
    for i in range(self.ultima_posicao + 1):  #avança nas posições do vetor
      posicao = i
      if self.valores[i] > valor:
        break       #caso o item na posição i seja maior que o valor, paramos o algoritmo
      if i == self.ultima_posicao:   #Caso o ponteiro do vetor chegue ao último elemnto, aumentamos o tamanho do vetor
        posicao = i + 1
    #Agora precisasmos ir a última posição do vetor para remanejar os elementos do vetor
    x = self.ultima_posicao
    while x >= posicao:   #enquanto x for maior que a item a ser buscado, temos o remanejamento
      self.valores[x + 1] = self.valores[x]
      x -= 1
    #Remanejados os valores, vamos inserir o novo valor e incrementar o tamanho do vetor
    self.valores[posicao] = valor
    self.ultima_posicao += 1

  def pesquisa_linear(self, valor):
     for i in range(self.ultima_posicao + 1):
      if self.valores[i] > valor: 
        return -1
      if self.valores[i] == valor: 
        return i
      if i == self.ultima_posicao:
        return -1   
      
  def pesquisa_binaria(self, valor):
    limite_inferior = 0
    limite_superior = self.ultima_posicao
    while True:
      posicao_atual = int((limite_inferior + limite_superior) / 2)
      #caso o valor foi encontrado na primeira tentativa
      if self.valores[posicao_atual] == valor:
        return posicao_atual
      #caso o valor não foi encontrado na primeira tentativa e temos
      elif limite_inferior > limite_superior:
        return -1
      #caso nenhuma das condiçoies acima, vamos escolher quais intervalos ele faz parte
      else:
        if self.valores[posicao_atual] < valor: #caso intervalo da direita
          limite_inferior = posicao_atual +1
        else: #caso intervalo da esquerda
          limite_superior = posicao_atual - 1
        
  def excluir(self,valor):
    posicao = self.pesquisar_binaria(valor)
    if posicao == -1:
      return -1  #caso o item não exista no vetor, retorna -1 
    else:
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i +1]  #caso exista, realiza o remanejamento dos valores
      self.ultima_posicao -= 1   #decrementa o valor das posições (diminui o tamanho do vetor)
