from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'store.views.home'),
    url(r'^store/(?P<store_id>\d+)/$', 'store.views.store_id'),
    url(r'^store/(?P<store_id>\d+)/check_in/$', 'store.views.store_id_check_in'),
)
