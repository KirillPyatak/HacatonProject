from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from internal.db import settings
from internal.db.database import current_session
from internal.entity.application import Application,Vacancy


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(settings)

    admin = Admin(
        app=app,
        url='/',
        name=settings.NAME,
        template_mode='bootstrap4',
    )
    admin.add_view(ModelView(Application, current_session))
    admin.add_view(ModelView(Vacancy, current_session))

    return app