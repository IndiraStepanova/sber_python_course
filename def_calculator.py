#вводим константы
OP_NOT_DEFINED = 'operation not defined'
OP_POW = 'pow'
OP_PERCENTS = 'perc'
OP_ADD = 'add'
OP_DIFF = 'diff'
OP_MULT = 'mult'
OP_DIV = 'div'

#определяем знак в вводимом пользователем выражении
def GetOperationType(operation: str) -> int:
    if operation.find("**") >= 1:
        return OP_POW
    elif operation.find("%") >= 1:
        return OP_PERCENTS
    elif operation.find("+") >= 1:
        return OP_ADD
    elif operation.find("-") >= 1:
        return OP_DIFF
    elif operation.find("*") >= 1:
        return OP_MULT
    elif operation.find("/") >= 1:
        return OP_DIV
    return OP_NOT_DEFINED

#функции определяющее отдельное выражение
def Pow(pow_operation: str):
    arr = pow_operation.split('**')
    a = int(arr[0])
    b = 2
    if arr[1] != "":
        b = int(arr[1])
    print(pow(a,b))
    return

def Percents(percents_operation: str):
    arr = percents_operation.split('%')
    a = int(arr[0])
    print(a/100)
    return

def Add(add_operation: str):
    arr = add_operation.split('+')
    a = int(arr[0])
    b = int(arr[1])
    print(a+b)
    return

def Diff(diff_operation: str):
    arr = diff_operation.split('-')
    a = int(arr[0])
    b = int(arr[1]) 
    print(a-b)
    return

def Mult(mult_operation: str):
    arr = mult_operation.split('*')
    a = int(arr[0])
    b = int(arr[1]) 
    print(a*b)
    return

def Div (div_operation: str):
    arr = div_operation.split('/')
    a = int(arr[0])
    b = int(arr[1]) 
    if b != 0:
        print(a/b)
    else:
        print('Division by zero')
    return

#находтим операцию и применяем соответствующую ей функцию
def PerformOperation(operation: str):
    op_type = GetOperationType(operation)
    if op_type == OP_POW:
        Pow(operation)
    elif op_type == OP_PERCENTS:
        Percents(operation)
    elif op_type == OP_ADD:
        Add(operation)
    elif op_type == OP_DIFF:
        Diff(operation)
    elif op_type == OP_DIV:
        Div(operation)
    elif op_type == OP_MULT:
        Mult(operation)
    else:
        print("operation not defined")

oper = str(input())
PerformOperation(oper)