from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Facturación",
    openapi_prefix="/api/factura",
    description="API para gestión de facturas con PostgreSQL",
    version="1.0.0"
)


# Endpoint GET para obtener todas las facturas (SELECT *)
@app.get("/obtenerFactura/", tags=["Facturas"], response_model=list[schemas.FacturaDto])
def obtener_facturas(db: Session = Depends(get_db)):
    """Obtiene todas las facturas de la base de datos"""
    return crud.get_facturas(db)

# Endpoint POST para crear nueva factura
@app.post("/insertarFactura/", tags=["Facturas"],response_model=schemas.FacturaDto)
def crear_factura(factura: schemas.FacturaDto, db: Session = Depends(get_db)):
    """Crea una nueva factura en la base de datos"""
    return crud.create_factura(db=db, factura=factura)