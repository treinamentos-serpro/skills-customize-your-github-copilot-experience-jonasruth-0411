"""
Data Structures in Python — Starter Code
Mergington High School

Complete as funções abaixo seguindo as tarefas do README.md.
Execute com:  python starter-code.py
"""


def build_playlist(songs):
    """Tarefa 1: cria e manipula uma lista de músicas.

    Adicione uma música com append(), remova uma com remove()
    e retorne a lista em ordem alfabética.
    """
    # Seu código aqui
    pass


def build_catalog():
    """Tarefa 2: retorna um dicionário {titulo: {"artist": ..., "duration": ...}}."""
    # Seu código aqui
    pass


def total_duration(catalog):
    """Tarefa 2: soma a duração (em segundos) de todas as músicas do catálogo."""
    # Seu código aqui
    pass


def songs_by_artist(catalog, artist):
    """Tarefa 2: retorna a lista de títulos de um artista (ou lista vazia)."""
    # Seu código aqui
    pass


def compare_playlists(playlist1, playlist2):
    """Tarefa 3: compara duas playlists usando sets.

    Retorne um dicionário com as chaves: common, all_songs, only_first.
    """
    # Seu código aqui
    pass


def top_songs(play_counts, n):
    """Tarefa 4 (Desafio): retorna as n músicas mais tocadas como lista de tuplas."""
    # Seu código aqui
    pass


if __name__ == "__main__":
    print(build_playlist(["Shape of You", "Blinding Lights", "Levitating"]))

    catalog = build_catalog()
    print(total_duration(catalog))
    print(songs_by_artist(catalog, "Dua Lipa"))

    print(compare_playlists(["A", "B", "C"], ["B", "C", "D"]))

    plays = {"Blinding Lights": 320, "Levitating": 215, "Shape of You": 410, "Bad Guy": 180}
    for i, (title, count) in enumerate(top_songs(plays, 3), start=1):
        print(f"{i}º lugar: {title} ({count} plays)")
