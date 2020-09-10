
def fibonachi(n):
    prev_val = 0                                    # предыдущее (первое) значение 0 - четное -> выводим
    print(prev_val)
    curr_val = 1                                    # текущее значение
    count_even = 1                                  # кол-во найденных четных чисел Ф

    while count_even < n:                           # пока кол-во найденнх четных чисел Ф < заданного
        curr_val_tmp = prev_val + curr_val
        prev_val = curr_val
        curr_val = curr_val_tmp                     # вычисляем через доп переменную следующее число Ф
        if curr_val % 2 == 0:                       # если оно четное -> выводим его и увеличиваем счетчик
            count_even = count_even + 1
            print(curr_val)


def fibonachi_1(n):                                 # считаю, что каждое 3е число Ф в последовательности
                                                    # будет четным  (1е, 4е, 7е, 10е и т.д.
                                                    # т.к. 2 нечетных числа в сумме дают четное,
                                                    # далее нечет + чет = нечет, далее чет + нечет = нечет и т.д.

    prev_val = 0                                    # предыдущее (первое) значение 0 - четное -> выводим
    print(prev_val)
    curr_val = 1
    count = 2                                       # общее кол-во найденных чисел Ф
    count_even = 1                                  # кол-во найденных четных чисел Ф

    while count_even < n:
        curr_val_tmp = prev_val + curr_val
        prev_val = curr_val
        curr_val = curr_val_tmp                     # вычисляем через доп переменную следующее число Ф
        count = count + 1                           # увеличиваем счетчик найденных на 1
        if count % 3 == 1:                          # если данное число Ф по счету 1е, 4е, 7е, 10е и т.д. ->
            count_even = count_even + 1             # выводим его и увеличиваем счетчик
            print(curr_val)


if __name__ == '__main__':
    fibonachi(10)
    print("-----------------------------")
    fibonachi_1(10)
