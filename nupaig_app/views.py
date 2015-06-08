from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from nupaig_app.forms import dependence_Form
from django.contrib.auth.decorators import login_required
from nupaig_app.models import dependence
from django.utils.translation import ugettext as _

# Create your views here.
def home(request):
    return render(request, 'views/principal.html')

@login_required
def add_dependence(request):

    link_items = reverse('principal:list_dependence')
    link_post = reverse('principal:add_dependence')

    frm = dependence_Form()

    if request.POST:
        frm = dependence_Form(data=request.POST)

        if frm.is_valid():
            description = frm.cleaned_data['dependence']
            Dep = dependence(dependence=description)
            Dep.save()
            return HttpResponseRedirect(reverse('principal:list_dependence'))
    return render(request,
        'Forms/form_dependence.html',
        {'form': frm,
         'link_post': link_post,
         'link_items': link_items})