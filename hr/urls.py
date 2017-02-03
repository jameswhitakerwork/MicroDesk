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

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
