from django.contrib import admin
from django.urls import path, include

from notes import views as notes_views

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', notes_views.index, name='home'),
    path('about/', notes_views.about, name='about'),
    path('notes/', include('notes.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('api.urls')),
# OpenAPI schema
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),

    # Swagger UI
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),

    # ReDoc
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),

]
