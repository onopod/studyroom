import requests
import json
from rest_framework.response import Response

class CommandSet:
    command_names = ["in", "out", "charge", "subject", "place", "info", "infoall", "comment", "emote", "chara"]
    def __init__(self, request, command_dict):
        self.request = request
        self.command_dict = command_dict
        self.set_user()

    def set_user(self):
        res = requests.get(
            "{}/api/users/{}/".format(
                self.request._current_scheme_host,
                self.get_user_id()
            )
        )
        self.user = res.json()

    def get_user_name(self):
        return self.user["name"]

    def get_subject(self):
        return self.user["subject"]
    def get_place(self):
        return self.user["place"]
    def get_emote(self):
        return self.user["emote"]
    def get_chara(self):
        return self.user["chara"]
    def get_comment(self):
        return self.user["comment"]

    def get_id(self):
        return self.command_dict["id"]

    def get_user_id(self):
        return self.command_dict["user"]

    def get_command(self):
        return self.command_dict["name"][1:]

    def get_args(self):
        return [
            self.command_dict["arg1"], 
            self.command_dict["arg2"], 
            self.command_dict["arg3"], 
            self.command_dict["arg4"]
        ]
    
    def is_command(self):
        return self.get_command() in self.command_names

    def execute(self):
        if self.is_command():
            # コマンドを実行
            eval("self.command_{}".format(self.get_command()))()
            #実行済にする
            res = requests.patch(
                "{}/api/commands/{}/".format(
                    self.request._current_scheme_host,
                    self.get_id()
                ),
                data={"executed_web": True}
            )
        return {"message": self.get_message()}

    def set_message(self, message):
        self.message = message
    def get_message(self):
        return self.message
    def command_in(self):
        self.set_message("{}さんが{}学習を開始しました。".format(
                self.get_user_name(),
                "{}の".format(self.get_subject()) if self.get_subject() else ""
            )
        )
    def command_out(self):
        self.set_message("{}さんが{}学習を終了しました。".format(
                self.get_user_name(),
                "{}の".format(self.get_subject()) if self.get_subject() else ""
            )
        )
    
    def command_charge(self):
        self.set_message("{}さんが学習時間を延長しました。".format(
                self.get_user_name(),
            )
        )
    def command_subject(self):
        res = requests.patch(
            "{}/api/users/{}/".format(
                self.request._current_scheme_host,
                self.get_user_id()
            ),
            data={"subject": self.get_args()[0]}
        )
        self.set_user()
        self.set_message("{}さんが学習内容を{}に設定しました。".format(
                self.get_user_name(),
                self.get_subject()
            )
        )
    def command_place(self):
        res = requests.patch(
            "{}/api/users/{}/".format(
                self.request._current_scheme_host,
                self.get_user_id()
            ),
            data={"place": self.get_args()[0]}
        )
        self.set_user()
        self.set_message("{}さんが{}に移動しました。".format(
                self.get_user_name(),
                self.get_place()
            )
        )
    def command_comment(self):
        res = requests.patch(
            "{}/api/users/{}/".format(
                self.request._current_scheme_host,
                self.get_user_id()
            ),
            data={"comment": self.get_args()[0]}
        )
        self.set_user()
        self.set_message("{}「{}」".format(
                self.get_user_name(),
                self.get_comment()
            )
        )
    def command_info(self):
        pass
    def command_infoall(self):
        pass
    def command_emote(self):
        res = requests.patch(
            "{}/api/users/{}/".format(
                self.request._current_scheme_host,
                self.get_user_id()
            ),
            data={"emote": self.get_args()[0]}
        )
        self.set_user()
        self.set_message("{}さんがemoteを{}に変更しました。".format(
                self.get_user_name(),
                self.get_emote()
            )
        )
    def command_chara(self):
        res = requests.patch(
            "{}/api/users/{}/".format(
                self.request._current_scheme_host,
                self.get_user_id()
            ),
            data={"chara": self.get_args()[0]}
        )
        self.set_user()
        self.set_message("{}さんがcharaを{}に変更しました。".format(
                self.get_user_name(),
                self.get_chara()
            )
        )
