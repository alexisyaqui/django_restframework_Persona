from rest_framework import routers
from .api import DpiViewSet, PersonaViewSet



router = routers.DefaultRouter()



router.register('api/dpi', DpiViewSet, 'dpi')
router.register('api/persona', PersonaViewSet, 'persona')




urlpatterns = router.urls