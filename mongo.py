#import motor.motor_asyncio
from typing import  List,Optional
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

from beanie import Document, Indexed, init_beanie

class Bar(BaseModel):
    apple: str = 'x'
    banana: str = 'y'

class Foo(BaseModel):
    count: int
    size: Optional[float] = None

class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]

class Category(BaseModel):
    name: str
    description: str


class Product(Document):
    name: str                        # You can use normal types just like in pydantic
    description: Optional[str] = None
    price: Indexed(float)              # You can also specify that a field should correspond to an index
    category: Category 
    arrau:Spam 
    a:list         # You can include pydantic models as well


# This is an asynchronous example, so we will access it from an async function
async def example():
    # Beanie uses Motor async client under the hood 
    client = AsyncIOMotorClient("mongodb://localhost:27017")

    # Initialize beanie with the Product document class
    await init_beanie(database=client.db_name, document_models=[Product])
   
    chocolate = Category(name="Chocolate", description="A preparation of roasted and ground cacao seeds.")
    m = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
    # Beanie documents work just like pydantic models
    tonybar = Product(name="Tony's", price=5.95, category=chocolate, arrau=m,a=[1,2,3])
    # And can be inserted into the database
    await tonybar.insert() 

    # You can find documents with pythonic syntax
    #product = await Product.find_one(Product.price < 10)

    # And update them
    #await product.set({Product.name:"Gold bar"})


