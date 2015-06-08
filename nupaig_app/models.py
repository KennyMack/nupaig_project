from django.db import models

# Create your models here.


class dependence(models.Model):

    class Meta:
        verbose_name = "dependence"
        verbose_name_plural = "dependences"

    dependence = models.CharField(
        verbose_name='Dependencia',
        max_length=50,
        blank=False)

    def __str__(self):
        return self.dependence


class disease(models.Model):

    class Meta:
        verbose_name = "disease"
        verbose_name_plural = "diseases"

    description = models.CharField(
        verbose_name="Descrição",
        max_length=50,
        blank=False)

    def __str__(self):
        return self.description


class exam(models.Model):

    choice_cabec_exam = (
        (0, u'Não'),
        (1, u'Sim'),
    )

    choice_type_exam = (
        (0, u'Sangue'),
        (1, u'Patologia'),
        (1, u'Imagem'),
    )

    class Meta:
        verbose_name = "exam"
        verbose_name_plural = "exams"

    description = models.CharField(
        verbose_name="Descrição",
        max_length=50,
        blank=False)

    print_cabec_exam = models.IntegerField(
        verbose_name="Imprime resultado no cabeçalho ?",
        choices=choice_cabec_exam)

    export_results = models.IntegerField(
        verbose_name="Imprime resultado no cabeçalho ?",
        choices=choice_cabec_exam)

    week_evolution = models.IntegerField(
        verbose_name="Imprime resultado no cabeçalho ?",
        choices=choice_cabec_exam)

    type_exam = models.IntegerField(
        verbose_name="Imprime resultado no cabeçalho ?",
        choices=choice_type_exam)

    def __str__(self):
        return self.description


class unit_measure(models.Model):

    class Meta:
        verbose_name = "unit_measure"
        verbose_name_plural = "unit_measures"

    unit = models.CharField(
        verbose_name="Cód. Unidade",
        blank=False,
        max_length=10)

    description = models.CharField(
        verbose_name="Descrição",
        max_length=50,
        blank=False)

    def __str__(self):
        return self.description


class exam_detail(models.Model):

    choice_type_exam_det = (
        (0, u'Qualitativo'),
        (1, u'Quantitativo'),
    )

    class Meta:
        verbose_name = "exam_detail"
        verbose_name_plural = "exam_details"

    description = models.CharField(
        verbose_name="Descrição",
        max_length=50,
        blank=False)

    type_exam_det = models.IntegerField(
        verbose_name="Tipo exame",
        choices=choice_type_exam_det)

    exam_id = models.ForeignKey(
        exam,
        blank=False)

    unit_measure_id = models.ForeignKey(
        unit_measure,
        blank=True)

    def __str__(self):
        return self.description


class exam_detail_qualit(models.Model):

    class Meta:
        verbose_name = "exam_detail_qualit"
        verbose_name_plural = "exam_detail_qualits"

    description = models.CharField(
        verbose_name="Descrição",
        max_length=50,
        blank=False)

    exam_detail_qualit = models.ManyToManyField(
        exam_detail,
        through='exam_detail_exam_detail_qualit'
    )

    def __str__(self):
        return self.description


class exam_detail_exam_detail_qualit(models.Model):

    class Meta:
        verbose_name = "exam_detail_exam_detail_qualit"
        verbose_name_plural = "exam_detail_exam_detail_qualits"

    exam_detail_id = models.ForeignKey(exam_detail)
    exam_detail_qualit_id = models.ForeignKey(exam_detail_qualit)


class transmition(models.Model):

    class Meta:
        verbose_name = "transmition"
        verbose_name_plural = "transmitions"

    description = models.CharField(
        verbose_name="Descrição",
        max_length=50,
        blank=False)

    def __str__(self):
        return self.description


class pathology(models.Model):

    class Meta:
        verbose_name = "pathology"
        verbose_name_plural = "pathologys"

    description = models.CharField(
        verbose_name="Descrição",
        max_length=50,
        blank=False)

    def __str__(self):
        return self.description


class risk(models.Model):

    class Meta:
        verbose_name = "risk"
        verbose_name_plural = "risks"

    description = models.CharField(
        verbose_name="Descrição",
        max_length=50,
        blank=False)

    def __str__(self):
        return self.description


class treatment_place(models.Model):

    class Meta:
        verbose_name = "treatment_place"
        verbose_name_plural = "treatment_places"

    description = models.CharField(
        verbose_name="Descrição",
        max_length=50,
        blank=False)

    def __str__(self):
        return self.description


class standard_form(models.Model):

    class Meta:
        verbose_name = "standard_form"
        verbose_name_plural = "standard_forms"

    description = models.CharField(
        verbose_name="Descrição",
        max_length=50,
        blank=False)

    text = models.TextField(
        verbose_name="Texto",
        blank=False,
        max_length=500)

    def __str__(self):
        return self.description


class event(models.Model):

    class Meta:
        verbose_name = "event"
        verbose_name_plural = "events"

    description = models.CharField(
        verbose_name="Descrição",
        max_length=50,
        blank=False)

    def __str__(self):
        return self.description


class treatment(models.Model):

    class Meta:
        verbose_name = "treatment"
        verbose_name_plural = "treatments"

    description = models.CharField(
        verbose_name="Descrição",
        max_length=50,
        blank=False)

    def __str__(self):
        return self.description


class suspension_reason(models.Model):

    choice_reason = (
        (0, u'Não'),
        (1, u'Sim'),
    )

    class Meta:
        verbose_name = "suspension_reason"
        verbose_name_plural = "suspension_reasons"

    description = models.CharField(
        verbose_name="Descrição",
        max_length=50,
        blank=False)

    reason = models.IntegerField(
        verbose_name="Solicita motivo",
        choices=choice_reason,
        default=0,
        blank=False)

    def __str__(self):
        return self.description


class person(models.Model):

    choice_sex = (
        (u'M', u'Maculino'),
        (u'F', u'Feminino'),
    )

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "persons"

    name = models.CharField(
        verbose_name="Nome",
        max_length=80,
        blank=False)

    dob = models.DateField(
        auto_now_add=True)

    sex = models.CharField(
        max_length=1,
        choices=choice_sex
    )

    sign_date = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return self.name


class address(models.Model):

    class Meta:
        verbose_name = "address"
        verbose_name_plural = "address"

    address = models.CharField(
        verbose_name="Endereço",
        max_length=80)

    cep = models.CharField(
        verbose_name="C.E.P.",
        max_length=10)

    district = models.CharField(
        verbose_name="Bairro",
        max_length=50)

    city = models.CharField(
        verbose_name="Estado",
        max_length=50)

    complement = models.CharField(
        verbose_name="Complemento",
        max_length=60)

    phone = models.CharField(
        verbose_name="Telefone",
        max_length=50)

    cellphone = models.CharField(
        verbose_name="Celular",
        max_length=50)

    address = models.ManyToManyField(person, through='person_address')

    def __str__(self):
        return self.address


class person_address(models.Model):

    class Meta:
        verbose_name = "person_address"
        verbose_name_plural = "person_address"

    person_id = models.ForeignKey(person)
    address_id = models.ForeignKey(address)
