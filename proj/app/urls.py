"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('home/add/', views.add, name='add'),
    path('home/add/addrecord/', views.addrecord, name='addrecord'),
    path('home/update/<int:id>', views.update, name='update'),
    path('home/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('home/delete/<int:id>', views.delete, name='delete'),
    path('home/delete/deleterecord/<int:id>', views.deleterecord, name='deleterecord'),
]
