import sys


def txt_importer(file_path):
    if not file_path.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.read().split("\n")
            return lines
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {file_path} não encontrado\n")
