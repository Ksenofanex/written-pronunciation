from rest_framework import generics
from dictionary.models import Word

from .serializers import WordSerializer
from .permissions import IsAuthorOrReadOnly


class WordList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Word.objects.all()
    serializer_class = WordSerializer