from internal.api import api_router
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from internal.db import settings
from sqlalchemy.exc import DBAPIError, NoResultFound
import os
import sys

from fastapi import FastAPI
from fastapi.logger import logger
from fastapi.responses import HTMLResponse
from internal.db import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.NAME,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
        terms_of_service="http://www.fastapi.org",
        license_info=dict(
            name="Apache 2.0",
            url="https://www.apache.org/licenses/LICENSE-2.0.html"
        ),
        openapi_url="{0}/openapi.json".format(settings.DOCS),
        swagger_ui_parameters=settings.SWAGGER_UI_PARAMETERS,
    )

    # def init_webhooks(base_url):
    #     # Update inbound traffic via APIs to use the public-facing ngrok URL
    #     pass

    # if settings.USE_NGROK:
    #     # pyngrok should only ever be installed or initialized in a dev environment when this flag is set
    #     from pyngrok import ngrok

    #     # Get the dev server port (defaults to 8000 for Uvicorn, can be overridden with `--port`
    #     # when starting the server
    #     port = sys.argv[sys.argv.index(
    #         "--port") + 1] if "--port" in sys.argv else 8000

    #     # Open a ngrok tunnel to the dev server
    #     public_url = ngrok.connect(port).public_url
    #     logger.info(
    #         "ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

    #     # Update any base URLs or webhooks to use the public ngrok URL
    #     settings.BASE_URL = public_url
    #     init_webhooks(public_url)

# ... Initialize routers and the rest of our app
    from fastapi.templating import Jinja2Templates
    templates = Jinja2Templates(directory="templates")


    @app.get("/")
    async def read_item(request: Request):
        context = {"request": request}
        return templates.TemplateResponse("item.html", context)

    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin)
                           for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    app.include_router(api_router, prefix=settings.API)

    return app
