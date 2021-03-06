from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import User

from django import forms

from mainapp.models import ProductCategory,Product
from django.forms.models import ModelForm



class UserAdminRegisterForm(UserRegisterForm):

    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image','first_name', 'last_name', 'password1', 'password2')
class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': False}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': False}))

class ProductCategoryForm(ModelForm):

    class Meta:
        model = ProductCategory
        fields = ('name', 'desription')