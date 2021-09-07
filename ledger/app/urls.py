from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("get_data", views.get_data, name="get_data"),
    path("add", views.add_new, name="add"),
    path("stats", views.stats, name="stats")
]