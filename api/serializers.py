from rest_framework import serializers
from .views import Word


class WordSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    word_url = serializers.HyperlinkedIdentityField(view_name='api-word-detail', lookup_field='pk')

    class Meta:
        model = Word
        fields = ('id', 'word_url', 'english', 'turkish', 'author_name', 'author',)