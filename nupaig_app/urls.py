__author__ = 'Jonathan'
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url
from django.contrib import admin

from nupaig_app.list_views import dependence_ListView

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
)