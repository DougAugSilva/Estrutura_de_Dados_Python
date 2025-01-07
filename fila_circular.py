import numpy as np

class FilaCircular:
  def __init__(self,capacidade):
    self.capacidade = capacidade
    self.inicio = 0  #seta o ponetiro de leitura do início
    self.final = -1  #seta o ponteiro de leitura do final
    self.numero_elementos = 0
    self. valores = np.empty(self.capacidade, dtype = int) #cria o vetor do tipo np array com entradas inteiras

 #função que verifica se a fila está vazia
  def __fila_vazia(self):
    return self.numero_elementos == 0  #se o número de elementos for 0, a fila está vazia

 #função que verifica se a fila está cheia
  def __fila_cheia(self):
    return self.numero_elementos == self.capacidade

  #funçao que adiciona elementos na fila
  def enfileirar(self, valor):
    if self.__fila_cheia():  #caso a fila esteja cheia
      print("A fila está cheia")  #retorna que a fila está cheia e não adiciona mais elementos
      return
    if self.final == self.capacidade -1: #caso o ponteiro do final da fila tenha chegado no último elemento
      self.final = -1  #direcionanmos ele para começar no início da fila antes da posição inicial
    self.final += 1  #depois setamos ele para a o inicio da fila na posição 0
    self.valores[self.final] = valor  #depois o final da fila recebe op valor desejado
    self.numero_elementos += 1  #depois incrementamos o número de elementos da fila

  #função que retira elementos da fila
  def desenfileirar(self):
    if self.__fila_vazia():  #caso a fila não tenha elementos para retiramos
      print("A fila já está vazia")  #retorna que a fila está vazia
      return
    temp = self.valores[self.inicio]  #atribuimos a tem qual elemento foi desenfileirado (sempre o elemento do início)
    self.inicio += 1  #depois de adicionarmo um elemento trocamos o ponteiro de posição inicial da fila
    if self.inicio == self.capacidade -1:  #caso o ponteiro do inicio da fila chegou ao final da fila
       self.inicio = 0  #retornamos o ponteiro para o início da fila
    self.numero_elementos -= 1  #diminuimos o núumero de elementos da fila
    return temp  #nos retorna o valor que foi retirado da fila

  #função que retorna o primeiro valor da fila
  def primeiro(self):
    if self.__fila_vazia(): #caso a fila esteja vazia nos retorna o valor -1
      return -1
    return self.valores[self.inicio]  #caso contrário nos retorna o valor no início da fila