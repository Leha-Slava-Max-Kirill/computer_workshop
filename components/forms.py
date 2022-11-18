from django import forms

class GetCores(forms.Form):
    cores = forms.IntegerField(help_text="Enter number of cores")