import uuid
import sqlalchemy as sa

from internal.entity.base import Base


class Application(Base):

    __tablename__ = 'applications'
    id = sa.Column(sa.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = sa.Column(sa.String(50), nullable=False)
    first_name = sa.Column(sa.String(50), nullable=False)  # имя
    second_name = sa.Column(sa.String(50), nullable=False)  # фамилия
    surname = sa.Column(sa.String(50), nullable=False)  # отчество
    cv_file = sa.Column(sa.String(50), nullable=False)
    login_telegram = sa.Column(sa.String(50), nullable=False, unique=True)

    comment = sa.Column(sa.Text, nullable=True, default="")

    def __repr__(self):
        return f'<Book {self.title}>'


class Vacancy(Base):
    id = sa.Column(sa.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = sa.Column(sa.String(255), index=True, nullable=False)
    gross = sa.Column(sa.Integer, index=True, nullable=True)
    description = sa.Column(sa.Text, nullable=False)
