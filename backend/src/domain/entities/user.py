"""User domain entity."""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

@dataclass
class User:
    """User domain entity representing a user in the system."""

    id: UUID
    email: str
    password_hash: str
    full_name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime