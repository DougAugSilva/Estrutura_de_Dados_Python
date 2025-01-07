import numpy as np
#quando colocamos __ antes de um atributo ou função, o usuário não tem acesso a ele
class Pilha:  #define a classe
  def __init__(self, capacidade):
    self.__capacidade = capacidade  #define a capacidade da pilha
    self.__topo = -1  #define o topo da pilha
    self.__valores = np.empty(self.__capacidade, dtype = int)  #pilha com dados inteiros

  #função para verificar se a pilha está cheia
  def __pilha_cheia(self):  #como o usuario não precisa ter acesso a essa função, colocasmos "__" antes dela
    if self.__topo == self.__capacidade - 1:
      return True
    else:
      return False
  #função que verifica se a pilha está vazia
  def __pilha_vazia(self):
    if self.__topo == -1:
      return True
    else:
      return False
  #definifno função de empilhar
  def empilhar(self, valor):
    if self.__pilha_cheia():
      print("A pilha está cheia")
    else:
      self.__topo += 1
      self.__valores[self.__topo] = valor
  #definindo a função de desempilhar
  def desempilhar(self):
    if self.__pilha_vazia():
      print("A pilha está vazia")
    else:
      self.__topo -= 1
  #definindo função de leitura do valor no topo da pilha
  def ver_topo(self):
    if self.__topo != -1:
      return self.__valores[self.__topo]
    else:
      return -1