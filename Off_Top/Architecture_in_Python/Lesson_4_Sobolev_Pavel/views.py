from clock_framework.templator import render
from patterns.сreational_patterns import Logger, Engine

site = Engine()
logger = Logger("main")


class Index:
    def __call__(self, request):
        logger.log("Это главная страница")
        return '200 OK', render('index.html', data_time=request.get('data_time', None), time=request.get('time', None),
                                time_city=request.get('time_city', None), city=request.get('city', None),
                                title="Главная")


class Contacts:
    def __call__(self, request):
        logger.log("Это страница контакты")
        return '200 OK', render('contacts.html', data=request.get(None), title="Контакты")


class Learn:
    def __call__(self, request):
        logger.log("Это новый раздел обучения")
        return '200 OK', render('order.html', data=request.get(None), objects_list=site.categories, title="Обучение")


class Developments:
    def __call__(self, request):
        logger.log("Это страница событий")
        return '200 OK', render('developments.html', data=request.get(None),
                                developments=request.get("developments", None), title="События")


class About:
    def __call__(self, request):
        logger.log("Это страница о нас")
        return '200 OK', render('about.html', data=request.get(None), title="О нас")


class NotFound404:
    def __call__(self, request):
        logger.log("Эта страница не существует")
        return '404 OK', render('404.html', data=request.get(None), title="404")


class CoursesList:
    def __call__(self, request):
        logger.log('Список курсов')
        try:
            category = site.find_category_by_id(int(request['data']['id']))
            return '200 OK', render('course_list.html', objects_list=category.courses, name=category.name,
                                    id=category.id, title="Список курсов")
        except KeyError:
            return '200 OK', render('course_list.html', objects_list=site.courses, title="Список курсов")


# контроллер - создать курс
class CreateCourse:
    category_id = -1

    def __call__(self, request):
        if request['method'] == 'POST':
            # метод пост
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                course = site.create_course('record', name, category)
                site.courses.append(course)

            return '200 OK', render('course_list.html', objects_list=category.courses,
                                    name=category.name, id=category.id, title="Создание курса")

        else:
            try:
                self.category_id = int(request['data']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render('create_course.html', name=category.name, id=category.id,
                                        title="Создание курса")
            except KeyError:
                return '200 OK', 'No categories have been added yet'


class CreateCategory:
    def __call__(self, request):

        if request['method'] == 'POST':
            # метод пост
            print(request)
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category_id = data.get('category_id')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)

            site.categories.append(new_category)

            return '200 OK', render('order.html', objects_list=site.categories, title="Создание категории")
        else:
            return '200 OK', render('create_category.html', categories=site.categories, title="Создание категории")


class CategoryList:
    def __call__(self, request):
        logger.log('Список категорий')
        return '200 OK', render('category_list.html', objects_list=site.categories, title="Категории")


class CopyCourse:
    def __call__(self, request):
        request_params = request['data']

        try:
            name = request_params['name']
            old_course = site.get_course(name)
            if old_course:
                new_name = f'copy_{name}'
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)

            return '200 OK', render('course_list.html', objects_list=site.courses, title="Копирование")
        except KeyError:
            return '200 OK', 'No courses have been added yet'
