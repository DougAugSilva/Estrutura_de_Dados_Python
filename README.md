# P.O.O com Vetores Ordenados e <br/> Não Ordenados em Python

## Introdução
Este repositório segue de notas das aulas do curso *Estrutura de Dados e Algoritmos em Python*, e tem como objetivo expor os conteudos nele apresentados, visando assim servir de guia para futuros projetos e de exemplo de aplicação do conteudo abordado no curso. No curso são vistas as pricipais estruturas de dados presentes na linguagem de programação Python, sendo estas:
- Vetores ordenados e não ordenados
- Pilhas, filas e deques
- Listas encadeadas
- Árvores
- Grafos
  
Também serão vistos algoritmos de criação e manipulação destas estruras de dados, bem como o básico de programção orientada a objetos e *big O notation* para a avaliação do comportamento assintótico dos algoritmos.

## Vetores Não Ordenados

### Teoria
Vetores não ordenados são uma estrutura de dados que armazena dados sem uma ordem específica, um vetor não ordenado possui caracteristicas particuylares com relação a sua construção e manipulação:
- Se o vetor permite elementos repetidos, um algoritmo de inserção realizará um único passa para adicionar um novo valor ao vetor, possuindo asssim *O(1)*.
- Ainda, se permitirmos elementos repetidos no vetor, um algoritmo de busca deverá checara as n entradas do vetor antes de retornar o valor, possuindo assim *O(n)*.
- Se o vetor *não* permnite elementos repetidos, o algoritmo deverá veririficar elemento a elemento do vetor antes de inserir um novo elemnto, possuindo assim *O(n)*, com n o número de elementos do vetor.
- Ao apagar um elemnto na n-esima popsição do vetor, os novos elementios deverão ser rearranjados da poisição *i* para *i-1* a patir do valor *i = n+1*.

Tais aspectos ficarão mais evidentes nas aplicações em Python.

### Definido a Classe e o Objeto
Primeiro vamos importar a biblioteca *numpy* para podermos defeirni mais facilmente o vetor. Começamos definidno a classe na qual o objeto `VetorNaoOrdenado` irá fazer parte, com isso podemos adicionar a capacidade do vetor, definir um ponteiro para a leitura de seus dados e os valores em suas entradas, neste exemplo vamos defeinir somente valores do tipo `int` para as entradas.
```python
import numpy as np   #importa a biblioteca numpy

class VetorNaoOrdenado:  #define a classe de vetor não ordenado
    def __init__(self, capacidade):  
        self.capacidade = capacidade  #capacidade de armazenamento do vetor
        self.ultima_posicao = -1  #define o ponteiro de leitura das entradas do vetor
        self.valores = np.empty(self.capacidade, dtype = int)  #define os tipos de entradas do vetor

vetor = VetorNaoOrdenado(5)  #exemplo: definindo um vetor com 5 entradas
```
### Função de Inserção
A primeira função que vamos definir para trabalha com o nosso vetor é a inserção, com elas podemos inserir novos valores ao vetor, neste caso a ordem de inserção não importa, sendo assim mais simples quie a função de inserção no case dos vetores ordenados. 
```python
def insere(self, valor): #definindo a função
        if self.ultima_posicao == self.capacidade -1:
            print("Capacidade máxima atingida") #caso o vetor esteja coimpleto
        else:
            self.ultima_posicao +=1  #move o ponteiro nas entradas do vetor
            self.valores[self.ultima_posicao] = valor
```
Note que inclui um detector caso o vetor esteja com todas as suas entradas já preenchidas com valores. Deste modo, para inserirmos o número 5 agora por exemplo, basta digitarmos `vetor.insere(5)`.

### Função de Impressão
Criado o vetor e inserido valores em suas entradas, podemos definir uma função para retornar estes valores, será adiconada uma mensagem caso o vetor se encontre "vazio", isto é, sem dados em suas entradas.
```python
def imprime(self):   #definindo função 
        if self.ultima_posicao == -1:   #caso o ponteiro permaneça na posição inicial, o vetor esta vazio
            print("O vetor está sem dados")
        else:     #caso contrario imprime as entradas do vetor
            for i in range(self.ultima_posicao +1):
                print(i, "-" , self.valores[i])

```
### Função de Pesquisa
Esta é a função mais custosa no sentido computacional, dado que não existe uma ordem explicita na organização dos elementos do vetor, a unica forma de pesquisa que podemos aplicar é a *pesquisa linear*, sendo preciso checar entrada a entrada do vetor para encontrar o item a ser pesquisado, e ainda, caso seja permitido itens repetidos no vetor, a pesquisa deve percorrer **Todas** as entradas do vetor. Definimos esta função pelo comando abaixo:
```python
def pesquisar(self, valor): #definindo a função 
      for i in range(self.ultima_posicao + 1): #define a posição inicial do ponteiro de leitura do vetor
        if valor == self.valores[i]:
           return i  #caso o elemento exista ele retorna o elemento
      return -1  #caso o elemento não exista no vetor
```
neste exemplo do vetor com entradas sendo números inteiros positvos, temos que caso o item pesquisado não esteja presente no vetor, retornamos o valor negatio -1, o motico pelo qual foi escolhido -1 no lugar de uma string dizendo `"valor não encontrado"` ficará mais evidente adiante.

