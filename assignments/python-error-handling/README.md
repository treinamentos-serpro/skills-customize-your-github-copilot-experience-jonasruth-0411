# 📘 Assignment: Error Handling in Python

## 🎯 Objective

Os alunos aprenderão a escrever código robusto usando o tratamento de exceções do Python — `try/except/finally`, `raise` e exceções customizadas — construindo um sistema de cadastro de notas que não quebra com entradas inválidas.

## 📝 Tasks

### 🛠️ Capturando a Primeira Exceção

#### Descrição
Complete a função `safe_divide` no starter code para calcular a média de pontos por prova sem deixar o programa quebrar com divisão por zero.

#### Requisitos
O programa concluído deve:

- Usar um bloco `try/except` para capturar `ZeroDivisionError`
- Retornar o resultado da divisão quando ela for válida
- Retornar `0` e imprimir uma mensagem amigável quando o divisor for zero

Exemplo de entrada/saída:

```python
>>> safe_divide(85, 0)
Não é possível dividir por zero!
0
```

### 🛠️ Convertendo Entradas com Segurança

#### Descrição
Notas digitadas pelos usuários chegam como texto e nem sempre são válidas. Complete a função `parse_grade` para converter a entrada em número tratando os erros possíveis.

#### Requisitos
O programa concluído deve:

- Converter a string recebida para `float` dentro de um bloco `try/except`
- Capturar `ValueError` e retornar `None` quando a entrada não for numérica (ex.: `"abc"`)
- Usar `finally` para imprimir `"Entrada processada."` em todos os casos, com ou sem erro

### 🛠️ Lançando Suas Próprias Exceções

#### Descrição
Nem todo número é uma nota válida. Complete a função `validate_grade` para rejeitar notas fora do intervalo permitido usando `raise`.

#### Requisitos
O programa concluído deve:

- Definir a exceção customizada `InvalidGradeError`, herdando de `Exception`
- Lançar `InvalidGradeError` com uma mensagem clara quando a nota for menor que 0 ou maior que 100
- Retornar a nota quando ela for válida

Exemplo de entrada/saída:

```python
>>> validate_grade(105)
InvalidGradeError: Nota 105 fora do intervalo permitido (0-100)
```

### 🛠️ Desafio: Cadastro de Notas à Prova de Erros

#### Descrição
Como objetivo final, junte tudo em um programa completo. Complete a função `grade_registry` que lê uma lista de entradas (simulando o que usuários digitariam) e monta o boletim final sem nunca quebrar.

#### Requisitos
O programa concluído deve:

- Processar cada entrada da lista usando `parse_grade` e `validate_grade`
- Capturar `InvalidGradeError` e registrar as entradas rejeitadas em uma lista separada
- Retornar um dicionário com as chaves `valid` (notas aceitas) e `rejected` (entradas recusadas)
- Processar a lista inteira até o fim, mesmo que várias entradas sejam inválidas
