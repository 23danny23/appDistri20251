from sqlalchemy.orm import Session
from . import models, schemas

def get_facturas(db: Session):
    """Obtiene todas las facturas (equivalente a SELECT * FROM factura)"""
    return db.query(models.Factura).all()


def create_factura(db: Session, factura: schemas.FacturaDto):
    """Crea una nueva factura"""
    db_factura = models.Factura(
        cliente=factura.cliente,
        producto=factura.producto,
        cantidad=factura.cantidad,
        categoria=factura.categoria,
        valor=factura.valor,
        total=factura.total
    )
    db.add(db_factura)
    db.commit()
    db.refresh(db_factura)
    return db_factura