"""school_online_quiz URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from online_quiz import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.homepage.as_view()),
    url(r'^(?P<pk>\d+)/$', views.exam_ready_page.as_view()),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^staff_login/',views.staff_login),
    url(r'^create_quiz/',views.create_quiz),
    url(r'^quiz/',views.quiz),
    url(r'^result/',views.result),
    url(r'^saveans/',views.saveans),





]
