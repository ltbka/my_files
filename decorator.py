# def decor_func(func): #должен принимать функцию
#     print('decor func')
#     return func()

# def func():
#     print('func2')
#     return 'hello'

# res = decor_func(func)
# print(res)


# декаратор - это функция который принимает другую функцию
# Декоратор является высшего порядка это функция которые могут принять как аргумент другую функцию и вернуть ее 
# Декоратор модификцирвует  и улучшает принутую функцию и выдает изменную 

# def func2(func):
#     print('Я буду работать до функции func1')
#     print(func())

# def func1():
#     return 'Функция deco завершилось'


# func2(func1)

# def to_upper(f):
#     def wrapper():
#         original_res = f()
#         modified_res = original_res.upper()
#     return wrapper

# @to_upper что бы быстрее вызвать декорации
# def some_words():
#     return 'Hello World'

# def some_words1():
#     return 'hello kyrgyzstan'

# print(some_words())



# def get_name(name):
#     return name

# def get_age(age):
#     return age

# def get_last_name(last_name):
#     return last_name

# print(get_name('john'))
# print(get_age(14))
# print(get_last_name('Snow'))


# def decorator_func(func):
#     def wrapper(some_info):
#         return 'Вы Передали: ' + str(func(some_info))
#     return wrapper

# @decorator_func
# def get_name(name):
#     return name

# @decorator_func
# def get_age(age):
#     return age

# @decorator_func
# def get_last_name(last_name):
#     return last_name

# print(get_name('Name'))




























# def func_def(function_to_decorate): #сюда попадает функция которую нужно задекорировать 
#     def wrapper(): # оберточная оболочка для функции
#         print('Я код , который отрабатывает до вызова функции!!!')
#         function_to_decorate()
#         print('А я код который сработает после!!!')
#     return wrapper # возвращаем обертку

# @func_def
# def func1(): # функция которую мы задекорируем
#     print('Я функция func1')

# res = func_def(func1)



# если мы используем аргументы у функции , то мы обьязательно должны передать их в редактор 


# def decorator(func): # лучше использовать такую запись , она является универсальной для всех функций 
#     def wrapper(*args, **kwargs):
#         print(f'здесь аргс {args}')
#         print(f'здесь кваргс {kwargs}')
#         func(*args, **kwargs)
#     return wrapper

# @decorator
# def func_winhout_parametrs():
#     print('функция без параметров')
 
# @decorator   
# def func_with_parametrs(first_name , last_name):
#     print('функция с параметрами')
#     print(f'hello {first_name}{last_name}')

# @decorator
# def func_with_parametrs_kwargs(first_name , last_name):
#     print('функция с параметрами')
#     print(f'hello {first_name}{last_name}')


# func_without_parametrs()
# func_with_parametrs()
# func_with_parametrs_kwargs(first_name='john', last_name='snow')

# def div(func):
#     print('f1')
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         return "<div>" + func(*args, **kwargs) + "</div>"
#     return wrapper

# @div
# def get(name, last_name):
#     print('f2')
#     return name + last_name

# print(get('John','Snow'))   

# def bread(func):
#     def wrapper(*args, **kwargs):
#         return 'bread' + str(func(*args, **kwargs)) + 'bread'
#     return wrapper

# def ingredients(func):
#     def wrapper(*args, **kwargs):
#         return 'tomato' + str(func(*args, **kwargs)) + 'salad'
#     return wrapper

# @bread
# @ingredients
# def get_sandwich(x):
#     print(x)
#     return x

# print(get_sandwich('sasusage'))

# def decorate_maker(f):
#     print(f)
#     print(f' Я создаю декораторы')
#     def my_decorator(func):
#         print('Я декоратор , я буду вызван в момент декорации функции')
#         def wrapper():
#             print('Я функция обертка ,вызываюсь каждый раз при декорации функции')
#             return func()
#         print('Я возвращаю обертную функцию')
#         return wrapper 

# @decorator_maker(2)
# def decorate_finction():
#     print('Я декорированная функция')
    
# decorate_function()


# def bencmark(func):
#     import time
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time
#         func()
#         end = time.time
#         print(f'функция отработала: {end - start}')
#     return wrapper

# @bencmark
# def call_webpage():
#     import request
#     webrage = request.get('https://google.com')
    
# @bencmark
# def iterate _list():
#     for i in range()














































