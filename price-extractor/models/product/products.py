from database import Base
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import DateTime, func, String, DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, Session, relationship
from datetime import datetime, timezone


class Product(Base):

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(index=True, primary_key=True, unique=True)
    canonical_url: Mapped[str] = mapped_column(unique=True, nullable=False)
    name: Mapped[str]
    description: Mapped[Optional[str]]
    main_image_url: Mapped[str]
    images: Mapped[List["ProductImage"]] = relationship(back_populates="product",
                                                        cascade="all, delete-orphan")
    prices: Mapped[List["ProductPrice"]] = relationship(back_populates="product",
                                                        cascade="all, delete-orphan")
    availability: Mapped[bool] = mapped_column(nullable=False)
    rating_value: Mapped[float] 
    rating_count: Mapped[int]
    seller_name: Mapped[Optional[str]]
    category: Mapped[str] = mapped_column(String(50))
    color: Mapped[str] = mapped_column(String(100))
    brand: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(
                                   DateTime(timezone=True),
                                   server_default=func.now())
    last_updated_at: Mapped[Optional[datetime]] = mapped_column(
                                                  DateTime(timezone=True),
                                                  onupdate=func.now())



class ProductImage(Base):

    __tablename__ = "products_images"

    id: Mapped[int] = mapped_column(index=True, primary_key=True, unique=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped["Product"] = relationship(back_populates="images")
    image_url: Mapped[str] = mapped_column(String(255), unique=True)
    created_at: Mapped[datetime] = mapped_column(
                                   DateTime(timezone=True),
                                   server_default=func.now())



class ProductPrice(Base):

    __tablename__ = "products_prices"
     
    id: Mapped[int] = mapped_column(index=True, primary_key=True, unique=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped["Product"] = relationship(back_populates="prices")
    price: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)
    effective_date: Mapped[datetime] = mapped_column(
                                       DateTime(timezone=True),
                                       server_default=func.now())
    