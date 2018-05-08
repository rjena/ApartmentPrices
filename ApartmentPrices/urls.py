from django.conf.urls import include, url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api', views.ApartmentViewSet)

app_name = 'ApartmentPrices'
urlpatterns = [
    url(r'^$', views.ApartmentPrices_list, name='ApartmentPrices_list'),
    url(r'^(?P<apartment_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^apartment/new/$', views.apartment_new, name='apartment_new'),
    url(r'^',include(router.urls))
]