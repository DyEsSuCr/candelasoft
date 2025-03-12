import uvicorn
from api.config import APP_HOST, APP_PORT, ENV


if __name__ == '__main__':
    uvicorn.run(
        'api.app:app',
        host=APP_HOST,
        port=APP_PORT,
        reload=ENV == 'dev',
    )
