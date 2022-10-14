import sys
import logger

def check_value (input_value, value_type):
    '''Проверка на ввод рационального числа (отсустствие букв) и комплексного числа (оканчивается на j)'''
    if value_type == 1:
        while is_digit(input_value) == False:
            input_value = input('Введены буквы, повторите ввод рационального числа:\n\t')
        input_value = float(input_value)
        return input_value
    else:
        while len(input_value) > len(''.join(list(filter(lambda char: char.isdigit() or char.lower() in '+-j' , input_value)))) or len(input_value) == 0:
            input_value = input('Ввод комплексного числа осуществлен не по маске "a+-bj"\n\tОбязательны для ввода А, оператор, B и "j" на конце:\n\t')
        return complex(input_value.lower()) 

""" 
В данном режиме не задействован
def check_expression (operands , operators):
    '''Проверка корректности выражения для вычисления'''
    return True if len(operands) > len(operators) else False
"""
def check_operators (input_value):
    '''Проверка на ввод операторов'''
    while (len(input_value) == 1 and any(filter(lambda char: char in '-+/*', input_value))) == False:
        input_value = input('Введите оператор из перечня "-+/*":\n \t')
    return input_value

def is_digit(string):
    '''Вспомогательная проверка строки на возможность преобразования в Float'''
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False    
def check_zerodivision (dividend, divider):
    
    try:
        dividend / divider
    except ZeroDivisionError:
        result ='Упс, деление на ноль'
        logger.log_result(result)
        sys.exit()


    
""" 

print (687/4 / (3-5j))
print (  (3-5j)/687/4)
print (  (3-5j)*4/687) """