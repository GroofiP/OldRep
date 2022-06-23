import quopri

from clock_framework.requests import PostRequests, GetRequests


class Framework:

    def __init__(self, routes_obj, fronts_obj):
        """
        Инизилизация framework`а
        :param routes_obj: Урлы сайта
        :param fronts_obj: Прослойка для представления
        """
        self.routes_lst = routes_obj
        self.fronts_lst = fronts_obj

    def __call__(self, environ, start_response):
        """
        Вызов основных задачи framework`а.
        :param environ: Стандарт WSGI
        :param start_response: Стандарт WSGI
        :return:
        """
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path = f'{path}/'
        request = {}
        method = environ['REQUEST_METHOD']
        request['method'] = method
        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = self.decode_value(data)
        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['data'] = self.decode_value(request_params)
        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = self.routes_lst['/404/']
        for front in self.fronts_lst:
            front(request)
        code, body = view(request)
        print(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        """
        Декодирует данные
        :param data:  Данные
        :return: Декодировнные данные
        """
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data
