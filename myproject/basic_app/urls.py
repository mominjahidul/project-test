from django.conf.urls import url
from basic_app import views

urlpatterns = [
    url(r'^contacts/$', views.ContactList.as_view(),name='contact_list'),
    url(r'^contacts/(?P<pk>[0-9]+)/$', views.ContactDetial.as_view(),name='contact_list'),
]
