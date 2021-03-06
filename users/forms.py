
#django
from django import forms

#models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    #sign up form
    username=forms.CharField(min_length=4, max_length=50)
    password=forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation=forms.CharField(max_length=70, widget=forms.PasswordInput())

    first_name=forms.CharField(min_length=2, max_length=50)
    last_name=forms.CharField(min_length=2, max_length=50)
    email=forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput())

    def clean_email(self):
        #email validation
        email=self.cleaned_data['email'].lower()
        email_taken=User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('email is already in use.')
        return email
    
    def clean_username(self):
        #username must be unique.
        username=self.cleaned_data['username'].lower()
        username_taken=User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('username is already in use.')
        return username

    def clean(self):
        #verify password confrimation match
        data=super().clean()
        password=data['password']
        password_confrimation=data['password_confirmation']

        if password != password_confrimation:
            raise forms.ValidationError('password do not match')

        return data
    def save(self):
        #create user and profile
        data=self.cleaned_data
        data.pop('password_confirmation')

        user= User.objects.create_user(**data)
        profile=Profile(user=user)
        profile.save()

    