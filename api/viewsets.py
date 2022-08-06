from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from dictionary.models import Word

from api.serializers import WordSerializer
from api.permissions import IsAuthorOrReadOnly
from api.filters import WordFilter


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.select_related("author").filter(is_approved=True)
    serializer_class = WordSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    )
    filterset_class = WordFilter
