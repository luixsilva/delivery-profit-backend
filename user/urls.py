from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserCreateView.as_view(), name='user-create' ),
    # path('login/', views.UserLoginView.as_view(), name='user-login' )
]