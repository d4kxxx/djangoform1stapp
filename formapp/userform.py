from django import forms


class UserForms(forms.Form):
    name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30)
    email = forms.EmailField()
    address = forms.CharField(max_length=100)
