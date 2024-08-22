from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file_content = txt_importer(path_file)

    file_name = path_file
    file_info = {
        "nome_do_arquivo": file_name,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }

    for i in range(len(instance)):
        existing_file = instance.search(i)
        if existing_file.get("nome_do_arquivo") == file_name:
            return

    instance.enqueue(file_info)

    sys.stdout.write(str(file_info))


def remove(instance):
    if instance.is_empty():
        sys.stdout.write(str("Não há elementos\n"))
        return

    removed_file = instance.dequeue()
    print(f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        sys.stdout.write(str(instance.search(position)))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
