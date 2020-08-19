first_number = float(input('Введите первое число: '))
second_number = float(input('Введите  второе число: '))
operation = input('Введите операцию: ')

a = first_number
b = second_number
c = operation

if (a == 0 and c in ('mod', '/', 'div')):
    print('Деление на 0!')
elif c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
elif c == 'mod':
    print(a % b)
elif c == 'pow':
    print(a ** b)
elif c == 'div':
    print(a // b)
else:
    print('НЕ верно введённые данные')




