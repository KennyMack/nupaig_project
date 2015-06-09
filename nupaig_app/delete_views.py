__author__ = 'Jonathan'
from django.core.urlresolvers import reverse
from django.views.generic import DeleteView
from nupaig_app.models import dependence
from django.contrib.auth.decorators import login_required


class dependence_DeleteView(DeleteView):

    """docstring for Dependence_DeleteView"""

    model = dependence
    template_name = 'confirm.html'
    success_url = 'principal:list_dependence'

    def get_success_url(self):
        return reverse(self.success_url)