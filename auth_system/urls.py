from django.urls import path
from auth_system import views

urlpatterns=[
    path("register/", views.register, name="register"),
    path("auth_login/", views.auth_login, name="auth_login"),
    path("auth_logout/", views.auth_logout, name="auth_logout"),
]