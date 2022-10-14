import check as ch
from typing import Union

def get_result (first: Union[ float, complex] , second: Union[ float, complex], operator) -> Union[int, float, complex]:
    operators = {
                '*': lambda x,y : x*y,
                '/': lambda x,y : x/y,
                '+': lambda x,y : x+y,
                '-': lambda x,y : x-y,
                }
    if operator == '/':
        ch.check_zerodivision(first,second)
        return operators.get(operator)(first,second)
    else:        
        return operators.get(operator)(first,second)
         
