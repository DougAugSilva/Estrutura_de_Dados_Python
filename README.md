# Estruturas de Dados e P.O.O com Python
#### Douglas Augusto da Silva
[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dougaugsilva/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DougAugSilva)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:douglasaugustosilva323@gmail.com)

## Introdução
Este repositório segue de notas das aulas do curso *Estrutura de Dados e Algoritmos em Python*, e tem como objetivo expor os conteudos nele apresentados, visando assim servir de guia para futuros projetos e de exemplo de aplicação do conteudo abordado no curso. No curso são vistas as pricipais estruturas de dados presentes na linguagem de programação Python, sendo estas:

- [Vetores Não Ordenados](#Vetores-Não-Ordenados)
- [Vetores Ordenados](#Vetores-Ordenados)
- [Pilhas](#Pilhas)
- [Filas Circulares](#Filas-Circulares)
- [Filas de Prioridade](#Filas-de-Prioridade)
- [Deques](#Deques)
- [Listas Encadeadas](#Listas-Encadeadas)
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
[voltar ao topo](https://github.com/DougAugSilva/Estrutura_de_Dados_Python?tab=readme-ov-file#introdu%C3%A7%C3%A3o)
### Teoria
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
Esta é a função mais complexa até agora. Sua complexidade se dá pelo fato de que não podemos inserir um novo valor de qualquer maneira em um vetor ordenado, a medida que adicionamos novos itens precisasmos respeitar a ordenação vigente, sendo esta crescente, decrescente ou alfabética caso trabalhemos com strings. <br/>
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
A grande vantagem de inserir uma relação de ordem na organização dos valores presenmtes na entradas de um vetor, é a facilidade da execução de buscas, na parte de comparação se tornará mais evidente essa diferença.  <br/>
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
A *pesquisa binária* é exclusica dos vetores ordenados, ela se aproveita da ordenação para gradativamente ir reduzindo o iontervalo de busca pela mentade, podendo assim realizar a busca de um elemento com muito mais eficiciencia do ponto de vista computacional. Implementamos ela atravéz do seguinte algoritmo:
```python
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
```
Novamente, podemos analisar esta função em quatro partes:
1. Primeiro definimos os extremos do intervalo de pesquisa e verificamos se o valor da pesquisa é igual, maior ou menor a média deste intervalo. Sendo que caso o valor seja igual a média, paramos a pesquisa.
2. Caso o valor seja *maior* que a média do intervalo, restringimos o intervalo de pesquisa atualizando os limites do intervalo de busca, com o novo intervalo inferior sendo a máedia dos intervlaos
3. Caso o valor seja *menor* que a média dos intervalos, rrestringimos o intervalo de pesquisa atualizando agora o limite superior como senod a média dos intervalos
4. Respetimos o processo até isolarmos nosso valor em intervalos cada vez menores, até que a média do intervalo coincida com ele.

### Função de Exclusão
Dado que a função de exlcusão depende de uma função de pesquisa, podemos criar uma função de exclusão com a pesquisa linear e outra com a pesquisa binária. para este exemplo foi escolhida com a pesquias binária, mas basta substituirmos no algoritmo `pesquisa_binária(..)` por `pesquisa_linear(...)` para mudarmos de uma para a outra, sendo que a com pesquisa binária será computacionalmente mais eficiente.
```python
def excluir(self,valor):
    posicao = self.pesquisar_binaria(valor)
    if posicao == -1:
      return -1  #caso o item não exista no vetor, retorna -1 
    else:
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i +1]  #caso exista, realiza o remanejamento dos valores
      self.ultima_posicao -= 1   #decrementa o valor das posições (diminui o tamanho do vetor)
```
### Comparando Vetores Ordenados e Não Ordenados
Estas estrurturas e dados embora semelhantes, possuem suas devidas recomendações para tipos específicos de aplicações, em resunmo temos que: 
- Vetores **não ordenados** são mais recomendados para aplicações em que temos muitas inserções de novos dados no sistemas, mas poucas buscas. Por exemplo o cadastro de preço de itens em um sistema de um supermercado.
- Vetordes **ordenaos** são recomendados para aplicações onde temos muitas buscas nos sistemas, mas pouca inserção de novos dados, por exemplo um banco de dados com cadastros de novos funcionários.

Outra diferença importante entre estes vetores é a presença da pesquis binária para o caso de vetores ordenados, já foi dito que esta é mais eficiente que a linear, mas o quanto mais eficiente? A tabela abaixo deixa mais notavel a diferença.

| Faixa de Busca | Busca Binária | Busca Linear |
|----------------|---------------|--------------|
| 10             | 4             | 5            |
| 100            | 7             | 50           |
| 1.000          | 10            | 500          |
| 10.000         | 14            | 5.000        |
| 100.000        | 17            | 50.000       |
| 1.000.000      | 20            | 500.000      |
| 10.000.000     | 24            | 5.000.000    |
| 100.000.000    | 27            | 50.000.000   |
| 1.000.000.000  | 30            | 500.000.000  |

A tabele acima mostra o número de passos de cada algortimo em ralação ao compriemnto do vetor, sendo que a busca linear realiza em média *n/2* passos em um vetor com *n* entradas. Note que fica evidente que para a pesquisa binária temos *O(ln)*, equanto para a pesquisa linear *O(n)*, sendo este o principal motivo por se investir tantos recursos no desenvolvimento de algoritmos ordenação de banco de dados, a grande eficiencia na busca de valores.

## Pilhas
[voltar ao topo](https://github.com/DougAugSilva/Estrutura_de_Dados_Python?tab=readme-ov-file#introdu%C3%A7%C3%A3o)
### Teoria
Pilhas são um aestruturas de dados com um acesso diferente aos seu itnes, ele permite acesso somente ao último item inserido, sendo necessário remover este para aacessar o próximo item (no caso o penultimo item inserido), e asssim por diante. Existem várias aplicações que são utilizads pilhas, como por exemplo:
- Correeção de expreções aritméticas
- Pesquisa nos vértices de um gráfo
- Percorrimento de uma árvore binária
- Arquitetura de microprocessadores

As operações que podemos realizar na manipulação de pilhas que serão abordadas aqui são:
- **Empilhar:** Colocar um item de dados mo topo da pilha
- **Desempuilhar:** Remover um item de dados do topo da pilha
- **Ver o Topo:** Mostar o elemento que está no topo da pilha.

Uma pilha é uma estrutura de dados do tipo *LIFO* (Last in First Out), isto é, O último elemento a ser inserido é o primeiro a elemnto a ser retirado.

### Definido a Classe e o Objeto
Primeiro vamos definir a classe e o objeto, para isso será uilizado novamente o pacote *numpy*. Assim como no caso dos vetores, as entradas serão definidas como inteiros positivos.
```python
import numpy as np

class Pilha:  #define a classe
  def __init__(self, capacidade):
    self.__capacidade = capacidade  #define a capacidade da pilha
    self.__topo = -1  #define o topo da pilha
    self.__valores = np.empty(self.__capacidade, dtype = int)  #pilha com dados inteiros
```
Como algumas não há a necessidade do usuario ter acessoa a algumas funções, colocamos "__" antes da definição para restringir seu acesso pelo usuário.

### Funções de Verificação
Será de grande utilidade ter informações sobre como se encontra a capácidade de armazenamento da pilha, para assim sabermops se ainda é possivel adicionar maisa itens ou realizar certas operações. Dado que estas funções servirão de base para criação de outras posteriormente, o usuario não precisa ter acesso direto a elas, com isso em ambas será adicionado "__" para restringir seu acesso.

#### Função Pilha Cheia
Esta nos diz se ainda é possivel adicionarmos elementos na pilha, verificando se ainda existem posiçõs sem valores atribuidos.
```python
  def __pilha_cheia(self): 
    if self.__topo == self.__capacidade - 1:
      return True
    else:
      return False
```
#### Função Pilha Vazia
Esta função verifica se há elementos na pilha, ela é util por exemplo para pararmos um algoritmo que retira elementos da pilha.
```python
def __pilha_vazia(self):
    if self.__topo == -1:
      return True
    else:
      return False
```

### Função Empilhar
Agora criada nossa pilha é preciso adicionar valores a ela, como temos acesso somente ao topo da pilha, sua função de iserção não precisa de um mecanimos para remanejar os itens como em vetores, nem ordenalos, basta adicionarmos item após item como se estivessemos os *"empilhando"*.
```python
def empilhar(self, valor):
    if self.__pilha_cheia():
      print("A pilha está cheia")
    else:
      self.__topo += 1
      self.__valores[self.__topo] = valor
```
Note que se fez necessário o uso da função `pilha_cheia()` previamente definida.

### Função Desempilhar
Caso precisemaos remover elementos de nossa pilha, faremos isso apenas manipulando seu topo, agora como se estivessemos *"desempilhando"* elemento a elemento.
```python
  def desempilhar(self):
    if self.__pilha_vazia():
      print("A pilha está vazia")
    else:
      self.__topo -= 1
```
Agora se fez necessária o uso da função `pilha_vazia()`.

### Função Ver Topo
Apesar de termos acesso somente ao topo da pilha, não signmifica que não possamos ter uma função de visualização. Assim como em uma pilha de papeis que podemos ler somente o papel que se encontar no topo, esta função nos dará somente o valor que estpá no topo da pilha.
```python
  def ver_topo(self):
    if self.__topo != -1:
      return self.__valores[self.__topo]
    else:
      return -1
```

## Filas Circulares
[voltar ao topo](https://github.com/DougAugSilva/Estrutura_de_Dados_Python?tab=readme-ov-file#introdu%C3%A7%C3%A3o)
### Teoria
Assim como em filas que encontramos em bancos e padarias, a fila como estrutura de dados segue alguns aspectos semelhantes a estas, como por exemplo primeiro elemento a aser inserido na fila será o primeiro a ser removido da fila. Algumas das aplicações das filas são:
- Modelar aviões aguardando a decolagem.
- Pacoites de dados que esperam ser transmitidos em uma rede.
- Fila de documentos para impressão de uma impressora.

Também temos operações que podemos realizar em filas, são estas:
- **Enfileirar:** Coloca um item no final da fila.
- **Desenfikleirar:** Remove um elemento do início da fila.
- **Ver Início:** Mostra o elemento que está no início da fila.

Uma fila é uma estrutura de dados do tipo *FIFO* (First In, First Out), isto é, primeiro a entar é o primeiroa sair. Em filas teremos dois ponteiros de manipulação e leitura, sendo um para o inicío da fila e um para o final da fila, coom isso temos o conceito de *fila circular*, onde os os ponteiros de início e final da fila se movem entre as posições da fila, dispesando assim um remanejamento dos itens, porem podemos ter a inverção dos ponteiro de inicio e final da fila, podendo em alguns casos o inico está a direita do ponteiro de final e vice versa.

### Definido a Classe e o Objeto
Na criação da fila vamos ter que inserir além da variavel de capacidade de armazenamento e dos valores, as variaveis dos ponteiros que farão a leitura dos elementos na posição inicial e final da fila. Para tal vamos importar a bibliota *numpy* e executar o código abaixo.
```python
import numpy as np

class FilaCircular:
  
  def __init__(self,capacidade):
    self.capacidade = capacidade
    self.inicio = 0  #seta o ponetiro de leitura do inico
    self.final = -1  #seta o ponteiro de leitura do final
    self.numero_elementos = 0
    self.valores = np.empty(self.capacidade, dtype = int) #cria o vetor do tipo np array com entradas inteiras
```

### Definindo Funções Auxiliares
Neste passo vamos defeinir de uma vez algumas funções que nos serão uteis, mas que não precisam ter seu acesso liberado ao usuário, apenas nos serão uteis para a criação das demias funções.
```python
 #função que verifica se a fila está vazia
  def __fila_vazia(self):
    return self.numero_elementos == 0  #se o numero de eleemnto for 0, a fila está vazia

 #função que verifica se a fila está cheia 
  def __fila_cheia(self):
    return self.numero_elementos == self.capacidade
```

### Função Enfileirar
Agora precisamos a de uma função para adicionarmos elementos a nossa fila, sendo que devemos respeitar a estrutura de adicioanrmos elementos ao inicio da fila, semelhante ao que fizemos com piulhas, não precisaremos de uma ordenação, dado que estamos trabalhando com uma fila circular, mas devemos criar um mecanismo de movimentação do ponteiro de final de fila a cada elemento adicionado.
```python
  def enfileirar(self, valor):
    if self.__fila_cheia():  #caso a fila esteja cheia
      print("A fila está cheia")  #retorna que a fila está cheia e não adiciona mais elementos
      return
    if self.final == self.capacidade -1: #caso o ponteiro do final da fila tenha chegado no último elemento
      self.final = -1  #direcionanmos ele para começar no inico da fila antes da posição inicial
    self.final += 1  #depois setamos ele para a o inico da fila na posição 0
    self.valores[self.final] = valor  #depois o final da fila recebe op valor desejado
    self.numero_elementos += 1  #depois incrementamos o número de elementos da fila
```
### Função Desenfileirar
Agora para removermos um elemento da fila precisamos respeitar a regra de que *"o primeiro elemento a entar deve ser o primeiro a sair"*, deste modo torna-se necessário desenvolver um mecanismo de mudança de posição para o ponteiro que indica o inicio da fila.
```python
 def desenfileirar(self):
    if self.__fila_vazia():  #caso a fila não tenha elementos para retiramos
      print("A fila já está vazia")  #retorna que a fila está vazia
      return
    temp = self.valores[self.inicio]  #atribuimos a tem qual elemento foi desenfileiradov (semopre o elemento do início)
    self.inicio += 1  #depois de adicionarmo um elemento trocamos o ponteiro de posição inicial da fila
    if self.inicio == self.capacidade -1:  #caso o ponteiro do inicio da fila chegou ao final da fila
       self.inicio = 0  #retornamos o ponteiro para o inico da fila
    self.numero_elementos -= 1  #diminuimos o núpumero de elementos da fila
    return temp  #nos retorna o valor que foi retirado da fila
```

### Função de Leitura
Assim como em pilhas, nas filas temos acesso apenas a um elemento por vez, no caso o elemento que está presente no iníco da fila, deste mdodoa função de leitura deve nos retornar apenas o elemento nesta posição.
```python
#função que retorna o primeiro valor da fila
  def primeiro(self):
    if self.__fila_vazia(): #caso a fila esteja vazia nos retorna o valor -1
      return -1  
    return self.valores[self.inicio]  #caso contrário nos retorna o valor no início da fila
```

### Importante Notar
Antes de darmos continuidades as demais estruturas de dados, é importante notar algo relacionado as filas:
- Na definição do objeto podemos inserir "__" nas funçoes de definição do objeto, ccomo *valores* por exemplo, para assim não permitir o usuario o acesso à valores que não estejam no início da fila.
- o ponteiro que indica a posição dos valores do **inicio da fila** só se move quando **retirando elementos da fila**.
- o ponteiro que indica a posição dos valores do **final da fila** só se move quando **adicionando elmentos da fila**.

## Filas de Prioridade
[voltar ao topo](https://github.com/DougAugSilva/Estrutura_de_Dados_Python?tab=readme-ov-file#introdu%C3%A7%C3%A3o)
### Teoria
Assim como em filas circulares, filas com prioridade também são estruturas de dados do tipo *FIFO* (First In, First Out), porém agora temos algumas propriedades adicionais:
- A cada item ordenado é atribuido um *peso*, de modo que itens com pesos maiores/menores possuem *prioridade* sobre os demais.
- Elementos com alta prioridade são colocados no início da fila, com média prioridade no meio da fila e com baixa prioridade no final da fila.

Dado a estrutura das filas com prioridade, as unicas funções que se alteram em comparação com as fils circulares são a função `enfileirar()` e a função `desenfileirar()`, deste modo podemos aproveitar as outras funções da seção anmterior.

### Função Enfileirar
Neste caso será preciso inserir um mecanismo de remanejamento semelhante ao presente nos *vetores*, para assim podermos inserir itens em suas devidas posições conforme suas prioridades. neste exemplo colocaremos uma prioridade maior para os números menores.
```python
 def enfileirar(self, valor):
    if self.__fila_cheia():  #caso a fila esteja cheia, retorna que a fila está cheia
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
```

### Função Desenfileirar
Já a função desenfileirar se torna mais simples neste caso, a ordenação dos elementos na fila dispensa um ponteiro de leirura para os itens no inio da fila, os itens a sair primeiro já se encontram organizados dentro da fila por conta da função de inserção, bastando apenas assim verificarmos se há elemntos na fila e removermos o elemnto mais a direita da fila.
```python
def desenfileirar(Self):
    if self.__fila_vazia():  #caso a fila esteja vazia
      print("A fila está vazia")
      return
    valor = self.valores[self.numero_elementos -1] 
    self.numero_elementos -= 1 
    return valor  #caso contrário remove o primeiro elemento da fila e o retorna
```

## Deques 
[voltar ao topo](https://github.com/DougAugSilva/Estrutura_de_Dados_Python?tab=readme-ov-file#introdu%C3%A7%C3%A3o)
### Teoria
Deque é uma sigla que significa *"Double Ended Queue"*, isto é, se trata de uma fila que temos acoesso agora aos seus dois extremos, como um deque de cartas em que podemos retirar uma carta da parte de sima ou de baixo do deque. Um Deque suporta operações tanto de filas quanto de pilhas, sendo muito usado em algoritmos de programação paraleala em processadores Intel por exemplo. As operações que podem sera realizadas são:
- Adicionar ao início
- Adicionar no final
- Excluir do início
- Excluir do final

Sendo que podemos implementar estas operações de forma *estática* ou *circular*. Será abordada a forma circular para um deque, forma na qual os elementos de inicio e fim circulam dentro do vetor, por meio de mudanças nos ponteiros de inicío e fim.

### Definindo a Classe e o Objeto
Vamos também definir nesta parte as funções auxiliares que servirão de base para a criação das demais.
```python
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
```

### Funções de Inserção 
Aqui podemos criar uma função que irá inserir intens no inicio do deque, e uma função para inserir itens no final do deque.

#### Função Insere Início
Primeiro vamos verificar se a fila está cheia, caso não esteja é preciso verificar se o início está na primeira posição, setamos ele para ulrima casa do vetor para assim inserirmos o valor, caso contrario apenas inserimos o valor na casa subsequente.
```python
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
```

#### Função Insere Final
De forma semelhante, segue a função que insere valores no final do deque:
```python
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
```

### Funções de Exclusão
Assim como temos duas funções de inserção, podemos ter duas funções de exclusão, e desde modo manipularmos de forma completa o inicio e o final do deque.

#### Função Excluir Inicío
Desta vez verificamos se o deque está vazio para sabermos e ainda há itens a serem removidos, depois verificamos se o deque possui apenas um único elemento para assim podermos setar os ponteiros de início e fim. 
```python
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
```

#### Função Excluir Final
Bem parecida coma função de excluir o início, mudando a parte de decrementarmos o novo final e o ajuste do ponteiro de final para a poisção final caso o inicio esteja na posição inícial.
```python
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
```

### Funções de Retorno
Falta apenas funções para visualisarmos quais fvalores estão nas posição inicila e na posição final do deque, são funções simples e sua sintaze segue abaixo;

#### Retorna o Inicio
```python
  def get_inicio(self):
    if self.__deque_vazio():
      print("O deque está vazio")
      return
    return self.valores[self.inicio]   
```

#### Retorna o Final
```python
  def get_final(self): 
    if self.__deque_vazio() or self.final < 0: #uma condição a mais por segurança
      print("O deque está vazio")
      return
    return self.valores[self.final]
```

## Listas Encadeadas
[voltar ao topo](https://github.com/DougAugSilva/Estrutura_de_Dados_Python?tab=readme-ov-file#introdu%C3%A7%C3%A3o)
### Teoria
As *listas encadeadaas* são estruras de dados que funcionam de maneira diferente ao que foi visto até então, enquando as aestruturas de dados aboradas até agora se baseiam em vetores, com um certo número de entradas pré determinado e indices para indicar suas posiçõs, listas encadeadas são estruturadas atravéz de *nós*, e surgiram a para tentar contiornar algumas desvantagens dos vetores.

**Principais Desvantagens dos Vetores:**
- Em um vetor não ordenado, a função de busca é lento.
- Em um vetor ordenado, a função de inserção é lenmta.
- Em qualquer vetor, mesmos as entradas vazias (sem valores atribuidops) ocupam espaço na memória, isto é, um vetor com 100 entradas mas contendo apenas 5 valores, ocupa um espaço na memória de 100 entradas.

Agora nas listas encadeadas cada valor de dado é incorporado em um nó, cada nó possui uma referencia a ao próximo item da lista, como se fosse uma coordenada de como encontra-lo, com isso temos a *cabeça* da lista que é o nó que não é referanciado por nenhum anterior a ele, e a *cauda* da lista que é um nó que não faz referencia anenhum outro nó.
- Cada elemento da lista é aramzeando em um nó que será definifo como um objeto.
- Cada elemento da lista faz referncia ao prócimo e só será remanejado se necessário.
- Será criado o objeto *cabeça da lista* para fazermos referéncia o primreiro nó da lista.

**Principais Diferenças Entre Listas e Vetores:**

**Vetor:** É uma estrutura de posicionamento dos dados.
- Cada elemento ocupa uma certa posição e lhe é atribuidop um certo indice.
- Cada posição pode ser acessada pelo seu indice.

**Lista:** É uma estrutura de relacionamento dos dados.
-  A única maneira de se chjegar a um elemento é seguindo a sequêncai de elementos.
-  Cada item de dados não pode ser acessado de forma direto, ou seja, a relação entre eles deve ser utilizada pra isso.
-  Iniciamos no primeiro item, depois para o segundo, e assim por diante, atpé encontrarmos o item desejado, realizando uma pesquisa linear.

As funções que vamos trabalhar com listas encadadas são:
- Inserve no Início
- Excluir no Início
- Mostar Lista
- Pesquisar
- Excluir da Posição

