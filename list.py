# numbers = [1,2,3,4,5]
# print(numbers[2])

# string = [mariiam]
#print(string)

# numbers = [5]*5
# print(numbers)

# numbers1 = [5,5,5,5,5]
# numbers = list (range(10,2,-1))
# print(numbers)


# numbers = [2,5.1'makers'] 
# где numbers это перкменная
# =- это присваивание
# []-это  лейтэрал списка
# 2 это числовой тип данных (int) или  (integer) 
# 5.1  это десятичное число  ( float)
# 'makers'это строчный тип данных(str)(string)

# a = 2
# a == 2 
# if a < 2:
#     print('yes')
# else:
#     print('no')

# создать программу которая пропускает людей в клуб по возрасту если  людям  >18 вход свободен , если им от 12-15 вход со взрослыми если <12 вход запрещен

#  user = int(input('Введите свой возраст: '))
#     if user >= 18:
#     print('добро пожаловать')
# elif user >= 12  and user <= 15:
#     print('вход со взрлосным')
#  else: 
#     print('вход запрещен')


# tuple

# кортеж - неизменяемый тип данных,индексируемый,упорядочный,итерируемый,
# предназначенный для хранения любых данных (в целом не отличаются от списков , просто их нельзя изменить и они занимают меньше памяти чем списки)


# tuple_= tuple()
# print(tupe(tuple_))

# tuple1 = (1,2,3)

# tuple1 = (1,2,3,[1,2,3,],{'a':1})
# tuple1[3].append(4)
# print(tuple1)

# методы tuple

# count считает количество элементов

# tuple1 = (1,2,3,4,5,6,,7)

# print(tuple1.count(1))


# index - возврощает индекс первого вхождения

# tuple1 = (1,2,3,4,5,6,7,8,3)
# print(tuple.index(3, 4))

# for element in tuple1:
#     if tupe(element) == list:
#         element.append(2)
        

# тип данных словари (dict)

# dict = dict([('key1':'value1'),('key2','value2')])
# print(dict2)

# dict2 = dict([('key','value')])
# print(dict2)

# dict3 = dict(['ab','cd','de'])
# print(dict3)

# dict4 = dict()
# dict4['key1'] = 'value'
# print(dict4)

# dct = dict(age=25)
# print(dct)
# dct['age'] = 26
# print(dct)

# dict.clear()- очищает словарь


# copy()-возвращает копию словаря


# fromkeys[object,value]- создает словарь с ключами из  object  и звчем  value  для всех ключей 
# если не передать value то значение у всез ключей будет None

# Mетоды получения элементов словаря

# get(key,default)-возвращает значение по этому ключу

# dict_= {'name':'atai','age':25}
# print(dict_.get('ag',' нет такого ключа'))  #-- выдает  N

# update - добавляет новый словарь в наш словарь

# setdefault -  получение значений
# работает точно также как  get() но если такого ключа нет он создаст новую парк

# values()-   выводит значения которые есть в словаре

# 

# items()-  выводит все ключи и значиние в словаре

# удаление элементов

# pop ,(key [massege])
# удвляет пару ключи и значение и возвращает значение,если  ключа нет то возвращает  message
# ( по умолчанию приходит ошибка
 
# popitem() ->  удаляет и возврощает пару ключ значение
# yдаляет последнюю добавленную пару  

# dict = {'a': 1,'b': 2,'c': 3,'e': 4,'d': 5,'y': 6}
# for key,value in dict_.items():
#      if value % 2 == 0:
#          dict_[key] = 0
         
# print(dict_)

 # если значение ключа четное то вам нужно поменять его на новое значение 0
 
# dict_= {'hello':None,'puthon':None,'javascript':None,'makers':None}
# for key,value in dict_keys():
#      print(key,'ключ')
#      dict_[key] = len(key)
 
# dict_ = {'John': 60,'Jack': 70,'Anton': 85,'Beka': 81,'Nastya':93}
# avarage-ocenka = 0
# for  value in dict_.values():
#     avarage_ocenka += value
    
# avarage = avarage_ocenka / len(dict_)
# dict_['avarage'] = avarage
# print





 