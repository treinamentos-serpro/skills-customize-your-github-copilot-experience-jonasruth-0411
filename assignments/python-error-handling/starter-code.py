"""
Error Handling in Python — Starter Code
Mergington High School

Complete as funções abaixo seguindo as tarefas do README.md.
Execute com:  python starter-code.py
"""


def safe_divide(total_points, num_tests):
    """Tarefa 1: divide com segurança, capturando ZeroDivisionError.

    Retorne o resultado da divisão, ou 0 (com mensagem amigável)
    se num_tests for zero.
    """
    # Seu código aqui
    pass


def parse_grade(text):
    """Tarefa 2: converte texto em float com try/except/finally.

    Retorne o número convertido, ou None se a entrada não for numérica.
    Use finally para imprimir "Entrada processada." em todos os casos.
    """
    # Seu código aqui
    pass


# Tarefa 3: defina aqui a exceção customizada InvalidGradeError


def validate_grade(grade):
    """Tarefa 3: valida a nota, lançando InvalidGradeError se estiver fora de 0-100."""
    # Seu código aqui
    pass


def grade_registry(entries):
    """Tarefa 4 (Desafio): processa todas as entradas sem quebrar.

    Retorne um dicionário: {"valid": [...], "rejected": [...]}.
    """
    # Seu código aqui
    pass


if __name__ == "__main__":
    print(safe_divide(85, 0))
    print(parse_grade("7.5"))
    print(parse_grade("abc"))

    # Entradas simulando o que usuários digitariam
    entries = ["8.5", "abc", "105", "92", "-3", "76.5"]
    print(grade_registry(entries))
    # Saída esperada: {'valid': [8.5, 92.0, 76.5], 'rejected': ['abc', '105', '-3']}
