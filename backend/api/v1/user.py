from fastapi import APIRouter,Depends


user = APIRouter(tags=['用户相关'])


@user.get("/user",summary="当前用户")
async def usr_info():
    return {}

