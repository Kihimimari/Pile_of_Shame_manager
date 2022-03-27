from django.contrib.auth.models import User
from django.db.models import Model, ForeignKey, DO_NOTHING, CharField, TextField

from viewer.models import Game


class Task(Model):
    userid = ForeignKey(User, on_delete=DO_NOTHING)
    gameid = ForeignKey(Game, on_delete=DO_NOTHING)
    status = CharField(max_length=20, null=True, blank=True)
    comment = TextField(null=True, blank=True)
