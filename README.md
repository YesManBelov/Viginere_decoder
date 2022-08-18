# Viginire Decoder 1.0 -

## Характеристики

Декодер шифра Вижинера имеет 2 версии:
- [Старая "decoder.py"](decoder.py) 
- [Новая "decoder_update.py"](decoder_update.py) 
по заданию - запрещено использование классов



### Алгоритм интерпретатора команд для дешифратора:
- Загрузить данные (текст, кодовое слово, шифр(используется для проверки));
- Проверить целостность данных;
- Зашифровать встроеным механизмом;
- Проверить правильность полученного шифра;
- Зашифровать;
- Определить длину кодового слова;
- Подобрать кодовые слова по заданной длине;
- Расшифровать по подобранным кодовым словам;
- Сохранить полученный результат в файл.

Стартовая точка входа - вызов функции: 
```sh
main()  # decoder_update.py
```

В независимости от версии программы, функция принимает команду формата ***dict***.
Возвращает так же объект ***string***, вв котором хранится дешифрованный текст

### Ввод данных

Правила передачи данных в версиях различны, но в обеих версиях, регистр символов в команде не важен.

В [***стандартной версии***](decoder.py) на вход может подаваться строчка

**Обе версии** программы не будут обрабатывать заданную команду, если встретят невалидный символ.


### Проверка целостности

За проверку целостности кэша мы принимаем функцию 

```sh
binary_search()  # decoder_update.py
```

```sh
def binary_search(list, item):
    low = 0
    hight = len(list) - 1

    while low <= hight:
        mid = (low + hight)   # ==> middle element
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            hight = mid - 1
    return None
```


За поиск длины ключа отвечает функция

```sh
get_logn_key()
```

```sh
def get_maxSrez(group_list):
	maximum_ls=[]
	for i in range(len(group_list)):

		max_ver = []
		print("Группа №", i+1)
		for j in range(len(cn.BUKVAR)):
			x = czaimnyi_index(group_list, j, i)
			print(j, "-", x)
			var = (x, j)

			max_ver.append(var)
		print(max_ver)
		print(max(max_ver))
		maximum_id = max(max_ver)[1]
		maximum_value = max(max_ver)[0]
		maximum_ls.append([maximum_id])

		for k in max_ver:											# добавляем те что удовлетворяют условию
			if k[0] >= maximum_value-0.01 and k[0] < maximum_value:
				maximum_ls[i].append(k[1])
	del maximum_ls[0]
	print(maximum_ls)
	return maximum_ls
```

Обеспечивая взаимодействия между двумя функциями, мы создаём карту распределения минусов, благодаря которой получая длину ключа мы минмизируем предполагание лишних вариантов.

СТандартизируя качесво использования карты координат, будем определять каждый новый ключ исключая данные по ппредположениям выделенных областей.
Программа работает на интерпретаторе python 3.8
ПРограмма сторонниъ библиотек не использует.
