from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from hr import views


urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(
        r'^staff/(?P<staff_id>[0-9]+)/',
        views.staff_view, name='staff_view'),

    url(r'^staff/$', views.staff_list, name='staff_list'),

    url(
        r'^staff-form/$',
        login_required(views.StaffCreate.as_view()),
        name='staff_form'),

    url(
        r'^contract-form/$',
        login_required(views.ContractCreate.as_view()),
        name='contract_form'),

    url(
        r'^position-form/$',
        login_required(views.PositionCreate.as_view()),
        name='position_form'),

    url(
        r'^staff-update/(?P<pk>[0-9]+)/$',
        login_required(views.StaffUpdate.as_view()),
        name='staff_update'),

    url(
        r'^position-update/(?P<pk>[0-9]+)/$',
        login_required(views.PositionUpdate.as_view()),
        name='position_update'),

    url(
        r'^contract-update/(?P<pk>[0-9]+)/$',
        login_required(views.ContractUpdate.as_view()),
        name='contract_update'),

    url(
        r'^position/(?P<pk>[0-9]+)/$',
        login_required(views.PositionView.as_view()),
        name='position_view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
