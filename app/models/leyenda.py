from sqlmodel import SQLModel, Field
from datetime import date

class Leyenda(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, nullable=False)
    categoria: str = Field(nullable=False)
    descripcion: str = Field(nullable=False)
    fecha: date = Field(nullable=False)
    provincia: str = Field(nullable=False)
    canton: str = Field(nullable=False)
    distrito: str = Field(nullable=False)
    imagen_url: str = Field(nullable=False)

