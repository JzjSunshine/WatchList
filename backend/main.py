import uvicorn

from api import app

if __name__ == '__main__':
    uvicorn.run("main:app",host='0.0.0.0',port=8081,debug=True, reload=True,workers=1)