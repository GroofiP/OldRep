import random

print("Игра 'Угадай число'. Компьютер загадывает любое число от 0 до 100, а вы должны его отгадать за 10 попыток.")

number = random.randint(0, 100)
attempts = 10

while True:

    number_user = int(input("Введите число: "))
    if number_user > 100:
        print(" нельзя писить больше 100")
    elif number_user < 0:
        print("нельзя писать меньше 0")
    elif number == number_user:
        print("вы победили :)")
        break
    elif number_user < number:
        print("это число меньше загадоного")
    elif number_user > number:
        print("это число больше загадоного ")

