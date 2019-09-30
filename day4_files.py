from functools import reduce


def count_words_per_line(lines: list):
    count_words = list(map(lambda line: len(line.split(' ')), filter(lambda x: x != '\n', lines)))
    return count_words, reduce(lambda acc, val: acc + val, count_words)


def format_result(result: tuple):
    format_text = [f'Linea contiene {count}\n' for count in result[0]]
    format_text.append(f'Total de palabras: {result[1]}\n\n')
    return format_text


def write_results_to_file(file_name: str, data: list):
    try:
        file = open(file_name, 'wt')
        file.writelines(data)
    except Exception as ex:
        print(ex)


def append_results_to_file(file_name: str, data: list):
    try:
        file = open(file_name, 'a')
        file.writelines(data)
    except Exception as ex:
        print(ex)


def main():
    """
    # Day 4 - Week 1 - Python

    Para hoy:
    * Repaso 💩
    * Trabajo con ficheros 💩
    * POO
    * netacad
    * applicacion practica
    """
    try:
        fichero = open('c:\\git\\curso_python\\palabras.txt', 'rt')
        data = fichero.readlines()
        print(data)
        result = count_words_per_line(data)
        print(f'Count of words per line {result[0]}, count of total words {result[1]}')
        write_results_to_file('c:\\git\\curso_python\\palabras_result.txt', format_result(result))
        append_results_to_file('c:\\git\\curso_python\\palabras_result.txt', format_result(result))

        fichero.close()
    except FileNotFoundError as err:
        print(err)
