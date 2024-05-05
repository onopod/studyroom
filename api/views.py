from datetime import datetime, timedelta
import requests
import json
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Study, Command
from .serializer import UserSerializer, StudySerializer, CommandSerializer
from .commandset import CommandSet

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=True, methods=["GET"])
    def changestatus(self, request, pk=None):
        message_dict = {
            "emote": "{}さんのエモートを{}に変更しました。",
            "place": "{}さんが{}に移動しました。",
            "subject": "{}さんが学習内容を{}に設定しました。",
            "comment": "{}「{}」",
            "chara": "{}さんがキャラを{}に設定しました。"

        }
        status_name = list(set(message_dict.keys()) & set(request.query_params.keys()))[0]
        user, _ = User.objects.update_or_create(
            pk=pk,
            defaults={
                "name": request.query_params.get("name"),
                status_name: request.query_params.get(status_name)
            }
        )
        return Response(message_dict[status_name].format(
            user.name, 
            getattr(user, status_name)
        ))

    @action(detail=True, methods=["GET"])
    def nightbot(self, request, pk=None):
        print("user id is", pk, "query_params is", request.query_params)
        return Response("this is test")
    
class StudyViewSet(ModelViewSet):
    queryset = Study.objects.all()
    serializer_class = StudySerializer

    @action(detail=False, methods=["GET"], url_path="in")
    def study_in(self, request):
        user, _ = User.objects.get_or_create(
            pk=request.query_params.get("id"),
            defaults={
                "name": request.query_params.get("name"),
            }
        )
        study = Study(**{
            "user": user, 
            "subject": user.subject, 
            "estimated_end_at": datetime.now() + timedelta(hours=1)
        })
        study.save()
        serializer = self.get_serializer(study)

        return Response("{}さんが学習を開始しました{}-[予定]{}".format(
            user.name,
            study.start_at.strftime("%H:%M"),
            study.estimated_end_at.strftime("%H:%M")
        ))

    @action(detail=False, methods=["GET"])
    def charge(self, request):
        user, _ = User.objects.get_or_create(
            pk=request.query_params.get("id"),
            defaults={
                "name": request.query_params.get("name"),
            }
        )
        study = Study.objects.filter(end_at=None).order_by("-start_at").first()
        if not study:
            return Response("{}さん：学習が開始されていません。先にinコマンドを実行してください。".format(user.name))
        study.estimated_end_at = study.estimated_end_at + timedelta(hours=1)
        study.save()
        return Response("{}さんが学習を延長しました{}-[予定]{}".format(
            user.name,
            study.start_at.strftime("%H:%M"),
            study.estimated_end_at.strftime("%H:%M")
        ))

    @action(detail=False, methods=["GET"], url_path="out")
    def study_out(self, request):
        user, _ = User.objects.get_or_create(
            pk=request.query_params.get("id"),
            defaults={
                "name": request.query_params.get("name"),
            }
        )
        study = Study.objects.filter(end_at=None).order_by("-start_at").first()
        if not study:
            return Response("{}さん：学習が開始されていません。先にinコマンドを実行してください。".format(user.name))
        study.end_at = timezone.now()
        study.save()
        return Response("{}さんが学習を終了しました{}-{} お疲れ様でした。".format(
            user.name,
            study.start_at.strftime("%H:%M"),
            study.end_at.strftime("%H:%M")
        ))
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
