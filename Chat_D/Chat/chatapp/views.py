from django.contrib import auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView

from chatapp.forms import MessageEditForm, UserRegisterForm
from chatapp.models import Message


class ChatView(CreateView, ListView):
    template_name = "index.html"
    form_class = MessageEditForm
    model = Message
    success_url = reverse_lazy("index")

    def get_queryset(self):
        message_list = Message.objects.all()
        try:
            message_list = message_list[int(message_list.count()) - 5: int(message_list.count())]
        except:
            pass
        return message_list

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.user)
        Message.objects.create(name=user[0], text=request.POST['text'])
        return HttpResponseRedirect(reverse("index"))

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)


def register(request):
    if request.method == "POST":
        register_form = UserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse("login"))
    else:
        register_form = UserRegisterForm()

    content = {"register_form": register_form}
    return render(request, "registration/register.html", content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
