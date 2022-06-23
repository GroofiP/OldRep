from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import forms, HiddenInput

from authapp.models import Shop_User


class Shop_User_Login_Form(AuthenticationForm):
    class Meta:
        model = Shop_User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class Shop_User_Register_Form(UserCreationForm):
    class Meta:
        model = Shop_User
        fields = ("username", "first_name", "password1", "password2", "email", "age", "avatar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    def clean_age(self):
        data = self.cleaned_data["age"]
        if data < 18:
            return forms.ValidationError("Вы слишком молоды!")
        return data


class Shop_User_Edit_Form(UserChangeForm):
    class Meta:
        model = Shop_User
        fields = ("username", "first_name", "password", "email", "age", "avatar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            if field_name == "password":
                field.widget = HiddenInput()

    def clean_age(self):
        data = self.cleaned_data["age"]
        if data < 18:
            return forms.ValidationError("Вы слишком молоды!")
        return data
