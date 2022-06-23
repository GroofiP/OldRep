number = int(input('Введите сколько нужно четных чисел: '))
even_score = []


def even_odd(num, a, b, even):
    if num == 0:
        even.insert(0,0)
        return print(f'Четные цифры : ({even})')
    else:
        c = a + b
        a = b
        b = c
        if c % 2 == 0:
            even.append(c)
            return even_odd(num - 1, a, b, even)
        else:
            return even_odd(num, a, b, even)



even_odd(number-1, 0, 1, even_score)
