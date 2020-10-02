from rest_framework import generics
from dictionary.models import Word

from .serializers import WordSerializer
from .permissions import IsAuthorOrReadOnly


class WordList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    
    def perform_create(self, serializer): # For setting the author field currently logged-in user.
        serializer.validated_data['author'] = self.request.user
        return super(WordList, self).perform_create(serializer)


class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Word.objects.all()
    serializer_class = WordSerializer
