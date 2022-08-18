from fastapi import APIRouter,Depends


movie = APIRouter(tags=['电影内容相关'])


@movie.get("/movie",summary="电影列表")
async def movie_list():
    return {}

@movie.post("/movie",summary="新增电影列表")
async def movie_create():
    return {}

@movie.put("/movie/{}",summary="编辑电影")
async def movie_update():
    return {}

@movie.delete("/movie/{pk}",summary="删除电影")
async def movie_list():
    return {}