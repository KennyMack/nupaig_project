__author__ = 'Jonathan'
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse
from nupaig_app.models import dependence
from nupaig_app.forms import dependence_Form


class dependence_UpdateView(UpdateView):
    model = dependence
    template_name = 'Forms/form_dependence.html'
    form_class = dependence_Form
    success_url = 'principal:list_dependence'

    def get_context_data(self, **kwargs):
        context = super(dependence_UpdateView, self).get_context_data(**kwargs)
        context['link_items'] = reverse('principal:list_dependence')
        context['link_post'] = ''
        return context

    def get_success_url(self):
        return reverse(self.success_url)