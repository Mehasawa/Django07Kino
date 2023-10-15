"""
URL configuration for Django07 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('kino/', views.Kinolist123.as_view(), name='allkino'),
    # path('kino/<int:id>/<str:title>', views.info, name='info'),
    path('kino/<slug:pk>/<str:title>', views.KinoDetail.as_view(), name='info'),
    path('user/', include('django.contrib.auth.urls')),
    path('actors/', views.AcList.as_view(), name='actors'),
    path('dirs/', views.DiList.as_view(), name='dirs'),
    path('actors/<slug:pk>', views.AcDetail.as_view(), name='infoactor'),
    path('dirs/<slug:pk>', views.DiDetail.as_view(), name='infodir'),
    path('status/', views.statusView, name='status'),
    path('prosmotr/<str:k2>', views.prosmotr, name='prosmotr'),
    path('buy/<int:type>', views.buy, name='buy'),
    path('user/reg', views.reg, name='reg')
]
