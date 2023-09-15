from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Goods, OrderPlace, OrderType, TagColors

class CreateUserForm(UserCreationForm):

    role = forms.CharField(initial=CustomUser.ADMIN, widget=forms.HiddenInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1','password2', 'role')

class CreateNewUser(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1','password2', 'role')

class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ['name', 'place', 'price', 'count']

class PlaceForm(forms.ModelForm):
    class Meta:
        model = OrderPlace
        fields = ['name', 'color']
        widgets = {
            'color': forms.Select(choices=TagColors.COLOR_CHOICE)
        }

class TypeForm(forms.ModelForm):
    class Meta:
        model = OrderType
        fields = ['name', 'color']
        widgets = {
            'color': forms.Select(choices=TagColors.COLOR_CHOICE)
        }