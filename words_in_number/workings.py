from . import tens, units


def solving(value):
    result = None

    if value[0] == '0' and value[1] != '0':
        value = int(value)

    value = str(value)

    if len(value) == 2:
        if value[0] == '1':
            result = units.unit(value)
        else:
            result = tens.ten(value)
    else:
        if value[0] == '0' and value[1] == '0' and value[2] == '0':
            result = ' '
        elif value[1] == '0' and value[2] == '0':
            result = problem_solving(value[0]) + ' Hundred'
        elif value[0] == '0':
            result = 'and ' + problem_solving(value)
        elif value[1] == '0':
            result = problem_solving(value[0]) + ' Hundred and ' + problem_solving(value[2])
        elif value[2] == '0':
            result = problem_solving(value[0]) + ' Hundred and ' + tens.ten(value[1]+'0')

    return result


def problem_solving(value):
    result = None
    value = int(value)

    if len(str(value)) == 1:
        result = units.unit(value)
    elif len(str(value)) == 2:
        s_v = list(str(value))
        if s_v[0] == '0':
            value = int(value)
        if s_v[0] == '1':
            result = units.unit(value)
        else:
            result = tens.ten(s_v[0]+'0') + '-' + problem_solving(s_v[1])
    elif len(str(value)) == 3:
        s_v = list(str(value))
        result = problem_solving(s_v[0]) + ' Hundred and ' + problem_solving(s_v[1]+s_v[2])

    return result


def comma(commas: int):
    result = None

    if commas == 4:
        result = 'Trillion'
    if commas == 3:
        result = 'Billion'
    if commas == 2:
        result = 'Million'
    if commas == 1:
        result = 'Thousand'

    return result
