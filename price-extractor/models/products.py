from database import Base
from typing import Optional
from sqlalchemy import DateTime, func, String
from sqlalchemy.orm import Mapped, mapped_column, Session
from datetime import datetime, timezone




class Product(Base):

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(index=True, primary_key=True, unique=True)
    canonical_url: Mapped[str] = mapped_column(unique=True, nullable=False)
    name: Mapped[str]
    description: Mapped[str]
    main_image_url: Mapped[str]
    availability: Mapped[bool] = mapped_column(nullable=False)
    rating_value: Mapped[float] 
    rating_count: Mapped[int]
    seller_name: Mapped[str]
    category: Mapped[str] = mapped_column(String(50))
    color: Mapped[str] = mapped_column(String(100))
    brand: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(
                                   DateTime(timezone=True),
                                   server_default=func.now())
    last_updated_at: Mapped[Optional[datetime]] = mapped_column(
                                                  DateTime(timezone=True),
                                                  onupdate=func.now())