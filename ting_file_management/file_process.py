import sys
from ting_file_management.file_management import txt_importer

files_processed = {}


def process(path_file, instance):
    try:
        files_processed[path_file]
    except KeyError:
        file = txt_importer(path_file)
        file_processed = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file
        }
        instance.enqueue(file_processed)
        print(file_processed, file=sys.stdout)
        files_processed[path_file] = file_processed


def remove(instance):
    if (len(instance) >= 1):
        name_file_removed = instance.dequeue()["nome_do_arquivo"]
        message = f"Arquivo {name_file_removed} removido com sucesso"
        print(message, file=sys.stdout)
    else:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        file_info = instance.search(position)
        print(file_info, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
