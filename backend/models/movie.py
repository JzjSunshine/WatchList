from typing import Optional,Iterable

from tortoise import models,BaseDBAsyncClient
from tortoise import fields



class Movie(models.Model):
    name = fields.CharField(max_length=50,null=False,description="电影名称")
    year = fields.CharField(max_length=50,null=False,description="电影年份")


