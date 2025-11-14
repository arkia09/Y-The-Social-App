from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "w-full px-3 py-2 rounded-lg border border-[#d6c8bc] bg-[#f4eee7] text-[#5a4634] focus:outline-none focus:ring-2 focus:ring-[#7b6149]"
            })
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')