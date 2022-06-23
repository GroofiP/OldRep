from clock_framework.main import Framework, FakeApplication, DebugApplication
from urls import fronts
from views import routes
from wsgiref.simple_server import make_server

application = Framework(routes, fronts)
application_fake = FakeApplication(routes, fronts)
application_debug = DebugApplication(routes, fronts)

with make_server('', 8000, application) as httpd:
    print("Запуск на порту 8000...")
    httpd.serve_forever()
