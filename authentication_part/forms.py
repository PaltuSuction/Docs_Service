from django import forms
from django.contrib.auth import get_user_model

from Docs_Service import settings


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput)

    class Meta:
        '''TODO: Разобраться с тем, почему не работает эта штука'''
        #model = settings.AUTH_USER_MODEL
        model = get_user_model()
        fields = ('avatar', 'email', 'last_name', 'first_name', 'middle_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')