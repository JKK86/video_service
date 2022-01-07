from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import DateInput

from users.models import Profile

User = get_user_model()


class CreateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(max_length=32)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie są takie same')
        return cd['password2']


class CreateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['birth_date']
        widgets = {'birth_date': DateInput(attrs={'type': 'date'})}


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date']
        widgets = {'birth_date': DateInput(attrs={'type': 'date'})}
