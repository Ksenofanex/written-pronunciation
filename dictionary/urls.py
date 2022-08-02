from django.urls import path

from dictionary.views import (
    WordListView,
    WordDetailView,
    WordCreateView,
    WordUpdateView,
    WordDeleteView,
    SearchResultsView,
)


urlpatterns = [
    # Word List & Detail.
    path("", WordListView.as_view(), name="home"),
    path("<int:pk>/", WordDetailView.as_view(), name="word_detail"),
    # CRUD.
    path("create/", WordCreateView.as_view(), name="word_create"),
    path("<int:pk>/update/", WordUpdateView.as_view(), name="word_update"),
    path("<int:pk>/delete/", WordDeleteView.as_view(), name="word_delete"),
    # Search.
    path("search/", SearchResultsView.as_view(), name="search"),
]
