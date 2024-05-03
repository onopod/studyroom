from rest_framework.serializers import ModelSerializer
from .models import User, Command

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CommandSerializer(ModelSerializer):
    class Meta:
        model = Command
        fields = "__all__"
