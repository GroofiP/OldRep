def guess_number_only(desc, answer, att, func_1):
    print(desc)


    while True:
        try:
            clover = int(input('Введите число от 0 до 100: '))
        except Exception as ex:
            func_1(ex)
            clover = 200
        if clover == answer:
            print(f"Победа!\n"
                  f"Число было: {answer}\n"
                  f"Конец игры")
            break
        elif att == 1:
            print("Вы проиграли!\n"
                  f"Число было: {answer}\n"
                  "Попробуйте ещё раз!")
            break
        elif clover < 0 or clover > 100:
            print("Вы ввели что-то не то!\n"
                  "Мы забираем попытку!")
            att = att - 1
        elif clover > answer:
            print("Ваше число больше,чем загадал компьютер")
            att = att - 1
        elif clover < answer:
            print("Ваше число меньше,чем загадал компьютер")
            att = att - 1


def guess_number_online(desc, answer,func_1, func_2):
    print(desc)
    player_1 = (input('Игрок 1, введите свое имя: '))
    player_2 = (input('Игрок 2, введите свое имя: '))
    player = player_2

    while True:
        player = func_2(player_1, player_2, player)
        print(f"Очередь, {player}")
        try:
            clover = int(input(f'{player}, введите число от 0 до 100: '))
        except Exception as ex:
            func_1(ex)
            clover = 200
        if clover == answer:
            print(f"Победа!\n"
                  f"Игрок {player} победил!\n"
                  f"Число было: {answer}\n"
                  f"Конец игры")
            break
        elif clover < 0 or clover > 100:
            print("Вы ввели что-то не то!\n"
                  "Мы отдаем ход следующему игроку!")
        elif clover > answer:
            print("Ваше число больше,чем загадал компьютер")
        elif clover < answer:
            print("Ваше число меньше,чем загадал компьютер")
