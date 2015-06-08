__author__ = 'Jonathan'
from django import forms
from nupaig_app.models import dependence


class dependence_Form(forms.ModelForm):
    class Meta:
        model = dependence
        fields = ('dependence', )

