from src.domain.entities.message import Message

class GetHelloMessageUseCase:
    def __init__(self, message_repository):
        self._repo = message_repository

    def execute(self) -> Message:
        return self._repo.get_message()
