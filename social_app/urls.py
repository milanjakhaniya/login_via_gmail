"""social_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# social_app/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views



urlpatterns = [
    path('admin/', admin.site.urls),


    #Adding social auth path
    path('social-auth/', include('social_django.urls', namespace="social")),
    
    path("", views.home, name="home"),
    path("user-home/", views.user_home, name="user-home"),
    path("admin-home/", views.admin_home, name="admin-home"),
    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('courses/', views.course_list, name='course_list'),
    path('add_course/', views.add_course, name='add_course'),
    path('update_view_list/', views.update_view_list, name='update_view_list'),
    path('update_course/<int:course_id>/', views.update_course, name='update_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),

    
]


