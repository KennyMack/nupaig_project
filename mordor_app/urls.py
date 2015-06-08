__author__ = 'Jonathan'
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'Project_Nupaig.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', 'mordor_app.views.register', name='register'),
    url(r'^login/$', 'mordor_app.views.user_login', name='login'),
    url(r'^logout/$', 'mordor_app.views.user_logout', name='logout'),
)
