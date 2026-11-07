from sqlalchemy import Integer,Float,String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
class ManageItems(Base):
    __tablename__ = "Manage_Items"
    id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    quantity: Mapped[int] = mapped_column(Integer, nullable = False)
    product_name: Mapped[str]= mapped_column(String, nullable = False)
class Placing_Order(Base):
    __tablename__ = "Placing_Order"
    id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    price: Mapped[float] = mapped_column(Float, nullable = False)
    product_name: Mapped[str] = mapped_column(String, nullable = False)
    buyer_email: Mapped[str] = mapped_column(String, nullable = False )
    