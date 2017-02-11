from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from hr import views


urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(
        r'^staff/(?P<staff_id>[0-9]+)/',
        views.staff_view, name='staff_view'),

    url(r'^staff/$', views.staff_list, name='staff_list'),

    url(r'^staff-form/$', views.staff_form, name='staff_form'),

    url(
        r'^contract-form/$',
        views.ContractView.as_view(),
        name='contract_form'),

    url(
        r'^position-form/$',
        views.PositionView.as_view(),
        name='position_form'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
