from rest_framework import viewsets

from dictionary.models import Word

from api.serializers import WordSerializer
from api.permissions import IsAuthorOrReadOnly


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.select_related("author")
    serializer_class = WordSerializer
    permission_classes = (IsAuthorOrReadOnly,)
