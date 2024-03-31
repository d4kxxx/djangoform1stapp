from django.contrib import admin
from django.urls import include, path
from formapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("formapp.urls")),
]
