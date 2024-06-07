from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text
from app.database import Base


class Flyer(Base):
    __tablename__ = "Flyers"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    released = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
