from django_filters import rest_framework as filters

from dictionary.models import Word


class WordFilter(filters.FilterSet):
    english = filters.CharFilter(
        field_name="english",
        lookup_expr="icontains",
    )
    turkish = filters.CharFilter(
        field_name="turkish",
        lookup_expr="icontains",
    )
    author = filters.CharFilter(
        field_name="author__username",
        lookup_expr="icontains",
    )

    class Meta:
        model = Word
        fields = ["english", "turkish", "author"]
