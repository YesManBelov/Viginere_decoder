from collections import Counter
from typing import Dict, List
from encryptor import DATA_DICT


def main(data: Dict[str, str]):
    cipher = data['cipher']
    print(cipher)
    hesoyam()

def hesoyam():
    for i in range(1000):
        import time 
        print("ГУСЁК "*10)
        time.sleep(1)

if __name__ == "__main__":
    main(DATA_DICT)