__author__ = 'Jonathan'
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from nupaig_app.models import dependence


class dependence_ListView(ListView):
    model = dependence
    template_name = "listviews/list_dependence.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(dependence_ListView, self).get_context_data(**kwargs)
        context['link_new'] = reverse('principal:add_dependence')
        context['link_list'] = reverse('principal:list_dependence')
        #context['link_delete'] = reverse('principal:delete_all_dependence')
        context['link_update'] = reverse('principal:update_dependence',
                                         kwargs={'pk': 0})
        context['caption'] = 'Dependência'
        return context

    def get_queryset(self):
        return dependence.objects.all().order_by("id")