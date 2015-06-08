__author__ = 'Jonathan'
from mordor_app.models import User_Profile
from django.contrib.auth.models import User
import re
from django import forms
from django.contrib.auth import authenticate
from mordor_app.validator import Form_Validator
from django.utils.translation import ugettext as _


class User_Form(forms.ModelForm):

    # re.compile(r'^\w{3,}?[@]\s?\w{3,}[.]?([c][o][m]){1}')

    # Regular expression to password
    # password must be almost 1 number
    passre = re.compile(
        r"^(?:\d+[a-z]\w|[a-z]\w+\d|\d+[A-Z]\w|[A-Z]\w+\d)+([A-Z\d]\w+|[a-z\d]\w+)*")

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': _(u'Senha')}),
        label=u"Senha",
        help_text=_(u'A senha deve conter letras e números'))
    passwordconfirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': _("Repita a senha")}),
        label=_("Senha"))

    def __init__(self, *args, **kwargs):
        super(User_Form, self).__init__(*args, **kwargs)
        self.fields["first_name"].label = _("Nome")
        self.fields["last_name"].label = _("Sobrenome")
        self.fields["email"].widget = forms.TextInput(
            attrs={'placeholder':  _("usuario@dominio.com")})
        self.fields["first_name"].widget = forms.TextInput(
            attrs={'placeholder':  _("Nome")})
        self.fields["last_name"].widget = forms.TextInput(
            attrs={'placeholder': _("Sobrenome")})
        self.fields["username"].widget = forms.TextInput(
            attrs={'placeholder': _("Usuário")})
        self.fields["username"].help_text = ''

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean_username(self):
        cleaned_data = super(User_Form, self).clean()
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError(
                Form_Validator.general_form_errors['required'])
        elif len(username) < 8:
            raise forms.ValidationError(
                Form_Validator.general_form_errors['min_digits8'])
        return cleaned_data.get('username', '')

    def clean_password(self):
        cleaned_data = super(User_Form, self).clean()
        cleanpass = self.cleaned_data.get('password')

        if not self.passre.match(cleanpass):
            raise forms.ValidationError(
                Form_Validator.register_form_errors['passinvalid'])

        if cleanpass and len(cleanpass) < 8:
            raise forms.ValidationError(
                Form_Validator.general_form_errors['min_digits8'])
        return cleaned_data.get('password', '')

    def clean_first_name(self):
        cleaned_data = super(User_Form, self).clean()
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError(
                Form_Validator.general_form_errors['required'])
        elif len(first_name) < 3:
            raise forms.ValidationError(
                Form_Validator.general_form_errors['min_digits3'])
        return cleaned_data.get('first_name', '')

    def clean_passwordconfirm(self):
        cleaned_data = super(User_Form, self).clean()
        password = self.cleaned_data.get('password')
        passwordconfirm = self.cleaned_data.get('passwordconfirm')

        if password and passwordconfirm and password != passwordconfirm:
            raise forms.ValidationError(
                Form_Validator.register_form_errors['not_equal'])
        return cleaned_data.get('passwordconfirm', '')


class User_ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(User_ProfileForm, self).__init__(*args, **kwargs)
        self.fields["cpfcnpj"].widget = forms.TextInput(
            attrs={'placeholder': '111.222.333-44'})
        self.fields["dob"].widget = forms.TextInput(
            attrs={'placeholder': '07/01/2014'})

    class Meta:
        model = User_Profile
        fields = ('sex', 'dob', 'PersonType', 'cpfcnpj')


class Login_Form(forms.Form):
    username = forms.CharField(max_length=30, label=_("User"))
    password = forms.CharField(widget=forms.PasswordInput(), label=_("Senha"))

    def clean(self):
        cleaned_data = super(Login_Form, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if not user.is_active:
                raise forms.ValidationError(
                    Form_Validator.login_form_errors['inactiveuser'])
                   # u'Usuário está desativado.')
        else:
            raise forms.ValidationError(
                Form_Validator.login_form_errors['invalidlogin'])
                # u'Usuário não existe e/ou senha incorreta.')
        return cleaned_data
