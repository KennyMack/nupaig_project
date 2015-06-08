from django.contrib import admin
from nupaig_app.models import dependence, disease, exam, unit_measure, exam_detail
from nupaig_app.models import exam_detail_qualit, exam_detail_exam_detail_qualit
from nupaig_app.models import transmition, treatment, treatment_place, pathology, risk
from nupaig_app.models import standard_form, event, suspension_reason, person
from nupaig_app.models import address, person_address


# Register your models here.
admin.site.register(address)
admin.site.register(dependence)
admin.site.register(disease)
admin.site.register(exam)
admin.site.register(exam_detail)
admin.site.register(exam_detail_qualit)
admin.site.register(exam_detail_exam_detail_qualit)
admin.site.register(event)
admin.site.register(pathology)
admin.site.register(person)
admin.site.register(person_address)
admin.site.register(risk)
admin.site.register(standard_form)
admin.site.register(suspension_reason)
admin.site.register(transmition)
admin.site.register(treatment)
admin.site.register(treatment_place)
admin.site.register(unit_measure)





