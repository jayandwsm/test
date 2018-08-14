from django.conf.urls import url
from rapp import views

urlpatterns = [
    url(r'^set_redis/',views.set_redis),
    url(r'^read_redis/',views.read_redis),
    url(r'^p/',views.p),
    url(r'^insert_object/',views.insert_object),
]