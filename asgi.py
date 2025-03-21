import uvicorn
from api.config import settings


if __name__ == '__main__':
    uvicorn.run(
        'api.app:app',
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.ENV == 'dev',
    )
