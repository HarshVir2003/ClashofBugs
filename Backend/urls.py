"""
URL configuration for Backend project.

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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from  . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("dashboard/", include("dashboard.urls")),
    path("learn/", include("coding.urls")),
    path("tournament/", include("tournaments.urls")),
    path("", include("user.urls")),
    path("accounts/", include("allauth.urls")),
    path("battle/", include("battle.urls")),
    path("win/", views.win, name="win"),
    path("lose/", views.lose, name="lose"),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password/password_reset_form.html"),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_done.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_success.html"),
         name='password_reset_complete'),
]
