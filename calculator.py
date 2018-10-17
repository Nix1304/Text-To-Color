import sys

print('Доступные действия: "+", "-", "/", "*", "ˆ"')
operator = input('Введите действие:\n')
if operator not in ('+', '-', '/', '*', 'ˆ'):
    print('Действие недопустимо!')
    sys.exit(1)
a = int(input('Введите первое число:\n'))
b = int(input('Введите второе число:\n'))

ret = 0
if operator == '+':
    ret = a + b
elif operator == '-':
    ret = a - b
elif operator == '*':
    ret = a * b
elif operator == '/':
    ret = a / b
elif operator == 'ˆ':
    ret = a ** b

out = '{} {} {} = {}'.format(a, operator, b, ret) if operator != 'ˆ' else '{}ˆ{} = {}'.format(a, b, ret)
print(out)
f = open('history.txt', 'a')
f.write(out + '\n')
f.close()
