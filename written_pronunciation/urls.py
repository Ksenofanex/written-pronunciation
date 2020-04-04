from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'Pronunciation API'
API_DESCRIPTION = 'A cool written pronunciation site.'
schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('', include('dictionary.urls')),
    path('admin/', admin.site.urls),

    # Django authentication.
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),

    # API.
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')), # Djangorestframework built-in api log in & out.

    # Django-rest-auth framework.
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),

    # Schema and documents.
    path('swagger-docs/', schema_view),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]
