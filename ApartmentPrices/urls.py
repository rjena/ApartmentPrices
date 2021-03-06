from django.conf.urls import url
from . import views

app_name = 'ApartmentPrices'
urlpatterns = [
    url(r'^$', views.ApartmentPrices_list, name='ApartmentPrices_list'),
    url(r'^(?P<apartment_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^new/$', views.apartment_new, name='apartment_new'),
    url(r'api', views.apartment_api),
    url(r'districts', views.district_api),
    url(r'materials', views.material_api)
]
