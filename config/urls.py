"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from restaurants.views import RestaurantViewSet, MenuItemViewSet
from orders.views import OrderViewSet

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r"menu-items", MenuItemViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="QuickFood API",
        default_version="v1",
        description="API documentation for the QuickFood Online Food Delivery System",
        terms_of_service="https://www.quickfood.com/terms/",
        contact=openapi.Contact(email="support@quickfood.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=()
)

urlpatterns = [
    path("admin/", admin.site.urls),
     path("api/orders/", include("orders.urls")), 
     path("api/", include(router.urls)), 
    path("api/restaurants/", include("restaurants.urls")),
    path("api/auth/", include("users.urls")),
    path(
        "api/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"
    ),
      # ReDoc (alternative documentation)
    path("api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),

    # Raw JSON schema
    path("api/schema.json/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)