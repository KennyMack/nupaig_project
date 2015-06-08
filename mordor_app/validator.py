# -*- coding: UTF-8 -*-
__author__ = 'Jonathan'
from django.utils.translation import ugettext as _


class Form_Validator(object):

    """docstring for Form_Validator"""

    register_form_errors = {
        'passinvalid': _(u"Senha digitada não é válida."),
        'not_equal': _(u"Senhas devem ser iguais."),
    }

    login_form_errors = {
        'inactiveuser': _(u"Usuário inátivo."),
        'invalidlogin': _(u"Usuário não existe e/ou senha incorreta."),
    }

    general_form_errors = {
        'required': _(u"Este campo é obrigatório."),
        'min_digits3': _(u"Este campo requer 3 digitos ou mais."),
        'min_digits4': _(u"Este campo requer 4 digitos ou mais."),
        'min_digits5': _(u"Este campo requer 5 digitos ou mais."),
        'min_digits6': _(u"Este campo requer 6 digitos ou mais."),
        'min_digits7': _(u"Este campo requer 7 digitos ou mais."),
        'min_digits8': _(u"Este campo requer 8 digitos ou mais."),
        'min_digits9': _(u"Este campo requer 9 digitos ou mais."),
    }