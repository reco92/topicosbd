from django.conf.urls import patterns, url

from excesos import views

urlpatterns = patterns('',
    url(r'^$', views.indice_principal, name='index')
)