from words_in_number import workings as wor

request = input('Enter Value \n\n>>>  ')

# Converts the number format to include commas after three values
number = f'{int(request):,}'

# This contains the final answer
answer = []

# This separates each three numbers by the comma
_split = number.split(',')

# This counts how many separate numbers were inserted
_count = len(_split)

# This loops through each value to get their equivalent words
for i in range(0, len(_split)):
    if '0' in _split[i]:
        answer.append(wor.solving(_split[i]))
    else:
        answer.append(wor.problem_solving(_split[i]))

    # This helps entail how many commas are in the values
    if _count > 1:
        if int(_split[i]) == 0:
            _count -= 1
            continue
        if _count == 2:
            answer.append(wor.comma(_count-1))
        elif _count == 3:
            answer.append(wor.comma(_count - 1))
        elif _count == 4:
            answer.append(wor.comma(_count - 1))
        elif _count == 5:
            answer.append(wor.comma(_count - 1))

    _count -= 1

# removes redundant spaces in the answer in case of multiple zeros
while ' ' in answer:
    answer.remove(' ')

# The Result
print('\n' + number + '\n', " ".join(answer), sep='')
