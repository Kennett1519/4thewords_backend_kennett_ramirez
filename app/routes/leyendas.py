from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form
from sqlmodel import Session
from app.database import get_session
from app.models.leyenda import Leyenda
from datetime import datetime
from app.services.leyendas_service import (
    obtener_todas_las_leyendas,
    obtener_leyenda_por_id,
    crear_leyenda,
    actualizar_leyenda,
    eliminar_leyenda
)
import shutil
import os
import uuid
from typing import List

router = APIRouter(prefix="/leyendas", tags=["leyendas"])

#Crear la ruta uploads para almacenar las imagenes
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

#Recibir imagen, guardarla en la ruta y devolver la URL
@router.post("/subir-imagen/")
async def subir_imagen(imagen: UploadFile = File(...)):
    try:
        #Generar nombre unico para la imagen
        file_extension = os.path.splitext(imagen.filename)[1]
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        file_path = os.path.join(UPLOAD_DIR, unique_filename)

        #Guardar imagen en la carpeta
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(imagen.file, buffer)

        #Devolver la URL para uso en el front
        return {"imagen_url": f"/static/{unique_filename}"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al subir la imagen: {str(e)}")


#Recibir los datos de la leyenda como JSON y guarda en la BD
@router.post("/", response_model=Leyenda)
def crear_leyenda_endpoint(
    leyenda_data: Leyenda, 
    session: Session = Depends(get_session)
):
    try:
        #Verificar que la URL de imagen no esté vacía
        if not leyenda_data.imagen_url:
            raise HTTPException(status_code=400, detail="Debe proporcionar una URL de imagen válida.")

        #Guardar leyenda en la BD
        return crear_leyenda(session, leyenda_data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear la leyenda: {str(e)}")

#Listar las leyendas
@router.get("/", response_model=List[Leyenda])
def listar_leyendas_endpoint(session: Session = Depends(get_session)):
    return obtener_todas_las_leyendas(session)

#Mostrar leyenda por id
@router.get("/{leyenda_id}", response_model=Leyenda)
def obtener_leyenda_endpoint(leyenda_id: int, session: Session = Depends(get_session)):
    return obtener_leyenda_por_id(session, leyenda_id)

#Actualizar leyenda por id:
@router.put("/{leyenda_id}", response_model=Leyenda)
def actualizar_leyenda_endpoint(
    leyenda_id: int, 
    leyenda_data: Leyenda, 
    session: Session = Depends(get_session)
):
    try:
        return actualizar_leyenda(session, leyenda_id, leyenda_data)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar la leyenda: {str(e)}")

@router.delete("/{leyenda_id}")
def eliminar_leyenda_endpoint(leyenda_id: int, session: Session = Depends(get_session)):
    return eliminar_leyenda(session, leyenda_id)

