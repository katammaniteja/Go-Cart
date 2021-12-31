from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class customForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']

    def clean(self):
        all_cleaned_data=super().clean()
        user_email=all_cleaned_data['email']
        if User.objects.filter(email=user_email).exists():
            msg="Email Already exists!"
            self.add_error('email', msg)
