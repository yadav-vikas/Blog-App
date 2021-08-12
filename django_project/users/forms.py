from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #defualt required=True

    class Meta:
        """class Meta: - gives us a nested namespace for configuration and keeps configuration at one place
        and within we are saying the model is affected is user model
        eg. if we do form.save() then it will save it to User model
        -- the fileds are listed below are form values we need to store
        """
        model = User
        fields = ['username','email', 'password1','password2']