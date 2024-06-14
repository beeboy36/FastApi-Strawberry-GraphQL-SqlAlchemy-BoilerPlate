from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from pydantic.typing import Optional
from . import Base, User

class StickyNotes(Base):
    __tablename__ = "stickynotes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    text: Mapped[str] = mapped_column(String, nullable=True)
    created_datetime: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey(User.id, ondelete='CASCADE'), nullable=True)

    def as_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "created_datetime": self.created_datetime,
            "user_id": self.user_id
        }