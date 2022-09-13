import csv
import sys


def txt_importer(path_file):
    try:
        if (path_file.endswith(".txt")):
            lines = []
            with open(path_file, ) as file:
                file_reader = csv.reader(file, delimiter="\n")
                for line in file_reader:
                    lines.append(line[0])
                return lines
        print("Formato inválido", file=sys.stderr)
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
