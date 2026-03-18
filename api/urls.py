from rest_framework.routers import DefaultRouter

from api.viewsets import WordViewSet

app_name = "v1"

router = DefaultRouter()
router.register("words", WordViewSet, basename="word")

urlpatterns = router.urls
