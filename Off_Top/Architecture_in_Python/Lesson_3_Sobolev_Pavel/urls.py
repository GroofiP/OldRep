import time
from datetime import date
from views import Index, About, NotFound404, Contacts, Developments


# front controller
def data_front(request):
    """
    Узнаем дату
    :param request: реквест который будет обновлен
    :return: обновленный реквест
    """
    request['data_time'] = date.strftime(date.today(), "%d.%m.%Y")


def time_front(request):
    """
    Узнаем время
    :param request: реквест который будет обновлен
    :return: обновленный реквест
    """
    request['time'] = str(f"{time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}")


def time_city_front(request):
    """
    Узнаем время для определенного города
    :param request: реквест который будет обновлен
    :return: обновленный реквест
    """
    data_city_time = {
        "ka": ["Калининград", -1],
        "ms": ["Москва", 0],
        "sp": ["Санкт-Петербург", 0],
        "sa": ["Самара", 1],
        "ek": ["Екатеринбург", 2],
        "om": ["Омск", 3],
        "kr": ["Красноярск", 4],
        "ir": ["Иркутск", 5],
        "ja": ["Якутск", 6],
        "vl": ["Владивосток", 7],
        "ma": ["Магадан", 8],
        "km": ["Камчатка", 9]
    }

    key = request["data"]
    if key.get("location"):
        key_a = data_city_time[key['location']][0]
        key_b = data_city_time[key['location']][1]
    else:
        key_a = data_city_time['sp'][0]
        key_b = data_city_time['sp'][1]
    request["city"] = key_a
    request['time_city'] = str(
        f"{int(time.localtime().tm_hour) + int(key_b)}:{time.localtime().tm_min}:{time.localtime().tm_sec}")


def save_msg_front(request):
    """
    Сохраняем реквест
    :param request: реквест у которого возьмем данных
    :return: сохраненное сообщение от пользователя
    """
    key = request["data"]
    if key.get("name") and key.get("email") and key.get("text_user"):
        with open("message_file", "a", encoding="utf-8") as msg:
            msg.write(f"Сообщение от пользовтеля {key['name']}\n"
                      f"С e-mail`ом : {key['email']}\n"
                      f"Сообщение: {key['text_user']}\n")


def add_development_front(request):
    """
    Сохраняем реквест
    :param request: реквест у которого возьмем данных
    :return: сохраненное сообщение от пользователя
    """
    key = request["data"]
    if key.get("name") and key.get("calendar") and key.get("time"):
        request["developments"] = f"Событие {key['name']} в {key['calendar']} {key['time']}"


fronts = [data_front, time_front, time_city_front, save_msg_front, add_development_front]

routes = {
    '/': Index(),
    '/about/': About(),
    '/contacts/': Contacts(),
    '/developments/': Developments(),
    '/404/': NotFound404()
}
