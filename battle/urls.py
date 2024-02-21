from django.urls import path

from . import views

app_name = "battle"

urlpatterns = [
    path("", views.index, name="battle"),
    path('get-updated-value/', views.get_updated_value, name='get_updated_value'),
    path("<str:room_name>/", views.room, name="room"),


]
