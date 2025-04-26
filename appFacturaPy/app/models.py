from sqlalchemy import Column, Integer, String, Numeric
from .database import Base

class Factura(Base):
    __tablename__ = "factura"

    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String)
    producto = Column(String)
    cantidad = Column(Integer)
    categoria = Column(String)
    valor = Column(Numeric(10, 2))
    total = Column(Numeric(10, 2))