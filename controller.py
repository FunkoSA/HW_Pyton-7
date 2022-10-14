import user_interface as ui
import calc_operations as c_op
import logger

def start():
    first_operand = ui.get_mumber(1)
    second_operand = ui.get_mumber(1)
    operator = ui.get_operator()
    calculate = c_op.get_result(first_operand,second_operand,operator)
    logger.log_result(calculate)
    ui.view_result(calculate)