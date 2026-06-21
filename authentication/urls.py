from django.urls import path
from . import views



urlpatterns = [
    path('login/', views.LoginView.as_view(), name='user-login' ),
    path('logout/', views.LogoutView.as_view(), name='user-logout' ),
    path('me/', views.MeView.as_view() ,name="user-me"),
    path("reset-password/", views.PasswordResetRequestView.as_view(), name="user-reset-password"),
    path("confirm-new-password/", views.PasswordResetConfirmView.as_view(), name="user-confirm-password")
]