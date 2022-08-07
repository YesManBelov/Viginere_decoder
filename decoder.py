'''
	alfha version

'''
import constants as cn, time

def text_correct(text, mnim_long):
	new_out = []
	new_out = [text[i] for i in range(len(text)) if i% mnim_long == 0]
	return new_out

def f_itoe(wordik):
	'''колличество букв в заданном тексте'''		# ТУТ МЫ СМОТРИМ СКОЛЬКО БУКВ В ТЕКСЕ
	result = {}
	for i in wordik:
		for j in range(len(cn.BUKVAR)):
			if i == cn.BUKVAR[j-1]:
				if cn.BUKVAR[j-1] not in result:
					result[cn.BUKVAR[j-1]] = 1
				else:
					result[cn.BUKVAR[j-1]] += 1
	return result

def index_cons(result, word):						# ТУТ МЫ НАХОДИМ ИНДЕКС СОВПАДЕНИЯ ДЛЯ ЗАДАННОГО ТЕКСТА
	'''ИС'''
	n = len(word)
	summ = 0
	for i in result:
		bukv=(result[i]*(result[i]-1)/(n*(n-1)))
		summ+=bukv
	return summ

def printin_dict(obj):								# ДЛЯ КРАСИВОГО ВЫВОДА
	for key in obj:
		print(key, ":", obj[key])

def itog_index(i_iteras, text):									# ТУТ Я НАХОЖУ СУММУ ИНДЕКСОВ СОВПАДЕНИЯ ДЛЯ КОЛЛИЧЕСТВА ЗАДАННЫЪ ГРУПП
	itog = {}
	for i in range(i_iteras): 	# ТУТ ЗАДАЮ КОЛЛИЧЕСТВО РАЗ (КОЛЛИЧЕСВТО РАЗ = КОЛЛИЧЕСТВОМ ИТОГОВЫХ ГРУПП, ЧТО = ДЛИННЕ КЛЮЧА)
		i+=1
		x = text_correct(text,i)
		result=f_itoe(x)
		index_summ = index_cons(result,x)
		itog[i] = index_summ
	for i in itog:

		print(i, ':', itog[i])
	return itog

def grouping(keys, text):					# юзаем после нахождения ключа для того чтобы его найти
	'''группировка по ключу'''
	group_list = []
	for i in range(keys):
		word_iter = text[i:]
		group = text_correct(word_iter, keys)
		symbols = f_itoe(group)

		group_list.append(group)
		print("Группа №", i+1, group)
		for i in symbols:
			print(i, ':', symbols[i])
	return group_list

def indexs_group(keys, text):
	indexs_group=[]
	for i in range(keys):
		print("\nГРУППА №", i+1)
		index_group=itog_index(1, text[i])
		indexs_group.append(index_group)
	return indexs_group

def sdwig_group(sdwig, text, alphavit):
	new_d = {value: key for key, value in alphavit.items()}
	y = text[:]
	for i in range(len(y)):
		y[i] = new_d.get((alphavit[y[i]] - alphavit['а'] + sdwig) % alphavit['я'] + alphavit['а'])
	return y

def czaimnyi_index(list_group, sdwig, group):
	y = list_group[group][:]
	start = list_group[0][:]
	x = f_itoe(y)

	y_new = sdwig_group(sdwig, y, cn.B_DICT)
	x_new = f_itoe(y_new)
	summ = 0

	x_start = f_itoe(start)

	for i in cn.BUKVAR:
		if i not in x_start or i not in x_new:
			resultat = 0
		else:
			resultat = (x_start[i]*x_new[i])/(len(start)*len(y))
		summ+= resultat

	return summ

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

def slovarny1(word_list):
	res =[]
	itog=[]
	text_file = open("slovarik.txt", 'r', encoding= 'utf-8')
	slovar1 = text_file.readlines()
	text_file.close()
	for i in word_list:
		for j in slovar1:
			if i.lower() in j.lower():
				res.append(i)
	for i in range(len(res)):
		if res[i] not in itog:
			itog.append(res[i])

	return itog

def slovarny(word_list):
	itog = []
	for i in word_list:
		slovo = binary_search(slovar, i)
		if slovo != None:
			itog.append(slovar[slovo])
	return itog

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

