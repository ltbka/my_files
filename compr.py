# comprehension -  генерация последовательностей в одну строку используя цикл 
# так же его называют синтаксическим сахаром



# index = 0

# dor i in raange(1,10:)
# index += 1
# index = index + 1

# основной целью использования как list, dict comprehension является упрощение и повышение читаемости кода


# list comprehension -   это упрощенный подход к созданию списка , который задействует цикл for 
# а также мф можем использовать if  else операторы
# под капотом генератор списка также 


# list_ = []
# for i in range (1,11):
#     list_.append(1 ** 2)
# print(list_)

# list_ =(i **2 for i in range(1,11))
# print(list(list_))
      

# list_ = []
# for i in range (1,11):
#     list_.append(i **2)
# print(list_)


# результат for элемент in итерируемый обьект

# import time 

# start_time = time.time()
# list2 = [for i in range (100)]
# time2 = time.time() - start_time1
# print(time2)

# list_ = []
# for i in range(1,11):
#     if not i % 2:
#         list_.append(i)
# print(list_)

# list_ = [ i for i in range(1,11) if not i%2]
# print(list_)

# list_ = ['нечетное' if i % 2 else 'четное' for i in range(1,11)]
# print(list_)

# list1 = [1, 'hello', 2, 'a', 4.0, '7', 8]

# a = ['нечетное' if i % 2 else 'четное' for i in list1 if type(i) == int or type(i) == float]
# print(a)

# set comprehions
# разница с list comprehision что выходные данные 



# dict comprehension - аналогично создаются , но обязательно нужно указывать key:Value

# squaeres = {i: i ** i for i in range(10)}
# print(squaeres)

# dict_ = {}
# for i in range(10):
#     dict_.update({i: i **i})
# print(dict_)

# list_ = [1,2,3,4,5,6,7,8]

# dict_ = {i: list_.count(i)for i in list_}
# print(dict_)


# list1 = {1,2,3,4,5}
# list2 = ['a', 'b','c','d','e']

# dict_ = {list1[index]:list2[index] for index in range(len(list1))}

# print(dict_)

# dict1 = [ 'a': 1, 'b': 2,'c':3 ]

# dict2 = {key: value for key, value in dict1.items()}

# dict1 = {
#     "a":[1,2,3,4,5],
#     "b":[10,30,2,5],
#     "c":[74,28,47],
#     "d":[4,6,2,92,9]
#     }

# dict2 = {key: sum(value) for key,value in dict1.items()}
# print(dict2)

# 'создайте список ,состоящий из 10 списков ,в которых строка "helloworld" повторяется по 5 раз'

# list_ = [['hello world' for i in range(5)]for i in range(10)]
# print(list_)


# hachtags =['#makers#bootcamp#программирование#it#курсы']
# list = hachtags.split('#')[1:]
# print(list)

# list_ = []
# list_ = []

# n = int(input('Введите количество слов: '))

# for i in range(n):
#     word = input('Введите слово: ')
#     word_list.append(word)
#     length_list.append(len(word))

# print('Список слов:', word_list)
# print('Список длин:', length_list)