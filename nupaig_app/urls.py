__author__ = 'Jonathan'
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url
from django.contrib import admin

from nupaig_app.list_views import dependence_ListView
from nupaig_app.detail_views import dependence_DetailView
from nupaig_app.update_views import dependence_UpdateView
from nupaig_app.delete_views import dependence_DeleteView

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'Project_Nupaig.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^dependence/$', 'nupaig_app.views.add_dependence', name='add_dependence'),

    url(r'^list-dependences/$',
        login_required(
            dependence_ListView.as_view()),
        name='list_dependence'),

    url(r'^update-dependence/(?P<pk>\d+)/$',
        login_required(
            dependence_UpdateView.as_view()),
        name='update_dependence'),

    url(r'^delete-dependence/(?P<pk>\d+)/$',
        login_required(
            dependence_DeleteView.as_view()),
        name='delete_dependence'),

    url(r'^detail-dependence/(?P<pk>\d+)/$',
        login_required(
            dependence_DetailView.as_view()),
        name='detail_dependence'),
)