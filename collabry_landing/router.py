import fastapi

from . import handlers


router = fastapi.APIRouter()


router.add_api_route(
    path="/email", methods=["POST"],
    endpoint=handlers.post_email,
)
