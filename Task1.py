hex_array = ['0', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
num = ''
while num != 'Q':
    print('Введите число для выхода введите Q')
    num = input('Введите число: ')
    if num.isdigit():
        num = int(num)
        temp = num
        result = ''
        while num > 0:
            result = hex_array[num % 16] + result
            num = num//16
            print(num)
        print(f'Шестнадцатиричный вид: {result}')
        print(f'Проверка функцией hex: {hex(temp)}')
    elif num != 'Q':
        print('Число введено не верно')
