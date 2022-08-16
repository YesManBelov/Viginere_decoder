from typing import Dict, List, Tuple, Union, Any


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


def get_answer(question: str, choice: Tuple[str, ...]) -> str:
    '''Получение ответа'''
    answer = input(question)
    while answer not in choice:
        answer = input(question)
    return answer


def get_alph(number: int) -> str:
    '''Загрузка алфавита'''
    text_lines = get_text_on_file('data/alphavit.txt')
    return text_lines[number].replace('\n', '')


def conv_text(text: Union[str, List],
              alphavit: str,
              options: str = 'to_int') -> List[Any]:
    '''Преобразователь текста в список индексов по алфавиту или наоборот'''
    if options == 'to_int':
        con_func = alphavit.index
    elif options == 'to_str':
        con_func = alphavit.__getitem__
    else:
        raise AttributeError
    text_numbers = []
    for word in text:
        text_numbers.append(con_func(word))
    return text_numbers


def get_cipher(text: str, code: str, alph: str) -> str:
    ''' Доработать (не будет работать с кодовым словом большим текста'''
    number_text = conv_text(text, alph)
    number_code = conv_text(code, alph)
    # найдем, что меньше:
    if number_text >= number_code:
        difference = len(number_text) // len(number_code)
        difference_mod = len(number_text) % len(number_code)
        r_number_code = (number_code * difference)
        r_number_code.extend(number_code[:difference_mod])
        r_number_text = number_text
    else:
        difference = len(number_code) // len(number_text)
        difference_mod = len(number_code) % len(number_text)
        r_number_text = (number_text * difference)
        r_number_text.extend(number_text[:difference_mod])
        r_number_code = number_code
    itog = [(x+y) % len(alph) for x, y in zip(r_number_code, r_number_text)]
    list_itog = conv_text(itog, alph, 'to_str')
    print(list_itog)
    print(type(list_itog[0]))
    return ''.join(list_itog)


def main(data: Dict[str, str]):
    '''Главная функция'''
    alph_number = get_answer('Без "Ё" - 0\nС "Ё" -   1\n: ', ('0', '1'))
    alph = get_alph(int(alph_number))
    main_cipher = get_cipher(data['text'], data['code_word'], alph)
    print('Check: ')
    print(main_cipher == data['cipher'])


if __name__ == '__main__':
    data_dict = get_data('data/data.txt')
    print(data_dict)
    main(data_dict)
