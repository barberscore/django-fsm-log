
# Third-Party
from rest_framework import routers

# Local
from .views import StateLogViewSet

router = routers.DefaultRouter(
    trailing_slash=False,
)

router.register(r'statelog', StateLogViewSet)
urlpatterns = router.urls
