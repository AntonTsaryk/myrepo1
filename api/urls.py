from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ServiceCategoryViewSet, WorkerViewSet, JobViewSet, ApplicationViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'service-categories', ServiceCategoryViewSet)
router.register(r'workers', WorkerViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = router.urls
