from django.urls import path
from formapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("details/", views.details, name="details"),
    path("delete_event/<event_id>", views.delete_event, name="delete-event"),
]
