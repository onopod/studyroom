from django.utils import timezone
from django.db.models import Model, CharField, DateTimeField, BooleanField, ForeignKey, CASCADE

class User(Model):
    id = CharField(max_length=100, primary_key=True)
    name = CharField(max_length=400)
    emote = CharField(max_length=10, null=True)
    chara = CharField(max_length=10, null=True)
    place = CharField(max_length=10, null=True)
    subject = CharField(max_length=100, default="指定なし")
    comment = CharField(max_length=100, null=True)
    created_at = DateTimeField(default=timezone.now)

    def __repr__(self):
        return "{}: {}".format(self.id, self.name)

    __str__ = __repr__

class Command(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=100)
    arg1 = CharField(max_length=100, null=True)
    arg2 = CharField(max_length=100, null=True)
    arg3 = CharField(max_length=100, null=True)
    arg4 = CharField(max_length=100, null=True)
    executed_unity = BooleanField(default=False)
    created_at = DateTimeField(default=timezone.now)

    def __repr__(self):
        return "{}: {} {} {}".format(self.id, self.name, self.executed_web, self.executed_unity)
    
    __str__ = __repr__
