import controller as c

while True:
    escape_key =input ('\n\t  Добро пожаловать в калькулятор\n\tВозможно производить следующие операции:' +
                        '\n\t\tСложение\n\t\tВычетание\n\t\tУмножение\n\t\tДеление\n\tСо следующими типами чисел:' +
                        '\n\t\tРациональне\n\t\tКомплексные' +
                        '\n\tДля продолжения - любой ввод\n\tДля завершения работы - "q"\n\t')
    if escape_key.lower() == 'q':
        print('Спасибо, до скорых встреч')
        break
    else:
        c.start()