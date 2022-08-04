from rest_framework.routers import DefaultRouter

from api.viewsets import WordViewSet

router = DefaultRouter()
router.register("words", WordViewSet, basename="word")
