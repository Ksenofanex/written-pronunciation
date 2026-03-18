from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from api.urls import router as api_router

urlpatterns = [
    path("", include("dictionary.urls")),
    path("admin/", admin.site.urls),
    # Django authentication.
    path("users/", include("users.urls")),
    path("users/", include("django.contrib.auth.urls")),
    # API.
    path("api/", include((api_router.urls, "v1"))),
    path(
        "api-auth/", include("rest_framework.urls")
    ),  # Djangorestframework built-in api log in & out.
    # Django-rest-auth framework.
    path("api/v1/rest-auth/", include("dj_rest_auth.urls")),
    path(
        "api/v1/rest-auth/registration/",
        include("dj_rest_auth.registration.urls"),
    ),
    # Schema and documentation.
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
