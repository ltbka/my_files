a = int(input('Введите значение 1:  '))

b = int(input('Введите значение 2:  '))


try:

a = float('a')

b = float('b')

print('a + b')

except ValueError:

print(str(a) + str(b))

else:

print(f'Все верно, вы ввели оба числа {a} и {b}')

finally:

print('Программа завершена')
