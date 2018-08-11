from django import forms
from django.contrib.auth.forms import UserCreationForm
from blog.models import *


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, required=False, help_text="(optional)")
    last_name = forms.CharField(max_length=32, required=False, help_text="(optional)")
    email = forms.CharField(max_length=256, required=True, help_text="Required. Inform a valid email address.")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('title', 'contents', )


class BookAssignForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', )
