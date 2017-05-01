"""microdesk_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from hr import views as hrviews
from procurement import views as procurmentviews
from assets import views as assetsviews
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'MicroDesk Administration'
urlpatterns = [

    url(r'^$', hrviews.index, name='index'),

    url(r'^admin/', admin.site.urls),

    url(r'^hr/', include('hr.urls')),

    url(r'^procurement/', include('procurement.urls')),

    url(r'^assets/', include('assets.urls')),

    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
