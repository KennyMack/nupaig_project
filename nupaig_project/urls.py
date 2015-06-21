from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nupaig_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^principal/', include('nupaig_app.urls', namespace='principal')),
    url(r'^mordor/', include('mordor_app.urls', namespace='mordor')),
    url(r'^$', 'nupaig_app.views.home', name='home'),
)

urlpatterns += staticfiles_urlpatterns()

handler404 = 'mordor_app.views.handler404'
handler500 = 'mordor_app.views.handler500'