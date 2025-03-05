import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_db
from fastapi.staticfiles import StaticFiles

#Inicializamos la base de datos
init_db()

app = FastApi()
app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:3000"], #URL del frontend para permitir la comunicación entre front y back
  allow_credentials=True,
  allow_methods=["*"], #Permite los métodos GET, POST, PUT, DELETE
  allow_headers=["*"],
)
