from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


user_date = {
    'id': 1,
    'username': 'john',
    'email': 'john@ya.ru'}

user = User(**user_date)
print(user)
print(user.is_active)

invalid_user_date = {
    'id': 1,
    'username': 'john',
    'email': 'john@ya.ru'}

invalid_user = User(**invalid_user_date)