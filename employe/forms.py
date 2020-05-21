from django import forms

from employe.models import Emplyee


class Empfrom(forms.ModelForm):
    class Meta:
        model = Emplyee
        fields = ['E_name', 'E_Id', 'E_address', 'E_salary']