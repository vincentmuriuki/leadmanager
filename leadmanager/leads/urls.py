from rest_framework import routers
from .api import LeadsViewSet

router = routers.DefaultRouter()

router.register('api/leads', LeadsViewSet, 'leads')

urlpatterns = router.urls