from rest_framework import routers
from .views import UserViewSet, StudyViewSet, CommandViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("studies", StudyViewSet)
router.register("commands", CommandViewSet)
