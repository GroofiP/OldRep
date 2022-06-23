from clock_framework.templator import render
from patterns.architectural_system_pattern_mappers import MapperRegistry
from patterns.architectural_system_pattern_unit_of_work import UnitOfWork
from patterns.behavioral_patterns import ListView, CreateView, EmailNotifier, SmsNotifier, BaseSerializer
from patterns.structural_patterns import AppRoute, Debug
from patterns.сreational_patterns import Logger, Engine

site = Engine()
logger = Logger("main")
email_notifier = EmailNotifier()
sms_notifier = SmsNotifier()
UnitOfWork.new_current()
UnitOfWork.get_current().set_mapper_registry(MapperRegistry)

routes = {}


@AppRoute(routes=routes, url='/')
class Index(ListView):
    template_name = "index.html"
    title = "Главная"


@AppRoute(routes=routes, url="/contacts/")
class Contacts(ListView):
    template_name = "contacts.html"
    title = "Контакты"


@AppRoute(routes=routes, url='/learn/')
class Learn(ListView):
    queryset = site.categories
    template_name = "order.html"
    title = "Обучение"


@AppRoute(routes=routes, url='/developments/')
class Developments(ListView):
    template_name = "developments.html"
    title = "События"


@AppRoute(routes=routes, url='/about/')
class About(ListView):
    template_name = "about.html"
    title = "О нас"


@AppRoute(routes=routes, url='/404/')
class NotFound404(ListView):
    template_name = "404.html"
    title = "404"


@AppRoute(routes=routes, url='/courses-list/')
class CoursesList(ListView):
    template_name = "course_list.html"
    title = "Список курсов"

    def render_template_with_context(self, request):
        template_name = self.get_template()
        title = self.get_title()
        context = {}
        try:
            category = site.find_category_by_id(int(request['data']['id']))
            context["object_list"] = category.courses
            context["name"] = category.name
            context["id"] = category.id
        except KeyError:
            context["object_list"] = site.courses
            context["id"] = 100
        context["title"] = title
        return '200 OK', render(template_name, **context)


@AppRoute(routes=routes, url='/create-course/')
class CreateCourse(CreateView):
    category_id = -1
    template_name = "create_course.html"

    def render_template_with_context(self, request):
        template_name = self.get_template()
        title = self.get_title()
        try:
            self.category_id = int(request['data']['id'])
        except KeyError:
            pass
        category = site.find_category_by_id(int(self.category_id))
        context = {"object_list": category.courses, "name": category.name, "id": category.id, "title": title}
        return '200 OK', render(template_name, **context)

    def create_obj(self, data: dict):
        name = data['name']
        name = site.decode_value(name)
        category = None
        if self.category_id != -1:
            category = site.find_category_by_id(int(self.category_id))
            course = site.create_course('record', name, category)
            course.observers.append(email_notifier)
            course.observers.append(sms_notifier)
            site.courses.append(course)


@AppRoute(routes=routes, url='/create-category/')
class CreateCategory(CreateView):
    template_name = "create_category.html"
    title = "Создание категории"

    def render_template_with_context(self, request):
        template_name = self.get_template()
        title = self.get_title()
        context = {"object_list": site.categories, "title": title}
        return '200 OK', render(template_name, **context)

    def create_obj(self, data: dict):
        name = data['name']
        name = site.decode_value(name)

        category_id = data.get('category_id')

        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))

        new_obj = site.create_category(name, category)
        site.categories.append(new_obj)


@AppRoute(routes=routes, url='/category-list/')
class CategoryList(ListView):
    template_name = "category_list.html"
    queryset = site.categories


@AppRoute(routes=routes, url='/copy-course/')
class CopyCourse(ListView):
    template_name = 'course_list.html'
    queryset = site.courses
    title = "Копирование"

    @Debug(name='CopyCourse')
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

            return '200 OK', render(self.template_name, objects_list=self.queryset, title=self.title)
        except KeyError:
            return '200 OK', 'No courses have been added yet'


@AppRoute(routes=routes, url='/student-list/')
class StudentListView(ListView):
    template_name = 'student_list.html'
    title = "Список студентов"

    def render_template_with_context(self, request):
        template_name = self.get_template()
        title = self.get_title()
        mapper = MapperRegistry.get_current_mapper('student')
        context = {"objects_list": mapper.all(), "title": title}
        return '200 OK', render(template_name, **context)


@AppRoute(routes=routes, url='/create-student/')
class StudentCreateView(CreateView):
    template_name = 'create_student.html'
    title = "Создание студента"

    def create_obj(self, data: dict):
        name = data['name']
        name = site.decode_value(name)
        new_obj = site.create_user('student', name)
        site.students.append(new_obj)
        new_obj.mark_new()
        UnitOfWork.get_current().commit()


@AppRoute(routes=routes, url='/add-student/')
class AddStudentByCourseCreateView(CreateView):
    template_name = 'add_student.html'
    title = "Добавление студента"

    def get_context_data(self):
        context = super().get_context_data()
        mapper = MapperRegistry.get_current_mapper('student')
        context['courses'] = site.courses
        context['students'] = mapper.all()
        return context

    def create_obj(self, data: dict):
        course_name = data['course_name']
        course_name = site.decode_value(course_name)
        course = site.get_course(course_name)
        student_name = data['student_name']
        print(data)
        student_name = site.decode_value(student_name)
        student = site.get_student(student_name)
        course.add_student(student)


@AppRoute(routes=routes, url='/api/')
class CourseApi(ListView):
    @Debug(name='CourseApi')
    def __call__(self, request):
        return '200 OK', BaseSerializer(site.courses).save()
