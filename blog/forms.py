from django import forms


class FormField(forms.Form):
    nama = forms.CharField()
    alamat = forms.CharField()
