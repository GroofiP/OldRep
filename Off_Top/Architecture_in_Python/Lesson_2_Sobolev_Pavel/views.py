from clock_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', data_time=request.get('data_time', None), time=request.get('time', None),
                                time_city=request.get('time_city', None), city=request.get('city', None))


class Contacts:
    def __call__(self, request):
        return '200 OK', render('contacts.html', data=request.get(None))


class About:
    def __call__(self, request):
        return '200 OK', render('about.html', data=request.get(None))


class NotFound404:
    def __call__(self, request):
        return '404 OK', render('404.html', data=request.get(None))
