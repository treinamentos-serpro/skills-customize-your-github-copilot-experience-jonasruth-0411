"""
Building REST APIs with FastAPI — Starter Code
Mergington High School

Para executar a API:
    1. Instale as dependências:  pip install fastapi uvicorn
    2. Inicie o servidor:        uvicorn starter-code:app --reload
    3. Acesse a documentação:    http://localhost:8000/docs

Complete as tarefas descritas no README.md. Boa sorte! 🚀
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Biblioteca da Mergington High",
    description="API REST para gerenciar os livros da biblioteca da escola",
)

# Banco de dados em memória da biblioteca (não altere a estrutura dos livros)
books = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes", "available": True},
    {"id": 2, "title": "Automate the Boring Stuff", "author": "Al Sweigart", "available": True},
    {"id": 3, "title": "Clean Code", "author": "Robert C. Martin", "available": False},
]


# Tarefa 1: Hello API
# Crie aqui a rota GET / que retorna uma mensagem de boas-vindas


# Tarefa 2: Listando e Consultando Livros
# Crie aqui as rotas GET /books e GET /books/{book_id}
# Dica: use HTTPException(status_code=404, detail="...") quando o livro não existir


# Tarefa 3: Criando Livros com Validação
# Defina aqui o modelo Pydantic `Book` e a rota POST /books
# Dica: herde de BaseModel e use status_code=201 no decorator da rota


# Tarefa 4 (Desafio): Empréstimo e Devolução
# Crie aqui as rotas PATCH /books/{book_id}/borrow, PATCH /books/{book_id}/return
# e DELETE /books/{book_id}
