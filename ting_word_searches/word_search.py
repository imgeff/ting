def exists_word(word, instance):
    queue = instance.getQueue()
    result = []
    for file in queue:
        report_file = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }
        for index, linha in enumerate(file["linhas_do_arquivo"]):
            if(word.lower() in linha.lower()):
                report_file["ocorrencias"].append({"linha": index + 1})
        if(len(report_file["ocorrencias"])):
            result.append(report_file)
    return result


def search_by_word(word, instance):
    queue = instance.getQueue()
    result = []
    for file in queue:
        report_file = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }
        for index, linha in enumerate(file["linhas_do_arquivo"]):
            if(word.lower() in linha.lower()):
                report_file["ocorrencias"].append({
                    "linha": index + 1, "conteudo": linha
                })
        if(len(report_file["ocorrencias"])):
            result.append(report_file)
    return result
