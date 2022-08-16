from collections import Counter
from typing import Dict, List
from encryptor import DATA_DICT


def main(data: Dict[str, str]):
    cipher = data['cipher']
    print(cipher)


if __name__ == "__main__":
    main(DATA_DICT)