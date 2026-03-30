from pydantic import BaseModel, Field


class Market(BaseModel):
    id: int
    name: str


class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description='Цена должна быть больше нуля')  # gt - больше чем ноль
    tags: list[str] = []
    market: Market


product_data = {
    'name': 'Phone',
    'price': 123,
    'tags': ['Apple', 'Google'],
    'market': {
        'id': 1,
        'name': 'Amazon'
    }
}

product = Product(**product_data)
print(product.market)

new_product = Product(
    name='Phone',
    price=123,
    tags=['Apple', 'Google'],
    market=Market(id=1, name='Amazon')
)
print('new_product', new_product)