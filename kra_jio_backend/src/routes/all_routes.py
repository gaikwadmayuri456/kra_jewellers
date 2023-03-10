from fastapi import APIRouter
from ..routes.goldrates import router as goldrates


router = APIRouter()

router.include_router(goldrates)

