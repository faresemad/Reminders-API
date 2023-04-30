from rest_framework_nested.routers import NestedDefaultRouter, DefaultRouter
from .views import ReminderViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'list', CategoryViewSet, basename='list')

reminder_router = NestedDefaultRouter(router, r'list', lookup='list')
reminder_router.register(r'reminder', ReminderViewSet, basename='reminder')

urlpatterns = router.urls + reminder_router.urls