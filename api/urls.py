from django.urls import path
from .views import WordList, WordDetail


urlpatterns = [
    path("", WordList.as_view(), name="api-home"),
    path("<int:pk>/", WordDetail.as_view(), name="api-word-detail"),
]
