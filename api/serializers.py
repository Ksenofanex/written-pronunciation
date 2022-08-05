from rest_framework import serializers

from dictionary.models import Word


class WordSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source="author.username")
    word_url = serializers.HyperlinkedIdentityField(
        view_name="word-detail", lookup_field="pk"
    )

    class Meta:
        model = Word
        fields = (
            "id",
            "word_url",
            "english",
            "turkish",
            "author_name",
            "date_created",
            "date_updated",
        )

    def create(self, validated_data):
        # For setting the author field currently logged-in user.
        validated_data["author"] = self.context.get("request").user
        return super().create(validated_data)
