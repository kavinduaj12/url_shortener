from django import forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control','placeholder':'enter username'}))
    password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control','placeholder':'enter password'}))

class UrlForm(forms.Form):
    url = forms.CharField(label="URL",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your url'}))