### Função de Exclusão
Definida a função de pesquisa, podemos utilizar ela para remover um item de uma dada entrada do vetor, esta entrada não pode ficar "vazia" após a remoção, sendo assim precisasmos rearranjar os elementos do vetor movendo um a auma a paertir desta entrada, e depois decrementar o tamnaho do vetor. O algoritmo que implementa estra função segue abaixo:
```python
def excluir(self, valor): #definindo função
      posicao = self.pesquisar(valor) #primeiro pesquisamos o item a ser excluido no vetor
      if posicao == -1: #caso o item não exista, retorna o valor -1
        return -1
      else: #caso o item exista, exclui o item e remanja os demais
        for i in range(posicao, self.ultima_posicao):
          self.valores[i] = self.valores[i + 1]
```
Aqui vemos o por que se faz útil a atribuição do -1 na pesquisa caso o elemnto não exista no vetor, ele aparece no primeiro `if` da função excluir. <br/>
Com isso, para excluirmo o número 5 que foi anterioirmente adicionado, basta fazermos `vetor.excluir(5)`.

## Vetores Ordenados
Vetores ordenados são semelhantes aos Não Ordenados, porem agora os dados são armazenados em uma ordem específica pré definida, possuindo assim carateristicas particulares quanto a sua manipulação:
- Toda vez que formos inserir um item no vetor, precisaremos fazer uma pesquisa sobre os demais itens para ainserção respeitar a ordenação do vetor.
- O algoritmo de pesquisa não precisa necessariamente fazer a leitura de todas as entradas do vetor em todos os casos, basta ele chegar no primeiro item maior que o item a ser pesquisado.
- A parte do remanejamento do algoritmo de exclusão é igual ao do vetor não ordenado.

Novamente vamos definir e implementar os algoritmos de manipulação dessa estrutura de dados.

### Definido a Classe e o Objeto

Para o *Vetor Ordenado*, definimos sua classe e função de impressão da mesma forma que para o *Vetor Não Ordenado*, com efeito, a diferença entre eles não se dá na definição de sua classe, nem na criação do objeto, mas sim no algoritmo de inserção de valores em suas entradas, com isso segue sua criação.
```python
import numpy as np

#criando a classe do vetor
class VetorOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype = int)

#definindo sua função de impressão
  def imprime(self):
    if self.ultima_posicao == -1:
      print("O vetor está sem dados")
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, "-", self.valores[i])

vetor = VetorOrdenado(5)  #exemplo: Criando um vetor de 5 entradas
```

### Função de Inserção
Esta é a função mais complexa até agora, como dito anteriormente, é ela que diferencia entre os dois tipos de vetores. Sua complexidade se dá pelo fato de que não podemos inserir um novo valor de qualquer maneira em um vetor ordenado, somente rearranjando os itens para liberar espaço como no caso do não ordenado, a medida que adicionamos novos itens precisasmos respeitar a ordenação vigente, sendo esta crescente, decrescente ou alfabétioca casop trabalhemos com strings. <br/>
Para este exemplo com entradas sendo inteiros positivos, vamos trabalhar com a ordenação na forma crescente, o algoritmo será exposto e posteriormente explicado suas nuancias.
```python
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
```
O algoritmo de inserção se divide em quatro partes:
1. A primeira parte é análoga ao caso do vetor não ordenado, primeiro é verificado se é possível se inserir mais itens ao veto, ou ele está com daados em todas as suas entradas.
2. Depois setamos o ponteiro do vetor para a posição inicial, verificamos item a item, até encontrarmos um elemento maior que o valor que queremos inserir, encontrado este elemento, uma posição antes dele é a posição a inserirmos o nosso valor.
3. Encontrada a posição ao qual o valor será inserido, definimos uma variavel x que vai rerarranjar os itens do vetor da última posição até a posição que vamos inserir, para assim a torna-la diponível para a atribuição do valor.
4. Feito isso, atribuimos o valor a posição e acrescemos de uma unidade o tamanho do vetor.

Caso ainda restem duvidas, recomento o debug para a execução do algoritmo passo a passo pelo compilador.

### Funções de Pesquisa

A grande vantagem de inserir uma relação de ordem na organização dos valores presenmtes na entradas de um vetor, é a facilidade da execução de buscas, na parte de comparação se tornará mais evidente a diferença, mas adiantando, vetores ordenados são recomendados em casos em que há muitas buscas por dados dentro do sistema, mas pouca inserção de novos dados. <br/>
Para este tipo de vetor temos dois algoritmos de pesquisa, um semelhante oa visto para vetores não ordenados denominado *Pesquisa Linear*, e outro que se aproveita da ordenação dos elementos para uma maior eficiência computacional, chamado de *Pesquisa Binária*, amobos serão abordados agora.

#### Pesquisa Linear
A principal diferença neste tipo de pesquisa para vetores ordenados, é que não há necessidade de se verificar todas as entradas do vetor, mesmo para o caso em que são aceitos valores repetidos, pois caso cheguemos a um item maior que o valor buscado, a relação de ordem entre os elementos garante que não havera mais valores iguais a este nas posições seguintes do vetor.
```python
def pesquisa_linear(self, valor):
     for i in range(self.ultima_posicao + 1):
      if self.valores[i] > valor: 
        return -1
      if self.valores[i] == valor: 
        return i
      if i == self.ultima_posicao:
        return -1   
```
#### Pesquisa Binária
