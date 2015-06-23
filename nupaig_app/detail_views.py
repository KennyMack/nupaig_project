from django.core.urlresolvers import reverse

__author__ = 'Jonathan'
from django.views.generic import DetailView
from nupaig_app.models import dependence


class dependence_DetailView(DetailView):
    """docstring for Dependence_DetailView"""
    model = dependence
    template_name = 'detailviews/detail_dependence.html'

    def get_context_data(self, **kwargs):
        context = super(dependence_DetailView, self).get_context_data(**kwargs)
        context['link_list'] = reverse('principal:list_dependence')
        context['link_new'] = reverse('principal:add_dependence')
        context['link_edit'] = reverse('principal:update_dependence',
                                           kwargs={'pk': self.object.id}
                                       )
        context['link_delete'] = reverse('principal:deletealldependence',
                                         kwargs={'pk': self.object.id }
                                         )
        return context