import random

# guess_number_game

COMPUTERS_ANSWER = random.randint(0, 101)
ATTEMPTS = 5
DESCRIPTION_GUESS_NUMBER_ONLY = "Это игра 'Угадай число', где тебе предстоит угадать число, которое загадал компьютер.\n" \
                                f"Число, которое он загадал находится в диапазоне от 0 до 100. Попыток, чтобы его отгадать {ATTEMPTS}.\n" \
                                "Удачи!"
DESCRIPTION_GUESS_NUMBER_ONLINE = "Это игра 'Угадай число' на двоих, где вам предстоит угадать число, которое загадал компьютер.\n" \
                                  "Число, которое он загадал находится в диапазоне от 0 до 100. Кто первым отгадает число, тот и выиграл!.\n" \
                                  "Удачи!"

# log_games
PATH_LOG = "logs/"
PATH_FILE_ROT = "app"
PATH_FILE_LOG = "app.log"

