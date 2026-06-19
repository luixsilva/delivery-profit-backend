from django.urls import path
from . import views

urlpatterns = [
    path('vehicles/', views.VehiclesCreateListView.as_view(), name='vehicle-create-list' ),
    path('vehicles/<int:pk>/', views.VehiclesRetriveUpdateDestroy.as_view(), name='vehicle-details' )
]