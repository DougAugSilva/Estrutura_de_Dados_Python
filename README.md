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

### Allgoritmo de Impreção
...

## Vetores Ordenados
Vetores ordenados são semelhantes aos Não Ordenados, porem agora os dados são armazenados em uma ordem específica pré definida, possuindo assim carateristicas particulares quanto a sua manipulação:
- Toda vez que formos inserir um item no vetor, precisaremos fazer uma pesquisa sobre os demais itens para ainserção respeitar a ordenação do vetor.
- O algoritmo de pesquisa não precisa necessariamente fazer a leitura de todas as entradas do vetor em todos os casos, basta ele chegar no primeiro item maior que o item a ser pesquisado.
- A parte do remanejamento do algoritmo de exclusão é igual ao do vetor não ordenado.

Novamente vamos definir e implementar os algoritmos de manipulação dessa estrutura de dados.

### Definido a Classe


