from fastapi import FastAPI
from fetcher import request
from database import Session, Base, engine
from models.products import Product
import sqlalchemy

Base.metadata.create_all(engine)
product = Product(
    canonical_url="canonical_url",
    name="Abajur",
    description="descricao",
    main_image_url="main_image_url",
    availability=True,
    rating_value= 4.58,
    rating_count=10,
    seller_name="Kabum",
    category="eletrônicos",
    color="branco",
    brand="Kabum",
 )

with Session() as session:
    session.add(product)
    session.commit()
    print(session.query(Product).all())
