from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^products$', views.category_list),
    url(r'^products/(?P<slug>.*)/$', views.category_detail),
]
