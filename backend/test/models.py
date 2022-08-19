from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

class User(Model):
    table = 'user'
    table_description = "用户表"
    uid = fields.CharField(max_length=255,primary_key=True, index=True, description='用户id')
    name = fields.CharField(max_length=255, index=True, description='用户名')
    account = fields.CharField(max_length=255, index=True, description='账号')
    pwd = fields.CharField(max_length=255, index=True, description='密码')
    collect = fields.TextField(null=True, default="[]", description='用户收藏')

    def __str__(self):
        return self.name

    class PydanticMeta:
        exclude = ['pwd']

    def to_dict(self,pwd=True):
        # 自定时使用
        data = {i:getattr(self,i) for i in self.__dict__ if not i.startswith('_')}
        if pwd:
            # 不返回密码
            del data['pwd']
        return data

User_orm = pydantic_model_creator(User,name='user')
User_in_orm = pydantic_model_creator(User,name='UserIn',exclude_readonly=True)


if __name__ == '__main__':
    # 创建数据表
    import asyncio
    from tortoise import Tortoise
    async def init():
        await Tortoise.init(
            db_url='',
            modules={'models': ['models']}
        )
        await Tortoise.generate_schemas() # 创建数据库表
    asyncio.run(init())