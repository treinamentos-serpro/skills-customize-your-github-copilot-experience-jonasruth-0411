# 📘 Assignment: Data Structures in Python

## 🎯 Objective

Os alunos aprenderão a usar as principais estruturas de dados do Python — listas, dicionários, sets e tuplas — escolhendo a estrutura certa para cada situação ao construir um sistema de playlist de músicas.

## 📝 Tasks

### 🛠️ Montando a Playlist com Listas

#### Descrição
Complete a função `build_playlist` no starter code para criar e manipular uma lista de músicas.

#### Requisitos
O programa concluído deve:

- Criar uma lista com os títulos das músicas recebidos como parâmetro
- Adicionar uma música ao final com `append()` e remover uma música específica com `remove()`
- Retornar a lista em ordem alfabética usando `sorted()` ou `sort()`

Exemplo de entrada/saída:

```python
>>> build_playlist(["Shape of You", "Blinding Lights", "Levitating"])
['Blinding Lights', 'Levitating', 'Shape of You']
```

### 🛠️ Catalogando com Dicionários

#### Descrição
Complete a função `build_catalog` para organizar as músicas em um dicionário que associa cada título às suas informações.

#### Requisitos
O programa concluído deve:

- Criar um dicionário onde cada chave é o título da música e o valor é outro dicionário com `artist` e `duration` (em segundos)
- Implementar a função `total_duration` que soma a duração de todas as músicas do catálogo
- Implementar a função `songs_by_artist` que retorna a lista de títulos de um artista específico (lista vazia se o artista não existir)

### 🛠️ Comparando Gostos com Sets

#### Descrição
Dois alunos querem descobrir o que têm em comum musicalmente. Complete a função `compare_playlists` usando operações de conjuntos (sets).

#### Requisitos
O programa concluído deve:

- Converter as duas playlists (listas) em sets
- Calcular as músicas em comum (interseção), todas as músicas (união) e as exclusivas de cada playlist (diferença)
- Retornar um dicionário com as chaves `common`, `all_songs` e `only_first`

Exemplo de saída:

```python
>>> compare_playlists(["A", "B", "C"], ["B", "C", "D"])
{'common': {'B', 'C'}, 'all_songs': {'A', 'B', 'C', 'D'}, 'only_first': {'A'}}
```

### 🛠️ Desafio: Top Músicas com Tuplas

#### Descrição
Como objetivo final, monte o ranking das músicas mais tocadas. Complete a função `top_songs`, que recebe um dicionário de contagens de reprodução e retorna uma lista de tuplas imutáveis.

#### Requisitos
O programa concluído deve:

- Transformar o dicionário `{titulo: reproducoes}` em uma lista de tuplas `(titulo, reproducoes)`
- Ordenar a lista da música mais tocada para a menos tocada (dica: use `sorted()` com o parâmetro `key`)
- Retornar apenas as `n` primeiras tuplas, onde `n` é um parâmetro da função
- Desempacotar as tuplas em um loop para imprimir o ranking no formato `1º lugar: <titulo> (<reproducoes> plays)`
