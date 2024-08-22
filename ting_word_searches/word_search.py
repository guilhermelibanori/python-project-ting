import re


def exists_word(word, instance):
    occurrences_list = []

    for index in range(len(instance)):
        file_info = instance.search(index)
        file_name = file_info["nome_do_arquivo"]
        occurrences = []

        with open(file_name, "r") as file:
            lines = file.readlines()

        for line_number, line in enumerate(lines, start=1):
            if re.search(rf"\b{re.escape(word)}\b", line, re.IGNORECASE):
                occurrences.append({"linha": line_number})

        if occurrences:
            occurrences_info = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences,
            }
            occurrences_list.append(occurrences_info)

    return occurrences_list


def search_by_word(word, instance):
    occurrences_list = []

    for index in range(len(instance)):
        file_info = instance.search(index)
        file_name = file_info["nome_do_arquivo"]
        occurrences = []

        with open(file_name, "r") as file:
            lines = file.readlines()

        for line_number, line in enumerate(lines, start=1):
            if re.search(rf"\b{re.escape(word)}\b", line, re.IGNORECASE):
                occurrences_info = {
                    "linha": line_number,
                    "conteudo": line.strip(),
                }
                occurrences.append(occurrences_info)

        if occurrences:
            occurrences_info = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences,
            }
            occurrences_list.append(occurrences_info)

    return occurrences_list
