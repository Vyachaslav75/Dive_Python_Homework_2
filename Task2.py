from fractions import Fraction
import math
num1 = ''
while num1 != 'Q':
    print('Введите две строки вида “a/b”,  для выхода введите Q вместо первой дроби')
    num1 = input('Введите первую дробь вида a/b: ')
    if num1 == 'Q':
        break
    num11, num12 = num1.split('/')
    num2 = input('Введите вторую дробь вида a/b: ')
    num21, num22 = num2.split('/')
    if num11.isdigit() and num12.isdigit():
        num11 = int(num11)
        num12 = int(num12)
        if num21.isdigit() and num22.isdigit():
            num21 = int(num21)
            num22 = int(num22)
            if num12 != num22:
                res1 = num11*num22+num21*num12
                res2 = num12*num22
                
            elif num12 == num22:
                res1 = num11 + num21
                res2 = num12
                
            print(math.gcd(res1, res2))
            temp = math.gcd(res1, res2)
            if temp > 0:
                res1 = res1 // temp
                res2 = res2 // temp
                
            if res1 // res2 > 0 and res1 % res2 == 0:
                print(f'Сумма дробей равна: {res1//res2}')
            else:
                print(f'Сумма дробей равна: {res1}/{res2}')
            print(f'Проверка с помощью Fraction {Fraction(num11, num12) + Fraction(num21, num22)}')
            res1 = num11 * num21
            res2 = num12 * num22
            temp = math.gcd(res1, res2)
            if temp > 0:
                res1 = res1 // temp
                res2 = res2 // temp
            
            if res1 // res2 > 0 and res1 % res2 == 0:
                print(f'Произведение дробей равно: {res1//res2}')
            else:
                print(f'Произведение дробей равно: {res1}/{res2}')
            print(f'Проверка с помощью Fraction {Fraction(num11, num12) * Fraction(num21, num22)}')
        else:
            print('Вторая дробь введена неверно')
    else:
        print('Первая дробь введена неверно')

        result = ''
