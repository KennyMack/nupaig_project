from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class User_Profile(models.Model):
    choicesex = (
        (u'M', _(u'Masculino')),
        (u'F', _(u'Feminino')),
    )
    choicepers = (
        (u'F', _(u'Pessoa Física')),
        (u'J', _(u'Pessoa Jurídica')),
    )

    class Meta:
        verbose_name = "User_Profile"
        verbose_name_plural = "User_Profiles"

    user = models.OneToOneField(User, primary_key=True)

    sex = models.CharField(verbose_name=_("Sexo"),
                           blank=False,
                           max_length=1,
                           choices=choicesex,
                           default='M')

    dob = models.DateField(verbose_name=_("Data de nascimento"),
                           blank=False)

    PersonType = models.CharField(verbose_name=_("Tipo de pessoa"),
                                  max_length=1,
                                  choices=choicepers,
                                  default='F')

    cpfcnpj = models.CharField(verbose_name=_("CPF/CNPJ"),
                               max_length=36,
                               blank=False)

    def __str__(self):
        return str(self.user)

