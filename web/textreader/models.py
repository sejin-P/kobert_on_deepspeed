from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, CASCADE

# Create your models here.
from django.db.models import CharField, TextField
from graphene import ObjectType


class Uploader(User):
    name = CharField(max_length=100, default='user')

    def __str__(self):
        return f'Uploader number {self.id}'


class Text(models.Model):
    name = CharField(max_length=100, default='text')
    user = ForeignKey(Uploader, related_name='texts', on_delete=CASCADE)
    text = TextField()
    category = CharField(max_length=100, default='unknown')
    class Meta:
        ordering = ['-modified_at']
        unique_together = [['user', 'text']]