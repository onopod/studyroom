from datetime import datetime, timedelta
import requests
import json
from django.utils import timezone
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Study, Command
from .filters import StudyFilter
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
        Command(user=user, user_name=user.name, command_name=status_name, arg1=request.query_params.get(status_name)).save()
        return Response(message_dict[status_name].format(
            user.name, 
            getattr(user, status_name)
        ))
    
class StudyViewSet(ModelViewSet):
    queryset = Study.objects.all()
    serializer_class = StudySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = StudyFilter

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

        Command(user=user, user_name=user.name, command_name="in").save()
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
        Command(user=user, user_name=user.name, command_name="charge").save()
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
        Command(user=user, user_name=user.name, command_name="out").save()
        return Response("{}さんが学習を終了しました{}-{} お疲れ様でした。".format(
            user.name,
            study.start_at.strftime("%H:%M"),
            study.end_at.strftime("%H:%M")
        ))

class CommandViewSet(ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer

    @action(detail=False, methods=["GET"])
    def unexecute_unity(self, request):
        unexecute_command = Command.objects.filter(executed_unity=False).order_by("created_at").first()
        
        if not unexecute_command:
            return Response("")

        serializer = self.get_serializer(unexecute_command)
        # 実行済にする
        unexecute_command.executed_unity = True
        unexecute_command.save()
        return Response(serializer.data)
