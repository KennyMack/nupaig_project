__author__ = 'Jonathan'
from django.core.urlresolvers import reverse
from django.views.generic import DeleteView
from nupaig_app.models import dependence
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

@login_required
def delete_dependence(request, pk):
    if request.method == 'POST':
        _id = pk
        instance = dependence.objects.get(id=_id)
        if instance.delete():
            v = True
    return HttpResponse(json.dumps("ok"),  content_type="application/json")