from django.urls import path
from . import views

urlpatterns = [
    path('routes/', views.RouteCreateListView.as_view(), name='route-create-list' ),
    path('routes/<int:pk>/', views.RouteRetrieveUpdateDestroy.as_view(), name='route-detail-view')
]