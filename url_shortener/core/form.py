from django import forms

class UrlForm(forms.Form):
    url = forms.CharField(label="URL",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your url'}))