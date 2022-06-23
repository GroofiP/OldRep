from django import forms

from authapp.forms import Shop_User_Edit_Form
from authapp.models import Shop_User
from mainapp.models import Product_Category, Product


class ShopUserAdminEditForm(Shop_User_Edit_Form):
    class Meta:
        model = Shop_User
        fields = "__all__"



class ProductCategoryEditForm(forms.ModelForm):
    class Meta:
        model = Product_Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
