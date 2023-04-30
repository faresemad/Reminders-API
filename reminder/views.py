from .models import Reminder, Category
from .serializers import ReminderSerializer, CategorySerializer
from rest_framework.viewsets import ModelViewSet

class ReminderViewSet(ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer