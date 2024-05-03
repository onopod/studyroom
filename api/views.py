import requests
import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Command
from .serializer import UserSerializer, CommandSerializer
from .commandset import CommandSet

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

    @action(detail=False, methods=["POST"])
    def register(self, request):
        command_dict = self.command_dict_from_text(request.data["text"])
        url = "{}/api/commands/".format(request._current_scheme_host)
        res = requests.post(url, data=json.dumps(command_dict), headers={"Content-Type": "application/json"})
        return Response(res.json())

    @action(detail=True, methods=["GET"])
    def execute(self, request, pk=None):
        # コマンドの内容を取得
        url = "{}/api/commands/{}/".format(request._current_scheme_host, pk)
        res = requests.get(url).json()
        c = CommandSet(request, res)
        return Response(c.execute())

    def command_dict_from_text(self, text):
        key_arr = ["user", "name", "arg1", "arg2", "arg3", "arg4"]
        command_arr = [s for s in text.split(" ") if s]
        res = {}
        for idx, command in enumerate(command_arr):
            res[key_arr[idx]] = command
        return res
