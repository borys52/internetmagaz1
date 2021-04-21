from  django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username', )

    def clean_password2(self, *args, **kwargs):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password2']

