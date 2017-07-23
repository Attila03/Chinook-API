from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    email2 = forms.EmailField(
        label='Confirm Email',
        widget=forms.EmailInput(attrs={'placeholder': 'abc@gmail.com'}),
    )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User

        fields = ['username', 'email', 'email2','password', 'password2']

        widgets = {'password': forms.PasswordInput,
                   'email': forms.EmailInput(attrs={'placeholder': 'abc@gmail.com', }),
                    }

        help_texts = {'username': None, }