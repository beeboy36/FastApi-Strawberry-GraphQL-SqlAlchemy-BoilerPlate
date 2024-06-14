from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped
from . import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    stickynotes = relationship("StickyNotes", cascade="all, delete", passive_deletes=True)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }