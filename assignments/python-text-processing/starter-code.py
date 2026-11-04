"""
Python Text Processing — Starter Code
Mergington High School

Complete as funções abaixo seguindo as tarefas do README.md.
Execute com:  python starter-code.py
"""


def clean_text(line):
    """Tarefa 1: normaliza uma linha de texto.

    Remova espaços das pontas, converta para minúsculas e
    substitua múltiplos espaços por um único espaço.
    """
    # Seu código aqui
    pass


def read_poem(filename):
    """Tarefa 2: lê o arquivo e retorna uma lista de linhas limpas.

    Use `with open(filename, encoding="utf-8")` e ignore linhas vazias.
    """
    # Seu código aqui
    pass


def analyze_text(lines):
    """Tarefa 3: calcula estatísticas do texto.

    Retorne um dicionário com as chaves: lines, words, most_common_word.
    """
    # Seu código aqui
    pass


def write_report(stats, filename="relatorio.txt"):
    """Tarefa 4 (Desafio): grava um relatório formatado com as estatísticas."""
    # Seu código aqui
    pass


if __name__ == "__main__":
    lines = read_poem("poema.txt")
    stats = analyze_text(lines)
    print(stats)
    # Descomente quando chegar à Tarefa 4:
    # write_report(stats)
