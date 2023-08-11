from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("pages.urls")),
    # path("", include("posts.urls")),
    path("", include("books.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("articles/", include("articles.urls")),  # new
    path("bankomat/", include("bankomat.urls")),
    # path("api/", include("apis.urls")),
    path("api/", include("todos.urls")),
    path("api/v1/", include("posts.urls")),
    path("api-auth/", include("rest_framework.urls")),  # new
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
    path(
        "api/v1/dj-rest-auth/registration/",
        include("dj_rest_auth.registration.urls"),
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
        
    ),  
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(
url_name="schema"), name="swagger-ui"), # new
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
