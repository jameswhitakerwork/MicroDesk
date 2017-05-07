from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from reports import views

urlpatterns = [

    url(r'^report-create/$', views.ReportCreate.as_view(), name='report-create'),

    url(r'^report-submit/(?P<pk>[0-9]+)/$', views.ReportSubmit.as_view(), name='report-submit'),

    url(r'^report-list/$', views.report_list, name='report-list'),

    url(r'^$', views.report_list, name='report-list'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)