from pydantic import BaseModel


class ApplicationCreate(BaseModel): 
    cv_file: str
    surname: str
    second_name: str
    first_name: str
    login_telegram: str


class ApplicationBase(BaseModel):
    pass