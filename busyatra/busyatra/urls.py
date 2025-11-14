"""
URL configuration for busyatra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminpanel/',views.index, ),
    path('index_code/',views.index_code,),
    path('dashboard/',views.dashboard,),
    path('managebus/',views.managebus,),
    path('manage_routes/',views.manage_routes,),
    path('manage_routes_code/',views.manage_routes_code,),
    path('managebus_code/',views.busmanage_code),
    path('manage_quotas/',views.manage_quotas,),
    path('manage_quotas_code/',views.manage_quotas_code),
    path('',views.bus,),
    path('searchcode/',views.searchcode,),
    path('viewbus/<int:id>',views.viewbus,),
    path('booknow/<int:id>',views.booknow,),
    path('booknowcode/',views.booknowcode,),
    path('confirmation/',views.confirmation,),
    path('confirmcode/<int:id>',views.confirmcode),
    path('bookin_view/',views.bookin_view,),

]
