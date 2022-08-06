from django.urls import path

from dictionary.views import (
    WordListView,
    WordDetailView,
    WordCreateView,
    WordUpdateView,
    WordDeleteView,
    SearchResultsView,
    UserWordListView,
)


urlpatterns = [
    # Word List & Detail.
    path("", WordListView.as_view(), name="home"),
    path("<int:pk>/", WordDetailView.as_view(), name="word-detail"),
    # CRUD.
    path("create/", WordCreateView.as_view(), name="word-create"),
    path("<int:pk>/update/", WordUpdateView.as_view(), name="word-update"),
    path("<int:pk>/delete/", WordDeleteView.as_view(), name="word-delete"),
    # Search.
    path("search/", SearchResultsView.as_view(), name="search"),
    # User's Words.
    path(
        "user-words/<str:username>/",
        UserWordListView.as_view(),
        name="user-words",
    ),
]
