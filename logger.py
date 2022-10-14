import datetime as dt
def log_value_input(value):
    log_time = dt.datetime.now().strftime('%H:%M')
    with open('Python/HW-PY_7/Calc_log.csv','a') as log:
        log.write ('\n {};Введено значение:;{}\n'.format(log_time, value))
    
def log_operator_input(value):
    log_time = dt.datetime.now().strftime('%H:%M')
    with open('Python/HW-PY_7/Calc_log.csv','a') as log:
        log.write ('\n {};Введен оператор:;{}\n'.format(log_time, value))
def log_result(value):
    log_time = dt.datetime.now().strftime('%H:%M')
    with open('Python/HW-PY_7/Calc_log.csv','a') as log:
        log.write ('\n {};Результат работы калькулятора:;{}\n'.format(log_time, value))

