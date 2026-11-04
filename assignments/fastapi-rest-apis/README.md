# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Os alunos aprenderão a construir uma API REST completa usando o framework FastAPI, criando endpoints para listar, consultar, criar e remover recursos, além de validar dados com modelos Pydantic.

## 📝 Tasks

### 🛠️ Hello API

#### Descrição
Comece explorando o starter code fornecido e crie seu primeiro endpoint. Execute a aplicação com `uvicorn` e acesse a documentação interativa em `/docs` para testar sua API.

#### Requisitos
O programa concluído deve:

- Executar sem erros com `uvicorn starter-code:app --reload`
- Responder à rota `GET /` com um JSON de boas-vindas, por exemplo: `{"message": "Bem-vindo à Biblioteca da Mergington High!"}`
- Exibir a documentação interativa automática em `http://localhost:8000/docs`

### 🛠️ Listando e Consultando Livros

#### Descrição
A API gerenciará a biblioteca da escola. Usando a lista de livros já incluída no starter code, crie endpoints de leitura (GET) para listar todos os livros e consultar um livro específico pelo seu `id`.

#### Requisitos
O programa concluído deve:

- Responder à rota `GET /books` com a lista completa de livros em JSON
- Responder à rota `GET /books/{book_id}` com o livro correspondente ao `id` informado
- Retornar o status HTTP `404` com uma mensagem clara quando o livro não existir

Exemplo de resposta para `GET /books/1`:

```json
{
  "id": 1,
  "title": "Python Crash Course",
  "author": "Eric Matthes",
  "available": true
}
```

### 🛠️ Criando Livros com Validação

#### Descrição
Permita que novos livros sejam cadastrados na biblioteca. Crie um modelo Pydantic para representar um livro e use-o para validar o corpo da requisição em um endpoint POST.

#### Requisitos
O programa concluído deve:

- Definir um modelo Pydantic `Book` com os campos `title` (str), `author` (str) e `available` (bool, padrão `True`)
- Responder à rota `POST /books` criando um novo livro com um `id` gerado automaticamente
- Retornar o status HTTP `201` e o livro criado em JSON
- Rejeitar automaticamente requisições com campos faltando ou de tipo incorreto (validação do Pydantic)

### 🛠️ Desafio: Empréstimo e Devolução

#### Descrição
Como objetivo final, implemente a lógica de empréstimo da biblioteca: os alunos podem pegar um livro emprestado (se disponível) e devolvê-lo depois. Use métodos HTTP adequados para atualizar e remover recursos.

#### Requisitos
O programa concluído deve:

- Responder à rota `PATCH /books/{book_id}/borrow` marcando o livro como indisponível (`available: false`)
- Retornar o status HTTP `409` com uma mensagem clara se o livro já estiver emprestado
- Responder à rota `PATCH /books/{book_id}/return` marcando o livro como disponível novamente
- Responder à rota `DELETE /books/{book_id}` removendo o livro da biblioteca e retornando o status HTTP `204`
