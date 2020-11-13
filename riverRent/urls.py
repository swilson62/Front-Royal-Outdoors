from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("category/<str:tripCategory>", views.category, name="category"),
    path("trip/<str:tripSelection>", views.trip, name="trip"),
    path("avail/<str:tripSelection>", views.avail, name="avail"),
    path("cart", views.cart, name="cart"),
]
