"""
URL configuration for exmaple project.

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
from testapp import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Empmain),
    path('home/', views.Emphome),
    path('resources/', views.Resour),
    path('admin12/', views.Empadmin),
    path('signup/', views.signup),
    path('logout/', views.Emplogout),
    path('work/', views.Empmodel1, name="back"),
    path('forms12/', views.Empforms1),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create/', views.Empcreate, name="create"),
    path('update/<int:pk>/', views.Empupdate.as_view()),
    path('delete/<int:pk>/', views.Empdelete.as_view()),
    path('courses/', views.OnlineTraining),
    # Add other URLs as needed
]