from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

#creating a custom signup form, instead of using default django's one.
class SignUpCustom(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name =forms.CharField(max_length=30, required=False)
    username = forms.CharField(max_length=50, help_text='choose a unique username')
    email = forms.EmailField(required=False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        labels = {'first_name': "What's Your First Name"
                  }
        
         # The Meta class inside a Django form provides additional information about the form itself, especially concerning its behavior and properties. We can use any class name instead of 'Meta', but its just the convention.
    
        
