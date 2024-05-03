import requests
import json
from rest_framework.response import Response

class CommandSet:
    command_names = ["in", "out", "charge", "set", "moveto", "info", "infoall", "comment", "emote", "chara"]
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

    def get_user_subject(self):
        return self.user["subject"]

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
                "{}の".format(self.get_user_subject()) if self.get_user_subject() else ""
            )
        )
    def command_out(self):
        self.set_message("{}さんが{}学習を終了しました。".format(
                self.get_user_name(),
                "{}の".format(self.get_user_subject()) if self.get_user_subject() else ""
            )
        )
    
    def command_charge(self):
        pass
    def command_set(self):
        pass
    def command_moveto(self):
        pass
    def command_info(self):
        pass
    def command_info(self):
        pass
    def command_infoall(self):
        pass
    def command_comment(self):
        pass
    def command_emote(self):
        pass
    def command_chara(self):
        pass
