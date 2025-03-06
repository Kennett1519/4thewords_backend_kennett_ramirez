from sqlmodel import SQLModel, create_engine, Session
from app.models.leyenda import Leyenda

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/4thewords_prueba_kennett_ramirez"
engine = create_engine(DATABASE_URL, echo=True)

#Inicializar la base de datos (crear las respectivas tablas)
def init_db():
    SQLModel.metadata.create_all(engine)

#Obtener una sesión de la base de datos
def get_session():
    with Session(engine) as session:
        yield session
