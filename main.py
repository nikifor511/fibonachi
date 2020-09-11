def fibonacci(n):
    """
    вычисляя очередное число Фибоначчи через доп переменную,
    проверяем, если четное - кладем в res
    """
    assert n > 0, "n must be > 0"

    fib_prev = 0
    fib_curr = 1
    res = [0]  # первое четное число Фибоначчи

    while len(res) < n:
            fib_curr1 = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_curr1
            if fib_curr % 2 == 0:
                res.append(fib_curr)

    return res


def even_fibonacci(n):
    """
    из статьи https://habr.com/ru/post/450594/
    по теореме Люка: каждое третье число Фибоначчи — чётное,
    а каждое чётное имеет номер кратный трём.
    Далее воспользуемся формулой F(n+3) = 4F(n) + F(n-3)
    """

    assert n > 0, "n must be > 0"

    res = [0]  # первое четное число Фибоначчи
    if n >= 2:
        res.append(2)  # второе четное число Фибоначчи
        for i in range(2, n):
            fib_curr = 4 * res[i-1] + res[i-2]
            res.append(fib_curr)

    return res


if __name__ == '__main__':
    for fib in fibonacci(3):
        print(fib)
    print("-------------------------------------")
    for fib in even_fibonacci(10):
        print(fib)
