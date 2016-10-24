from django.conf.urls import url
from . import views

"""having a default homepage -> where you go to the index of each app section (sub-homepage)
this is called index"""
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
