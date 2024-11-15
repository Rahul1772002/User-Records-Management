from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields =('name','photo','email','password','mobile_number','date_of_birth')