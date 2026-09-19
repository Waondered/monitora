from database import Base
from models.monitoring_queue import MonitoringQueue
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import DateTime, func, String, DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

if TYPE_CHECKING:
    from .monitoring_queue import MonitoringQueue


class Product(Base):

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(index=True, primary_key=True, unique=True)
    canonical_url: Mapped[str] = mapped_column(unique=True, nullable=False)
    name: Mapped[str]
    description: Mapped[Optional[str]]
    main_image_url: Mapped[str]
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

    # ------ One-to-Many relationships ------
    images: Mapped[List["ProductImage"]] = relationship(back_populates="product",
                                                            cascade="all, delete-orphan")
    prices: Mapped[List["ProductPrice"]] = relationship(back_populates="product",
                                                            cascade="all, delete-orphan")

    # ------ One-to-One relationship ------
    monitoring_queue: Mapped["MonitoringQueue"] = relationship(back_populates="product",
                                                                   cascade="all, delete-orphan")



class ProductImage(Base):

    __tablename__ = "products_images"

    id: Mapped[int] = mapped_column(index=True, primary_key=True, unique=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    image_url: Mapped[str] = mapped_column(String(255), unique=True)
    created_at: Mapped[datetime] = mapped_column(
                                   DateTime(timezone=True),
                                   server_default=func.now())
    product: Mapped["Product"] = relationship(back_populates="images")



class ProductPrice(Base):

    __tablename__ = "products_prices"
     
    id: Mapped[int] = mapped_column(index=True, primary_key=True, unique=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    price: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)
    effective_date: Mapped[datetime] = mapped_column(
                                       DateTime(timezone=True),
                                       server_default=func.now())
    product: Mapped["Product"] = relationship(back_populates="prices")
    