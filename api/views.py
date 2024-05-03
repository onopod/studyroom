from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Command
from .serializer import UserSerializer, CommandSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CommandViewSet(ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer

    @action(detail=False, methods=["GET"])
    def latest(self, request):
        latest_command = Command.objects.latest("created_at")
        serializer = self.get_serializer(latest_command)
        return Response(serializer.data)
