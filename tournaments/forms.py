from django import forms


class MyForm(forms.Form):
    my_button = forms.CharField(widget=forms.HiddenInput())
