import argparse

from guess_number_game import guess_number_only, guess_number_online
from log_games import logger
from settings import DESCRIPTION_GUESS_NUMBER_ONLY, COMPUTERS_ANSWER, ATTEMPTS, \
    DESCRIPTION_GUESS_NUMBER_ONLINE


def send_log_ex(exception):
    """Запись в log"""
    try:
        logger.info(f'{exception}')
    except Exception as ex:
        logger.info(f'Произошел сбой: {ex}')


def settings_player(player_first, player_second, player_origin):
    if player_origin == player_first:
        player_origin = player_second
        return player_origin
    else:
        player_origin = player_first
        return player_origin


def change_game(num):
    if num == 1:
        return guess_number_only(DESCRIPTION_GUESS_NUMBER_ONLY, COMPUTERS_ANSWER, ATTEMPTS, send_log_ex)
    if num == 2:
        return guess_number_online(DESCRIPTION_GUESS_NUMBER_ONLINE, COMPUTERS_ANSWER, send_log_ex, settings_player)


def start_parser(func_start):
    """Сценарий для терминала"""
    parser = argparse.ArgumentParser(description='Запуск игр')
    parser.add_argument("g", type=int, help='Выбор игры', nargs='?')
    args = parser.parse_args()
    if args.g is not None:
        func_start(num=args.g)
    elif args.g is None:
        quest = int(input("Какую игру вы хотите запустить?\n"
                          "Угадай число на одного, то пишите 1\n"
                          "Угадай число на двоих, то пишите 2\n"
                          "Ваше число: "))
        func_start(num=quest)
