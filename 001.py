# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

num_week = int(input('Введите номер дня недели - '))

if num_week == 6 or num_week == 7:
    print('ДА')
else:
    print('Нет')
