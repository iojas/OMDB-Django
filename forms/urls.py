from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^show/$', views.showForm),
    url(r'^login/$', views.showLogin),
]