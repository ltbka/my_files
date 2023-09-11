# set()-множества
# это неизменяемый тип данных ,неупорядоченный ,интерируемый тип данных ,неиндексируемый тип данных
# хранит только уникальные значения ,хранять только неизменяемый тип данных


# set1 = 
# set2 = {} -- так создаются словари
# set1 =
















# set1 = {1,2,3,(1,2,3,[1]),'s'}
# print(set1) --> unhashable tupe: 'list'

# добавление элементов

# add(element)
# update(sequense)

# my_set = {1,2,3}
# my_set.add(3)
# my_set.add('hello')
# my_set.add({1,2,3})
# print(my_set)




# clear()
# my_set,clear

# remove()- удаление элемент ,если такого элемента нет , то выдает ошибку

# my_set = {1,2}
# my_set.remove(4) ---> KeyError: 4

# discard()-- 

# pop()- удаляет случайный элемент из set() и возвращаet

# difference-
# set)a.difference(set_d)


# for i in range(10):
#     ptint(i)
#     for j in range(10):
#         ptint(j)
#         if j == 5
#             break
#         if i == 2:
#             break














from os import set_blocking


# intersection -- выводит похожие элементы из  set_a  set_b
# set_a & set_b




# union -  соединяет множетсва
#
# a = {1,2}
# b = {3,4}
# new_set = a.union(b) новая пременная
# print(a)
# print(a |  b)



# list_ = [2,1,3,6,2,5,2,8,2]
# while 2 in list_:
#     list_.remove(2)
# print(list_)

# else 
# else - примененное в цикле for и while, проверяет, был ли произведен выход из цикла с помощью 
# break , или же естественным образом
# else  срабоатет если выход из цикла был совершен без помощи break

# for i in 'hello world':
#     if i == 'a':
#         break
# else:
#     print(num)


# dict1 = {"a": 1, "b": 2,"c": 3,"d": 4}

# for key in dict1:
#     print(key)

# dict1 = {"a": 1, "b": 2,"c": 3,"d": 4}

#  for key in dict1:
#      print(dict1.get(key))
     
# dict1 = {"a": 1, "b": 2,"c": 3,"d": 4}

# for key in dict1:
#     print(key)

# dict1 = {"a": 1, "b": 2,"c": 3,"d": 4}

# for irems in dict1.items():
#     key = items[0]
#     value = items[1]
    
# for a,b,c, in [(1,2,3),(4,5,6),(7,8,9)]:
#     print(a,b,c)

# while True: 

# operator = input("enter operator + - / *: ")
# num1 = int(input("enter your first number: "))
# num2 = int(input("enter your second number: "))
# if operator == "+":
#       print(num1 + num2)
# elif operator == "-":
#       print(num1 - num2)
# elif operator == "*":
#       print(num1 * num2)
# elif operator == "/":
#      print(num1 / num2)
     
# while True:

# operator = int(input("enter operator + - / *: "))
#  num1 = int(input("enter your first number: "))
#  num2 = int(input("enter your second number: "))
#   if operator == "+":
#       print(num1 + num2)
#   elif operator == "-":
#       print(num1 - num2)
#   elif operator == "*":
#       print(num1 * num2)
#   elif operator == "/":
#       print(num1 / num2)
      
#       exit  = input('Do you want continue! Yes or No`)
#       if exit.lower() == 'yes':
#         continue
#     elif exit.lower() == 'no':
#         pirnt('bye bye')
#         play = Falsewhile True: 

# Попросите студентов написать программу, которая запрашивает у пользователя пароль и проверяет его на соответствие определенным требованиям. Пароль считается валидным, если он:

# Содержит как минимум 8 символов.
# Содержит хотя бы одну заглавную букву.
# Содержит хотя бы одну строчную букву.
# Содержит хотя бы одну цифру.
# Содержит хотя бы один специальный символ (например, !, @, #, $ и т.д.).

# while True: 
#     password = input('password')

#     elif len(password) < 8:
#        print("Пароль должен содержать минимум 8 символов")
#        continue
#     elif password.islower() == True:
#       print("Пароль должен содержать хотя бы одну заглавную букву")
#       continue
#     elif password.isupper() == True:
#       print("Пароль должен содержать хотя бы одну строчную букву")
#       continue
#     elif password.isalpha() == True:
#      print("Пароль должен содержать хотя бы одну цифру")
#      continue
#     elif password.isalnum() == True:
#      print("Пароль должен содержать хотя бы специальный символ (напримерб, !,@,#,$,и т.д.)")
#      continue

# print(password)
# break



# Дана строка. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная, 
# то длина первой части должна быть на один символ больше). Переставьте эти две части местами,
# результат запишите в новую строку и выведите на экран.
  