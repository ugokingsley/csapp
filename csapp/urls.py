"""csapp URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from cs.views import index
from cs.views import agents
from cs.views import agents_form
from cs.views import dg
from cs.views import nafdac
from cs.views import son
from cs.views import others
from cs.views import home
from cs.views import ChartData
from cs.views import login_success
from cs.views import HomeView
from cs.views import get_data

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^customer/$',index,name="index"),
    url(r'^officers/$',agents,name="agents"),
    url(r'^officers-form/$',agents_form,name="agents_form"),
    url(r'^director-general/$',dg,name="dg"),
    url(r'^nafdac/$',nafdac,name="nafdac"),
    url(r'^son/$',son,name="son"),
    url(r'^others/$',others,name="others"),
    url(r'login_success/$',login_success, name='login_success'),
    url(r'^$', home,name='home'),

    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^chart/$', HomeView.as_view(), name='home'),
]
