
def get_data(text_file: str) -> dict[str, str]:
    with open(text_file, 'r', encoding='utf8') as f:
        text_lines = f.readlines()
    text_lines = list(map(lambda s: s.replace('\n', '').strip(), text_lines))
    text_lines = list(filter(None, text_lines))
    if len(text_lines) != 3:
        raise AttributeError
    columns = ('text', 'code_word', 'cipher')
    return {columns[i]: text_lines[i] for i in range(3)}


def main(data: dict[str, str]):
    pass


if __name__ == '__main__':
    data_dict = get_data('data.txt')
    main(data_dict)
