from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from procurement import views

urlpatterns = [

    url(r'^$', views.index, name='procurement_index'),

    url(
        r'^pr-form/$',
        login_required(views.PRCreate.as_view()),
        name='pr_form'),

    url(
        r'^pr-create-form/$',
        login_required(views.pr_create),
        name='pr_create'),

    url(
        r'^pr-create/$',
        login_required(views.PurchaseRequestCreate.as_view()),
        name='purchaserequest_create'),

    url(
        r'^pr-update/(?P<pk>[0-9]+)/$',
        login_required(views.PurchaseRequestUpdate.as_view()),
        name='purchaserequest_update'),

    url(
        r'^item-update/(?P<pk>[0-9]+)/$',
        login_required(views.PurchaseItemUpdate.as_view()),
        name='purchaseitem_update'),


    url(
        r'^pr-list/$',
        login_required(views.pr_list),
        name='pr_list'),

    url(
        r'^pr/(?P<pk>[0-9]+)/$',
        login_required(views.purchase_request_view),
        name='pr_view'),

    url(
        r'^pr/(?P<pk>[0-9]+)/(?P<sig_type>\w+)$',
        login_required(views.add_signature),
        name='add_signature'),

    url(
        r'^dashboard/$',
        login_required(views.dashboard),
        name='dashboard'),

    ]