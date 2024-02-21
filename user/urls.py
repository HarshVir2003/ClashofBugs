from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path('signup/', views.UserSignupPage.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),

]
