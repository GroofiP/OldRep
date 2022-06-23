from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import Shop_User_Login_Form, Shop_User_Register_Form, Shop_User_Edit_Form


def login(request):
    login_form = Shop_User_Login_Form(data=request.POST)
    next_url = request.GET.get("next","")
    if request.method == "POST" and login_form.is_valid():
        user_name = request.POST.get("username")
        password = request.POST["password"]
        user = auth.authenticate(username=user_name, password=password)
        if user.is_active and user:
            auth.login(request, user)
            if "next" in request.POST.keys():
                return HttpResponseRedirect(request.POST["next"])
            return HttpResponseRedirect(reverse("index"))
    context = {
        "login_form": login_form,
        "next": next_url
               }
    return render(request, "authapp/login.html", context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        register_form = Shop_User_Register_Form(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse("authapp:login"))
    else:
        register_form = Shop_User_Register_Form()
    context = {"register_form": register_form}
    return render(request, "authapp/register.html", context=context)


def edit(request):
    if request.method == "POST":
        edit_form = Shop_User_Edit_Form(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("authapp:login"))
    else:
        edit_form = Shop_User_Edit_Form(instance=request.user)
    context = {"edit_form": edit_form}
    return render(request, "authapp/edit.html", context=context)
