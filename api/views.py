from rest_framework.viewsets import ModelViewSet
from .models import User, Command
from .serializer import UserSerializer, CommandSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CommandViewSet(ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer

