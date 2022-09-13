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
        instance.enqueue(path_file)
        print(file_processed, file=sys.stdout)
        files_processed[path_file] = file_processed


def remove(instance):
    if (len(instance) >= 1):
        file_removed = instance.dequeue()
        print(f"Arquivo {file_removed} removido com sucesso", file=sys.stdout)
    else:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
