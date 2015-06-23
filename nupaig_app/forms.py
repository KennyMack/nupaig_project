__author__ = 'Jonathan'
from django import forms
from nupaig_app.models import dependence


class dependence_Form(forms.ModelForm):
    class Meta:
        model = dependence
        fields = ('dependence', )

    def __init__(self, *args, **kwargs):
        super(dependence_Form, self).__init__(*args, **kwargs)
        self.fields["dependence"].widget = forms.TextInput(
            attrs={'placeholder': u'Dependência',
                   'ng-model':u'model_dependence.dependence',
                   'id':'dependence',
                   'required':'sasdasas'
                   })
        #self.fields["text"].help_text = \
        #    u'Digite as informações abaixo e use "#"' \
        #    u' onde deseja que seja subistituído no momento da impressão.'

