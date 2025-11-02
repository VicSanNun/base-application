from fastapi import APIRouter
from src.presentation.api.controllers.hello_controller import get_hello_message

router = APIRouter(prefix="/hello", tags=["Hello"])

@router.get("/", response_model=dict)
def hello():
    message = get_hello_message()
    return {"message": message.text}
