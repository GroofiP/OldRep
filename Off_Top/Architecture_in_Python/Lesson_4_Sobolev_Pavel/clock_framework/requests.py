# get requests
class GetRequests:

    @staticmethod
    def parse_input_data(data: str):
        """
        Превращает из строки в словарь
        :param data: Данные
        :return: Словарь с данными
        """
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_params(environ):
        """
        Собираем параметры для реквеста
        :param environ: Стандарт WSGI
        :return: Словарь с данными для реквеста
        """
        query_string = environ['QUERY_STRING']
        request_params = GetRequests.parse_input_data(query_string)
        return request_params


# post requests
class PostRequests:

    @staticmethod
    def parse_input_data(data: str):
        """
        Превращает из строки в словарь
        :param data: Данные
        :return: Словарь с данными
        """
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_wsgi_input_data(env) -> bytes:
        """
        Узнаем длинну данных POST запроса
        :param env: Стандарт WSGI
        :return: Данные
        """
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        """
        Декодируем данные
        :param data: Данные
        :return: Декодированные данные
        """
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        """
        Переход декодированных данных в словарь
        :param environ: Стандарт WSGI
        :return: Данные
        """
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data
