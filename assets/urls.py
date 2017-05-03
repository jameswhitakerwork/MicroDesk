from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from assets import views


urlpatterns = [

    url(
        r'^asset-create/',
        views.assetcreate, name='asset_create'),

    url(
        r'^asset-list/',
        views.asset_list, name='asset_list'),

    url(
        r'^asset-view/(?P<pk>[0-9]+)/',
        views.assetview, name='asset_view'),

    url(
        r'^checkout-create/(?P<asset_id>[0-9]+)/',
        login_required(views.Checkout_Create.as_view()), name='checkout_create'),

    url(
        r'^checkin-create/(?P<asset_id>[0-9]+)/',
        login_required(views.Checkin_Create.as_view()), name='checkin_create'),

    url(
        r'^download-assets/',
        views.download_assets, name='download_assets'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
