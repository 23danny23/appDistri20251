from pydantic import BaseModel

class FacturaDto(BaseModel):
    cliente: str
    producto: str
    cantidad: int
    categoria: str
    valor: float
    total: float