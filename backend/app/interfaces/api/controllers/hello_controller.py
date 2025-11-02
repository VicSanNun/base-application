from app.application.use_cases.get_hello_message import GetHelloMessageUseCase
from app.infrastructure.repositories.message_repository_impl import MessageRepositoryImpl
from app.interfaces.schemas.message_schema import MessageSchema

def get_hello_message() -> MessageSchema:
    repo = MessageRepositoryImpl()
    use_case = GetHelloMessageUseCase(repo)
    message = use_case.execute()
    return MessageSchema(text=message.text)
