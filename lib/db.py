from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str


USERS: list[User] = []
DEFAULT_USER = User(email="",password="")

def set_user(email, password):
    USERS.append(User(email=email, password=password))


def get_user(email:str):
    print(email, USERS)
    return next(filter(lambda x: x.email == email, USERS), DEFAULT_USER)

def get_check_valid_password(email:str, password:str):
    return get_user(email).password==password
