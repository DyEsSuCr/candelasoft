from fastapi import APIRouter

from api.modules.countries import routes as countries
from api.modules.users import routes as users


router = APIRouter(prefix='/api/v1')

router.include_router(
    users.router,
    prefix='/users',
    tags=['Users'],
)

router.include_router(
    countries.router,
    prefix='/countries',
    tags=['Countries'],
)
