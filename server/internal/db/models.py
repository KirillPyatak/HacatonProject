import uuid
from internal.utils.base import Base
from sqlalchemy import (
    JSON,
    UUID,
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
)

role = Table(
    "role",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)


class User(Base):
    __tablename__ = "users"
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(50), nullable=False, unique=True)
    hashed_password: str = Column(String(length=1024), nullable=False)
    city = Column(String(50), nullable=False)
    role_id = Column(Integer, ForeignKey(role.c.id))
    rating = Column(Integer, default=0)
    telegram_id = Column(Integer, nullable=True, unique=True)


class Application(Base):
    __tablename__ = "applications"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)  # имя
    second_name = Column(String(50), nullable=False)  # фамилия
    surname = Column(String(50), nullable=False)  # отчество
    cv_file = Column(String(50), nullable=False)
    login_telegram = Column(String(50), nullable=False, unique=True)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    comment = Column(Text, nullable=True, default="")


class Vacancy(Base):
    __tablename__ = "vacancy"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    gross = Column(Integer, nullable=True)
