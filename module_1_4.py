my_string = input('Введите ваше ФИО: ')
print('Введено', len(my_string), 'символов')

print('Введенные символы в большом регистре: ')
print(my_string.upper())

print('Введенные символы в малом регистре: ')
print(my_string.lower())

print('Все пробелы удалены:')
print(my_string.replace(' ', ''))

print('Первый введенный символ:')
print(my_string[0])

print('Последний введенный символ:')
print(my_string[-1])
