# lambda - анонимная функция(та же самая функция но без названия)

# lambda  парметр : что функция возврощает

# def add_nums(a,b):
#     return a + b

# print(add_nums(5,2))

# result = lambda a,b : a + b

# print(result(5,2))

# x = lambda a,b,c : (a * b) % c
# print(x(5,7,10))

# get_keys = lambda x : x.keys()
# dict_ = {1:2, 3:4, 5:6, 7:8}
# print(get_keys(dict_))

# get_last = lambda ls: ls[-1]
# list1 =  [1,2,3,4,5]
# print(get_last(list1))


# map (function,itarable) функция которая принимает функцию и итерирыемый обьект 
# она принимает функцию к каждому элементу в iterable

# mag_gen = map(int, ['1','2','3','4'])
# print(tuple(map_gen))

# nums = [1,2,3,4,5]

# def square(number):
#     return number * number

# map_function = map(square, nums)

# print(square(2)) #4

# func = lambda e: e+1
# res = []
# for e in [1,2,3,4,5]:
#     res.append(func(e))
# print(res)


# filter(function, iterable) -  функция , принимает первым аргументов другую функцию и итерируемый обьект
# результатом будет последовательлность  которые прошли условия filter

# nums = [1,2,3,4,5,6,7,8,9,10]

# def filter_nums(number):
#     if number % 2 == 0:
#         return True
    
    
# result = list(filter(filter_nums, nums))
# print(result)

# filter_nums = lambda nums: nums % 2 == 0
# print(list(filter(filter_nums, nums)))

# res = list(filter(lambda num: num % 2 == 0, nums))
# print(res)


# list_ = ['Эртай', 'Оомат', 'Арген' , 'Манас', 'Бекзат', 'Даниэль', 'Эркайым']

# def startwith_vowels(name):
#     vowels = 'АДБФЫДЬВСЯ'
#     print(tuple(vowels))
#     return name.upper().startwith(tuple(vowels))

# print(startwith_vowels('Мариям'))

# reduce -  эта функция принимает функцию и возвращает 1 результат
# (ее убрали из стандартроной библиотеки питона так как ей нашли замену SUM MAX)
 
# from functools import reduce
 
# lst = [1,2,3,4,5]

# result = reduce(lambda x, y : x +y, lst)
# print(result)

# lst = [1,2,3,4]

# def mul(a,b):
#     return a * b

# res = reduce(mul, lst)
# print(res)


# enumerate(iterable, [start - с какого наичнать элемента по дефолту 0])
# функция принимает последовательность возвращет tuple  состоящий из чисел и элемента

# lst = ['a','b','c','d']

# for i in enumerate(lst):
#     print(i)
    
    
 
#  lst = ['a','b','c','d']
 
# for i in enumerate(lst, 10):
#     print(i)

# list_ = ['one','two','three']
# res = list(enumerate(list_,1))
# print(res)

# zip(iterable, iterable.......)  сопостовляет  каждый эдлемент из  iterable  со следующим

# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d']
# print(dict(zip(list1, list2)))

# any(iterable) -  возвращает  True если хотя бы один элемент  в itebale имееет значение True

# my_list = [False,0,False,False]
# print(any(my_list))

# all(iterable) возворащает True  если все элементы являются True


# my_list = [True,True,True,True]
# print(all(my_list))



'''изменить тип данных значений'''

# dict_ = {1: 2, 3: 4, 5: 6}

# res = list(map(lambda x: str(x), dict_.values()))
# print(res)


# """задача при помощи map() заменить значение чисел словами четное.нечетное"""
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# res = dict(map(lambda x: ''))
# print
 
 