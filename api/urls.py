from rest_framework import routers
from .views import UserViewSet, CommandViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("commands", CommandViewSet)
