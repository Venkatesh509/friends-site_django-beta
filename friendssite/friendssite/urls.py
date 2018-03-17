"""friendssite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from myfriends.views import index, details


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', index),
	url(r'^friends/info/(\d+)$', details),

]+static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)

admin.site.site_header = 'Python Friends Site'
#admin.site.index_title='Site Features Area'
