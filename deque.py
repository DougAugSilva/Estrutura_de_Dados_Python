import numpy as np

class Deque:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.inicio = -1
    self.final = 0
    self.numero_elementos = 0
    self.valores = np.empty(self.capacidade, dtype = int)

  def __deque_cheio(self):
    return (self.inicio == 0 and self.final == self.capacidade - 1) or (self.inicio == self.final + 1)

  def __deque_vazio(self):
    return self.inicio == -1

#Funçãoes de inserção
  #defina a função que insere valores no inicio do deque
  def insere_inicio(self, valor):
    if self.__deque_cheio():
      print("O deque está cheio")
      return
    #caso o deque esteja vazio
    if self.inicio == -1:
      self.inicio = 0
      self.final = 0
    #caso o início esteja na primeira posição
    elif self.inicio == 0:
      self.inicio = self.capacidade - 1
    #caso não
    else:
      self.inicio -= 1
    self.valores[self.inicio] = valor

  #defina a função que insere valores no final do deque
  def insere_final(self, valor):
    if self.__deque_cheio():
      print("O deque está cheio")
      return
    #caso o deque esteja vazio
    if self.inicio == -1:
      self.inicio = 0
      self.final = 0
    #caso o dinal esteja na última posição
    elif self.final == self.capacidade - 1:
      self.final = 0
    else:
      self.final += 1
    self.valores[self.inicio] = valor

#Funções de exclusão

  #define a função que exclui um valor no início
  def excluir_inicio(self):
    if self.__deque_vazio():
      print("O deque já está vazio")
      return
    #caso possua somente um elemnto no deque
    if self.inicio == self.final:
      self.inicio = -1
      self.final = -1
    else:
      #volta para a posição inicial
      if self.inicio == self.capacidade - 1:
        self.inicio = 0
      else:
        #vamos incrementar o novo início para removermos o início atual
        self.inicio += 1

  #define a função que exclui o final do deque
  def excluir_final(self):
    if self.__deque_vazio():
      print("O deque já está vazio")
      return
    #caso possua somente um elemento
    if self.inicio == self.final:
      self.inicio = -1
      self.final = -1
    else:
      #volta para a posição final
      if self.inicio == 0:
        self.final = self.capacidade - 1
      else:
        #vamos decrementar o novo final para removermos o final atual
        self.final -= 1

#Funções de impressão
  #nos retorna o valor no início do deque
  def get_inicio(self):
    if self.__deque_vazio():
      print("O deque está vazio")
      return
    return self.valores[self.inicio]   

  #nos retorna o valor no final do deque
  def get_final(self): 
    if self.__deque_vazio() or self.final < 0: #uma condição a mais por segurança
      print("O deque está vazio")
      return
    return self.valores[self.final]