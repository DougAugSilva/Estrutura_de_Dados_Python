# Peincipais Estruturas de Dados em Python
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

### Definido a Classe
Primeiro vamos importar a biblioteca *numpy* para podermos defeirni mais facilmente o vetor. Começamos definidno a classe na qual o objeto `VetorNaoOrdenado` irá fazer parte, com isso podemos adicionar a capacidade do vetor, definir um ponteiro para a leitura de seus dados e os valores em suas entradas, neste exemplo vamos defeinir somente valores do tipo `int` para as entradas.
```python
import numpy as np   #importa a biblioteca numpy

class VetorNaoOrdenado:  #define a classe de vetor não ordenado
    def __init__(self, capacidade):  
        self.capacidade = capacidade  #capacidade de armazenamento do vetor
        self.ultima_posicao = -1  #define o ponteiro de leitura das entradas do vetor
        self.valores = np.empty(self.capacidade, dtype = int)  #define os tipos de entradas do vetor
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

### Função de Pesquisa
Esta é a função mais custosa no sentido computacional, dado que não existe uma ordem explicita na organização dos elementos do vetor, a unica forma de pesquisa que podemos aplicar é a *pesquisa linear*, sendo preciso checar entrada a entrada do vetor para encontrar o item a ser pesquisado, e ainda, caso seja permitido itens repetidos no vetor, a pesquisa deve percorrer **Todas** as entradas do vetor. Definimos esta função pelo comando abaixo:
```python
def pesquisar(self, valor): #definindo a função 
      for i in range(self.ultima_posicao + 1): #define a posição inicial do ponteior de leitura do vetor
        if valor == self.valores[i]:
           return i  #caso o elemento exista ele retorna o elemento
      return -1  #caso o elemento não exista no vetor
```
neste exemplo do vetor com entradas sendo números inteiros positvos, temos que caso o item pesquisado não esteja presente no vetor, retornamos o valor negatio -1, o motico pelo qual foi escolhido -1 no lugar de uma string dizendo `"valor não encontrado"` ficará mais evidente adiante.

##Função de Exclusão

## Vetores Ordenados
Vetores ordenados são semelhantes aos Não Ordenados, porem agora os dados são armazenados em uma ordem específica pré definida, possuindo assim carateristicas particulares quanto a sua manipulação:
- Toda vez que formos inserir um item no vetor, precisaremos fazer uma pesquisa sobre os demais itens para ainserção respeitar a ordenação do vetor.
- O algoritmo de pesquisa não precisa necessariamente fazer a leitura de todas as entradas do vetor em todos os casos, basta ele chegar no primeiro item maior que o item a ser pesquisado.
- A parte do remanejamento do algoritmo de exclusão é igual ao do vetor não ordenado.

Novamente vamos definir e implementar os algoritmos de manipulação dessa estrutura de dados.

### Definido a Classe






