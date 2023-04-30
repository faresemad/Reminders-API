from django.urls import path
from .views import ReminderViewSet, CategoryViewSet

urlpatterns = [
    path('reminders/', ReminderViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('reminders/<int:pk>/', ReminderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
