from django.urls import path

from shipments import views

urlpatterns = [
    path('shipments/', views.shipments, name="shipments"),
    path('shipments/<int:pk>/', views.shipments_specific),
]
