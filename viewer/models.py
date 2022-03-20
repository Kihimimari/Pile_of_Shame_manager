from django.db.models import Model, CharField, ForeignKey, DO_NOTHING, DateTimeField, TextField


class Genre(Model):
    name = CharField(max_length=256)


class Game(Model):
    name = CharField(max_length=256)
    platform = CharField(max_length=256)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    developer = CharField(max_length=265)
    publisher = CharField(max_length=256)
    first_release_date = DateTimeField()
    summary = TextField()
    cover = TextField()
