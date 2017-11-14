"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from todo.core import views

from todo.tarefas import urls as tarefas_urls
from todo.accounts import urls as accounts_urls

urlpatterns = [
    url(r'^$', views.home, name='core'),
    url(r'^accounts/', include(accounts_urls, namespace='accounts')),
    url(r'^tarefas/', include(tarefas_urls, namespace='tarefas')),
    url(r'^admin/', admin.site.urls),
]
