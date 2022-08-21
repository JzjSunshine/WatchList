from typing import Optional,Iterable

from tortoise import fields,models,BaseDBAsyncClient

from backend.core import get_password_hash

class User(models.Model):
    id = fields.IntField(pk=True,allows_generated=True)

    username = fields.CharField(max_length=20,null=False,description='用户名')
    password = fields.CharField(max_length=128,null=False,description="密码")
    nickname = fields.CharField(max_length=20,null=True,description="昵称",default='你好')

    async def save(
            self,
            using_db:Optional[BaseDBAsyncClient] = None,
            update_fields:Optional[Iterable[str]] =None,
            force_create:bool = False,
            force_update:bool = False
    ):
        if force_create or 'password' in update_fields:
            self.password = get_password_hash(self.password)

        await super(User, self).save(using_db,update_fields,force_create,force_update)

    # class PydanticMeta:
    #     computed = ["full_name"]
    #     exclude = ["password_hash"]

