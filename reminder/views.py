from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import ReminderSerializer, CategorySerializer
from .models import Reminder, Category

class ReminderViewSet(ModelViewSet):
    serializer_class = ReminderSerializer
    
    def get_queryset(self):
        return Reminder.objects.filter(auther=self.request.user)

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.filter(auther=self.request.user)