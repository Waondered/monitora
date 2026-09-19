from database import Base
from typing import Optional, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, DateTime, func
from datetime import datetime

if TYPE_CHECKING:
    from .products import Product

class MonitoringQueue(Base):

    __tablename__ = "monitoring_queue"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    status: Mapped[str] = mapped_column(String(50))
    last_checked_at: Mapped [Optional[datetime]] = mapped_column(
                                                   DateTime(timezone=True),
                                                   onupdate=func.now())
    next_check_at: Mapped[Optional[datetime]] = mapped_column(
                                                DateTime(timezone=True),
                                                onupdate=func.now())
    created_at: Mapped[datetime] = mapped_column(
                                       DateTime(timezone=True),
                                       server_default=func.now())
    product: Mapped["Product"] = relationship(back_populates="monitoring_queue")