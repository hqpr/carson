from django.conf.urls import patterns, include, url
from django.contrib import admin
from carson import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^product/(\d+)/$', views.product, name='product'),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns("django.views",
        url(r"%s(?P<path>.*)$" % settings.STATIC_URL[1:], "static.serve", {
            "document_root": settings.STATIC_ROOT,
            'show_indexes': True,
        }),
        url(r"%s(?P<path>.*)$" % settings.MEDIA_URL[1:], "static.serve", {
            "document_root": settings.MEDIA_ROOT,
            'show_indexes': True,
        }),
    )
