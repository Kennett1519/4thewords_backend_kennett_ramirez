from sqlmodel import Session, select
from app.models.leyenda import Leyenda
from fastapi import HTTPException
from typing import List

def obtener_todas_las_leyendas(session: Session) -> List[Leyenda]:
  return session.scalars(select(Leyenda)).all()

def obtener_leyenda_por_id(session: Session, Leyenda_id: int) -> Leyenda:
  leyenda = session.get(Leyenda, leyenda_id)
  if not leyenda:
    raise HTTPException(status_code=404, detail="Leyenda no encontrada")
  return leyenda

def crear_leyenda(session: Session, Leyenda: Leyenda) -> Leyenda:
  session.add(leyenda)
  session.commit()
  session.refresh(leyenda)
  return leyenda


def actualizar_leyenda(session: Session, leyenda_id: int, leyenda_data: Leyenda) -> Leyenda:
  leyenda = session.get(Leyenda, leyenda_id)
  if not leyenda:
    raise HTTPException(status_code=404, detail="Leyenda no encontrada")
  
  leyenda_data_dict = leyenda_data.dict(exclude_unset=True)
  if "id" in leyenda_data_dict:
    leyenda_data_dict.pop("id")  # Evitar actualización del ID
  
  for key, value in leyenda_data_dict.items():
    setattr(leyenda, key, value)
  
  session.add(leyenda)
  session.commit()
  session.refresh(leyenda)
  return leyenda

def eliminar_leyenda(session: Session, Leyenda_id: int):
  leyenda = session.get(Leyenda, Leyenda_id)
  if not leyenda:
    raise HTTPException(status_code=404, detail="Leyenda no encontrada")
  
  session.delete(leyenda)
  session.commit()
  return {"message": "Leyenda eliminada con éxito"}

