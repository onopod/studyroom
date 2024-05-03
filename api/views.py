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
    @action(detail=True, methods=["GET"])
    def create_if_not_exist(self, request, pk=None):
        # ユーザー情報を取得
        user = requests.get("{}/api/users/{}/".format(request._current_scheme_host, pk)).json()
        if not user.get("id"):
            # ユーザーを新規作成
            user = requests.post("{}/api/users/".format(request._current_scheme_host, pk), data={"id": pk, "name": pk}).json()
        return Response(user)

class CommandViewSet(ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer

    @action(detail=False, methods=["POST"])
    def register(self, request):
        command_dict = self.command_dict_from_text(request.data["text"])
        #ユーザーが存在しなければ作成
        user = requests.get("{}/api/users/{}/create_if_not_exist/".format(request._current_scheme_host, command_dict["user"])).json()

        # コマンドを登録
        url = "{}/api/commands/".format(request._current_scheme_host)
        command = requests.post(url, data=json.dumps(command_dict), headers={"Content-Type": "application/json"}).json()

        # コマンドを実行
        res = requests.get("{}/api/commands/{}/execute/".format(request._current_scheme_host, command["id"])).json()
        return Response(res)

    @action(detail=True, methods=["GET"])
    def execute(self, request, pk=None):
        # コマンドの内容を取得
        url = "{}/api/commands/{}/".format(request._current_scheme_host, pk)
        res = requests.get(url).json()
        c = CommandSet(request, res)
        return Response(c.execute())

    @action(detail=False, methods=["GET"])
    def unexecute_unity(self, request):
        unexecute_command = Command.objects.filter(executed_unity=False).order_by("created_at").first()
        serializer = self.get_serializer(unexecute_command)
        return Response(serializer.data)

    def command_dict_from_text(self, text):
        key_arr = ["user", "name", "arg1", "arg2", "arg3", "arg4"]
        command_arr = [s for s in text.split(" ") if s]
        res = {}
        for idx, command in enumerate(command_arr):
            res[key_arr[idx]] = command
        return res
