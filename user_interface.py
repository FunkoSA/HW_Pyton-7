from ast import operator
import check as ch
import logger
def get_mumber(number_type):
    '''Функция получения операндов для последующего вычисления'''
    number_type = input('Для ввода рационального числа введите "1" \nДля комплексного - любой ввод\n')
    if number_type == '1':
        num = ch.check_value(input (f'Введите рациональнове число: \n'),int(number_type))
        logger.log_value_input(num)
        return num
    else:
        num = ch.check_value(input (f'Введите комплексное число в формате "a+bj": \n'),number_type)
        logger.log_value_input(num)
        return num
    

def get_operator ():
    '''Функция получения оператора для последующих вычислений'''
    operator = ch.check_operators(input(f'Ведите операцию\n \tДля сложения "+"\n \tДля вычитания "-"\n \tДля умножения "*"\n \tДля деления "/"\n \t'))
    logger.log_operator_input(operator)
    return operator

def view_result(data):
    '''Функция вывода результата'''
    print(f'Результат вычислений:\n{data}')
