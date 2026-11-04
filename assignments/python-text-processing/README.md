# 📘 Assignment: Python Text Processing

## 🎯 Objective

Os alunos aprenderão a trabalhar com strings, leitura e escrita de arquivos (file I/O) e técnicas de manipulação de texto em Python, construindo um analisador de texto passo a passo.

## 📝 Tasks

### 🛠️ Explorando Strings

#### Descrição
Comece praticando os métodos de string mais usados do Python. Complete a função `clean_text` no starter code para normalizar uma linha de texto.

#### Requisitos
O programa concluído deve:

- Remover espaços em branco do início e do fim do texto com `strip()`
- Converter todo o texto para minúsculas com `lower()`
- Substituir múltiplos espaços consecutivos por um único espaço

Exemplo de entrada/saída:

```python
>>> clean_text("   Olá   MUNDO  ")
'olá mundo'
```

### 🛠️ Lendo o Arquivo de Texto

#### Descrição
Complete a função `read_poem` para ler o arquivo `poema.txt` fornecido e retornar suas linhas já normalizadas.

#### Requisitos
O programa concluído deve:

- Abrir o arquivo usando `with open(..., encoding="utf-8")`
- Retornar uma lista com as linhas do arquivo, aplicando `clean_text` em cada uma
- Ignorar linhas vazias (não incluí-las na lista retornada)

### 🛠️ Analisando o Texto

#### Descrição
Agora transforme seu programa em um analisador de texto. Complete a função `analyze_text` para calcular estatísticas sobre o poema.

#### Requisitos
O programa concluído deve:

- Contar o número total de linhas e de palavras do texto
- Encontrar a palavra mais frequente (dica: use um dicionário para contar ocorrências)
- Retornar os resultados em um dicionário com as chaves `lines`, `words` e `most_common_word`

Exemplo de saída:

```python
>>> analyze_text(read_poem("poema.txt"))
{'lines': 12, 'words': 75, 'most_common_word': 'mar'}
```

### 🛠️ Desafio: Gerando um Relatório

#### Descrição
Como objetivo final, escreva os resultados da análise em um novo arquivo. Complete a função `write_report` para gerar um relatório formatado em `relatorio.txt`.

#### Requisitos
O programa concluído deve:

- Criar o arquivo `relatorio.txt` usando file I/O de escrita
- Formatar o relatório usando f-strings, com uma estatística por linha
- Incluir no relatório as 5 palavras mais frequentes do texto, em ordem decrescente de ocorrências
- Executar todo o fluxo (ler → analisar → gravar) quando o script for executado diretamente
