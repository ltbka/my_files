# циклы

# цикл- это блок кода , который повторяется определенное количество раз или работает бесконечно

# for - цикл,который работает с итерируемыми обьектами и закончит свою работу на последнем элементе
    
# while - цикл , который работает пока условие вер


# while True -  пока правда
# после while идет условие цикла и пока это  условие верно ,то цикл будет работать

# остановить цикл можно комбинациями  ctrl + c или ctrl + z




# counter = 0 
# while True:
#         counter += 1
#         print(counter)

# count = 0
# while count !=101: #--пока count не равен 101
#     print(count)
#     count += 1
# print('end')


# count = 10
# while count != 0:
#     print(count)
#     #count -=1
#     count = count - 1
# 10 9 8 7 6 5 4 3 2 1 end
# print('end')

# a = 0
# while a:
#      print('hello')


# не отработает потому что условие False

# for i in range (1,10):
#     print(i+1)
# [1,2,3,4,5,6,7,8,9]
# print(i)


# for i in 12345:
#     print(i) --> int' object ic not iterable
# тип данных int неинтерируемый обьект

# num = 12345678
# sum = 0
# for i in str(num):
#     # sum += int(i)
#     sum = sum + 1
# print(sum)

# string = 'hello'
# string = 'world'
# for i in range(len(string)):
#     0 string[0] string1[0]

# пример создание бесконечного  цикла с помощью for

# list_ = [1,2,3]
# for i in list_:
#     print(i)
#     list_.append('hello')

# ключевые слова в циклах


# break - полностью выйти из цикла досрочно прерывает цикл

# continue - перейти к следующей итерации

# for i in range(10):
#     if i == 3:
#         continue
#     print(i)

# i = 0
# while i < 6:
#     if i == 3:
#         break
#     else:
#         print(i)
#         i += 1

