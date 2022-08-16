from collections import Counter
from typing import Dict, List
# from decoder import 


def get_text_on_file(text_file: str) -> List:
    '''Получение текста из файла'''
    with open(text_file, 'r', encoding='utf8') as f:
        text_lines = f.readlines()
    return text_lines


def get_data(text_file: str) -> Dict[str, str]:
    '''Получение данных (текст, кодовое слово, зашифрованный текст)'''
    text_lines = get_text_on_file(text_file)
    text_lines = list(map(lambda s: s.replace('\n', '').strip().lower(),
                          text_lines,
                          ))
    text_lines = list(filter(None, text_lines))
    if len(text_lines) != 3:
        raise AttributeError
    text_lines[0] = text_lines[0].replace(' ', '')
    columns = ('text', 'code_word', 'cipher')
    return {columns[i]: text_lines[i] for i in range(3)}


def main(data: Dict[str, str]):
    cipher = data['cipher']
    print(cipher)


if __name__ == "__main__":
    data_dict = get_data('data/data.txt')
    main(data_dict)