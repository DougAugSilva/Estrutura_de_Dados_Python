import numpy as np

class FilaPrioridade:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.numero_elementos = 0
    self.valores = np.empty(self.capacidade, dtype = int)

  def __fila_vazia(self):
    return self.numero_elementos == 0

  def __fila_cheia(self):
    return self.numero_elementos == self.capacidade
  
  def primeiro(self):
    if self.__fila_vazia():
      return -1
    return self.valores[self.numero_elementos -1]
  
  #criando a função de enfileirar para filas de prioridade, aqui a prioridade é para números menores
  def enfileirar(self, valor):
    if self.__fila_cheia():  #caso a fila esteja cheia
      print("A fila está cheia")
      return
    if self.numero_elementos == 0:  #caso a fila esteja vazia
      self.valores[self.numero_elementos] = valor
      self.numero_elementos += 1
    else:  #caso a fila não esteja vazia
      x = self.numero_elementos -1  #criamos a varialvel x para ser o ponteiro de remanejarmos os elementos
      while x >= 0:  #enquanto o ponteiro não ficar na primeira posição
        if valor > self.valores[x]:  #caso o valor inserido seja maior que o valor na posição x
          self.valores[x + 1] = self.valores[x]  #realizamos o remanejamento
        else:  #caso contrário, podemos parar o código
          break
        x -=1  #depois decrementamos o valor de x
      self.valores[x + 1] = valor  #inserimos a valor na devida posição  
      self.numero_elementos += 1  #aumentamos o número de elementos da fila
  
  #função desenfileirar
  def desenfileirar(self):
    if self.__fila_vazia():  #caso a fila esteja vazia
      print("A fila está vazia")
      return
    valor = self.valores[self.numero_elementos -1] 
    self.numero_elementos -= 1 
    return valor  #caso contrário, remove o primeiro elemento da fila e o retorna