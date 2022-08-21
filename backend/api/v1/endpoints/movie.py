from typing import List,Any,Union

from fastapi import APIRouter,Depends
from backend.schemas import Movie_Pydantic,MovieIn_Pydantic,Response200,Response400

from backend.models import Movie
from backend.core import deps

movie = APIRouter(tags=['电影内容相关'])
# movie = APIRouter(tags=['电影内容相关'],dependencies=[deps.get_current_user]) # 这样写的话，以下所有API访问都需要登陆

@movie.get("/movie",summary="电影列表",response_model=Union[Response200,Response400])
async def movie_list(limit:int = 10,page:int = 1):
    skip = (page - 1) * limit
    try:
        # SELECT * FROM 表名 LIMIT 1 OFFSET 3;   #从第4条数据开始取数，取1条数据，即只取第四条
        all_result = await Movie_Pydantic.from_queryset(Movie.all().offset(skip).limit(limit).order_by('-id'))
        # print(type(all_result))
        # print(all_result) #[Movie(id=4, name='流浪地球', year='2021'), Movie(id=3, name='战狼2', year='2020'),
        data = {
            "total": await Movie.all().count(),
            "movies": all_result
        }
        return Response200(data=data)
    except Exception as e:
        return Response400(msg="请求失败：{}" + str(e))


@movie.post("/movie",summary="新增电影列表")
async def movie_create(movie_from:MovieIn_Pydantic,token:Any = Depends(deps.get_current_user)):
    return Response200(data= await Movie_Pydantic.from_tortoise_orm(await Movie.create(**movie_from.dict())))


@movie.put("/movie/{pk}",summary="编辑电影")
async def movie_update(pk:int,movie_from:MovieIn_Pydantic,token:Any = Depends(deps.get_current_user)):
    if await Movie.filter(pk=pk).update(**movie_from.dict()):
        return Response200()
    return Response400(msg="更新失败")


@movie.delete("/movie/{pk}",summary="删除电影")
async def movie_list(pk:int,token:Any = Depends(deps.get_current_user)):
    if await Movie.filter(pk=pk).delete():
        return Response200()
    return Response400(msg="更新失败")