def rezak(sdwigi):
	B_DICT=cn.B_DICT
	new_d = {value: key for key, value in B_DICT.items()}
	chlen=["а","б","в","г","д","е","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]

	print(sdwigi,"sdsdsdsdsd")
	for p in sdwigi:
		sdwig = p
		print(sdwig)
		y= cn.BUKVAR[:]
		for i in range(len(y)):
			y[i] = new_d.get((B_DICT[y[i]] - B_DICT['а'] - sdwig) % B_DICT['я'] + B_DICT['а'])
			chlen[i]+=y[i]
	return chlen

def main():
	print('ИНДЕКСЫ ДЛЯ ПОИСКА ДЛИНЫ КЛЮЧА')
	tables_index = itog_index(20, cn.WORD) # НАХОДИМ ИНДЕКСЫ ДЛЯ ПОИСКА ДЛИНЫ КЛЮЧА
	GROUP_CONS = int(input("Надо выбрать длину ключа: "))	# Допустим мы получили наибольшее значение индексов и оно равно 9 (ДЛИНА КОЮЧА 9)

	print("РАСПРЕДЕЛЕНИЕ ПО ГРУППАМ")
	group_list = grouping(GROUP_CONS, cn.WORD) # групируем посимвольно текст исходя из длины ключа

	print("ИНДЕКСИРУЕМ КАЖДУЮ ГРУППУ")
	indexs_group1 = indexs_group(GROUP_CONS, group_list) # получили индексы совпадения по группам

	print("ВЫВОДИМ НА ЭКРАН ВЕРОЯТНОСТИ СДВИГОВ КАЖДОЙ ГРУППЫ")
	maximum_in_group = get_maxSrez(group_list)
	print("wdwdwdwdwdwdwddw",maximum_in_group)
	print(len(maximum_in_group))
	input("ПРОДОЛЖАЕМ?")

	start = time.time()
	print("ВЫБИРАЕМ ВСЕ ВОЗМОЖНЫЕ СЛОВА ИСХОДЯ ИЗ СДВИГОВ")
	cecs=[]
	if len(maximum_in_group)==1:
		all_word = rezak(maximum_in_group)
		print("ОПРЕДЕЛЯЕМ ТОЛЬКО ОСМЫСЛЕННЫЕ")
		smysl=slovarny(all_word)
		print(smysl)
		cecs.append(smysl)

		input("lol kek cheburek")
	elif len(maximum_in_group)==2:
		for i in maximum_in_group[0]:
			for k in maximum_in_group[1]:
				all_word = rezak((i,k))
				print("ОПРЕДЕЛЯЕМ ТОЛЬКО ОСМЫСЛЕННЫЕ")
				smysl=slovarny(all_word)
				print(smysl)
				print(i)
				cecs.append(smysl)

	elif len(maximum_in_group)==3:
		for i in maximum_in_group[0]:
			for k in maximum_in_group[1]:
				for l in maximum_in_group[2]:
					all_word = rezak((i,k,l))
					print("ОПРЕДЕЛЯЕМ ТОЛЬКО ОСМЫСЛЕННЫЕ")
					print('x',all_word)
					smysl=slovarny(all_word)
					print(smysl)
					print(i)
					cecs.append(smysl)

	elif len(maximum_in_group)==4:
		for i in maximum_in_group[0]:
			for k in maximum_in_group[1]:
				for l in maximum_in_group[2]:
					for m in maximum_in_group[3]:
						all_word = rezak((i,k,l,m))
						print('y',all_word)
						print("ОПРЕДЕЛЯЕМ ТОЛЬКО ОСМЫСЛЕННЫЕ")
						smysl=slovarny(all_word)
						print(smysl)
						print(i)
						cecs.append(smysl)

	elif len(maximum_in_group)==5:
		for i in maximum_in_group[0]:
			for k in maximum_in_group[1]:
				for l in maximum_in_group[2]:
					for m in maximum_in_group[3]:
						for n in maximum_in_group[4]:
							all_word = rezak((i,k,l,m,n))
							print("ОПРЕДЕЛЯЕМ ТОЛЬКО ОСМЫСЛЕННЫЕ")
							smysl=slovarny(all_word)
							print(smysl)
							print(i)
							cecs.append(smysl)

	elif len(maximum_in_group)==6:
		for i in maximum_in_group[0]:
			for k in maximum_in_group[1]:
				for l in maximum_in_group[2]:
					for m in maximum_in_group[3]:
						for n in maximum_in_group[4]:
							for o in maximum_in_group[5]:
								all_word = rezak((i,k,l,m,n,o))
								print("ОПРЕДЕЛЯЕМ ТОЛЬКО ОСМЫСЛЕННЫЕ")
								smysl=slovarny(all_word)
								print(smysl)
								print(i)
								cecs.append(smysl)

	elif len(maximum_in_group)==7:
		for i in maximum_in_group[0]:
			for k in maximum_in_group[1]:
				for l in maximum_in_group[2]:
					for m in maximum_in_group[3]:
						for n in maximum_in_group[4]:
							for o in maximum_in_group[5]:
								for p in maximum_in_group[6]:
									all_word = rezak((i,k,l,m,n,o,p))
									print("ОПРЕДЕЛЯЕМ ТОЛЬКО ОСМЫСЛЕННЫЕ")
									smysl=slovarny(all_word)
									print(smysl)
									print(i)
									cecs.append(smysl)

	elif len(maximum_in_group)==8:
		for i in maximum_in_group[0]:
			for k in maximum_in_group[1]:
				for l in maximum_in_group[2]:
					for m in maximum_in_group[3]:
						for n in maximum_in_group[4]:
							for o in maximum_in_group[5]:
								for p in maximum_in_group[6]:
									for r in maximum_in_group[7]:
										all_word = rezak((i,k,l,m,n,o,p,r))
										print("ОПРЕДЕЛЯЕМ ТОЛЬКО ОСМЫСЛЕННЫЕ")
										smysl=slovarny(all_word)
										print(smysl)
										print(i)
										cecs.append(smysl)
	print(cecs)
	end = time.time()
	print(end - start, 'seconds')
	input("lol kek cheburek")






def durackiy_search(list, item):
    if item in list:
        return list.index(item)

text_file = open("slovarik.txt", 'r', encoding= 'utf-8')
slovar = text_file.readlines()
text_file.close()
slovar = list(map(str.strip,slovar))
# start = time.time()
# print(durackiy_search(t, 'слон'))
# end = time.time()
# print(end - start, 'seconds')
# print(binary_search(t, 'слон'))
# lastend = time.time()
# print(lastend - end, 'seconds')
main()

input("")
