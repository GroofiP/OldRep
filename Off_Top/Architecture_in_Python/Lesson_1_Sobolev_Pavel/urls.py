import time
from datetime import date
from views import Index, About, NotFound404


# front controller
def data_front(request):

    request['data'] = date.strftime(date.today(), "%d.%m.%Y")


def time_front(request):
    request['time'] = str(f"{time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}")


fronts = [data_front, time_front]

routes = {
    '/': Index(),
    '/about/': About(),
    '/404/': NotFound404()
}
