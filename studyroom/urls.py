from django.contrib import admin
from django.urls import path, include
from api.urls import router as api_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api_router.urls)),
    path("display/", include("display.urls"))
]
