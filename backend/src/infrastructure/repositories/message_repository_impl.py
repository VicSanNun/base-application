from src.domain.entities.message import Message

class MessageRepositoryImpl:
    def get_message(self) -> Message:
        return Message(text="Hello, World!")
