from fastapi import APIRouter,Depends


user = APIRouter(tags=['用户相关'])


@user.get("/user",summary="当前用户")
async def user_info():
    return {}



@user.put("/user",summary="修改信息")
async def user_update():
    """
    修改当前用户信息
    :return:
    """
    return {}