from django import forms


class CarForm(forms.Form):

    manufacturer = forms.CharField(max_length=255, required=False)
    model = forms.CharField(max_length=255, required=False)
    year = forms.IntegerField(required=False)
    kpp = forms.CharField(max_length=255, required=False)
    color = forms.CharField(max_length=255, required=False)
