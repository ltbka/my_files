# list_ = ['abc',1,2,3]
# count = 0
# for i in list_:
#     count += 1
# print(count)


# str_ = 'abcde'
# count = 0
# for i in str_:
#     count += 1
# print(count)


# def my_len(obj):
#     count = 0
#     for element in obj:
#         count += 1
#         print(count)
        
# str_ = 'abcde'
# list_ = ['abc', 1,2,3]

# my_len(str_)
# my_len(list_)

""""
Функции - это именнованный блок кода ,который выполняет одну задачу и может принимать в себя аргументым возврощает какое то значение 
Функции можно вызывать много раз ,оброщаясь по имени 

def - ключевое слово , указывает puthon что мы хотим создать функцию 
название функции - это пременная , под этим именем puthon запоминает название этой функции 
скобки - нужны для того , что бы функция могла принимать параметры
"""

"""синтаксис"""

# def название_функции(параметры):
#     принимаем аргументы для работы в теле название_функции
#     тело_функции
    
# название функции(аргументы )

# def my_sum(x,y):
#     print(x + y)
     # return x + y

# my_sum(5,6)
# my_sum(11,2)
# my_sum('a','b')
# my_sum(9,0)

# res = my_sum(5,6)
# print(res, 'res')

"""
return - используется для возвращения результата и на этом моменте функции завершает свою работу 
return - это ключевое слово , которое дает поонять puthon что за этой командой будет какая то информации которая является окончательным результатом нашей функции 
"""

# def sum_two_number(a,b,c=9):
#     print(a,b,c)

# sum_two_number(5,6)TypeError: sum_two_number() missing 1 required positional argument: 'c

# sum_two_number(1,2,3) - позиционые аргументы 
# sum_two_number(c=2, a=2, b=2) - именованные аргументы


# sum_two_number(4, b=3 4)

""""
распаковка
"""

# list = list(range(1,11))
# print(list1)
# list1 = [*range(1,11)] #распаковка значение на новый список
# print(list1)

# dict1 = {'a':1, "b":2,"c":3}
# dict2 = {**dict1}
# list3 = {*dict1}
# print(dict2)
# print(list3)


""""
необязательные аргументы args args, kwargs
args - принимает позиционные аргементы
kwargs - принимает именнованные аргументы 

args - tuple
kwargs - dict
"""

# def two_sum(a,b, *args, **kwargs):
#     print(a,b)
#     # print(args)
#     # print(kwargs)
#     return a + b + sum(args) + sum(kwargs.values())
    
# print(two_sum(2,2,2,5,10,2,14,2,2,2,1,1,8,8,9,first=100, second=200, third=300,four=400))


# def func(a,b=10, *args, **kwargs):
#     print('a ', a)
#     print('b ', b)
#     print('args --',args)
#     print('kwargs --', kwargs)
    
#func(5)
#func(5,12)
#func(40,50,60,70,80)
# func(10,15,20,hello='hello world')
# func(10,c=5,d=[1,2,3], e=True,f=None)


# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)

# print(func())


""""
Анотации - делают код более информативным
"""

# a = 5
# a = 'str'
# a= list()
# a = dict()

# num: int = 10
# str_: str = 'hello'


# def func(a, b:int,c:int) -> int:
#     """
#     hello wirld rhic sum func
#     """
#     print(a+b+c)
    
# func(1,2,3)
# list.append()


# list_ = ['olo','lol','world','aziza']

# def palindrom(words: list) -> list:
#     palindrom1 = []
#     for word in words:
#         if word == word[::-1]:
#             palindrom1.append(word)
#         else:
#             continue
#     return palindrom1

# print(palindrom(list_))

# дан словарь удалите из него все элементы с пустыми значениями 


# a = {'a':1, 'b':2, 'c':None, 'e':3, 'd':None}

# def func(obj:dict) -> dict:
#     dict_ = {}
#     for key,value in obj.items():
#         if value == None:
#             pass
#         else:
#             dict_[key] = value
#     return dict_
        
# print(func(a))

# def validate_email(email:str) -> bool:
#     index = email.find('@')
#     if '@' not in email:
#         raise Exception ('Invalid email')
#     elif not email[o:index]:
#         raise Exception('Invalid email')
#     elif email[index+1] not in domains:
#         print(email{index+1:})
#         raise Exception(f'Invalid email domain {domains}')
#     print("Email is valid and sucessfully saved")
#     return True


# def register(email:str, password1: str, password2:str) -> dict:
#     db_email = None
#     password = None
#     if validate_email(email):
#         db_email=email
#     if password1 != password2:
#         raise Exception('пароли не совподают')
#     password = password1
#     msg = 'Вы успешно зарегестрировались '
#     return{'email':email, 'password':password[::-1], "msg":msg}

# email = input('введите почту ')
# password1 = input('введите пароль ')
# password2 = input('подтвердите пароль ')
# print(register(email=email,password1=password,password2=password2))

# string = ([1,2,3,45])
# print(string)