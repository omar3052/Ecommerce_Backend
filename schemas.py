from pydantic import BaseModel, ConfigDict

# --- ITEM SCHEMAS ---
class ItemBase(BaseModel):
    product_name: str
    quantity: int
class ItemCreate(ItemBase):
    pass
class ItemResponse(ItemBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# --- Order Schemas ---
class OrderBase(BaseModel):
    product_name:str
    price: float
    buyer_email: str

class OrderCreate(OrderBase):
    pass
class OrderResponse(OrderBase):
    model_config = ConfigDict(from_attributes=True)