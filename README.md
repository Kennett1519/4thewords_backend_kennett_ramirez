# Prueba Fullstack Junior Backend Python FastAPI - 4thewords Kennett Ramirez

Este proyecto es una API construida con Python FastAPI para gestionar un libro virtual de leyendas costarricenses.

### Requisitos previos
- Python 3.13.2
- MySQL (Manejado con MySQL Workbench)
- Virtualenv (Opcional, pero altamente recomendado)

### Configuración
1. Clonar el repositorio:
   git clone https://github.com/Kennett1519/4thewords_backend_kennett_ramirez.git
   cd 4thewords_backend_kennett_ramirez

2. Crear un entorno virtual e instalar librerías:
   python -m venv .venv
   source .venv/Scripts/activate
   pip install -r requirements.txt

3. Configurar la base de datos MySQL:
   Ejecutar el código dentro del archivo script.sql
   Luego, editar DATABASE_URL dentro de database.py para colocar las credenciales de MySQL.
   Luego abrir MySQL Workbench para conectarse a la instancia y base de datos para tener una correcta ejecución del backend.

4. Iniciar el servidor:
   uvicorn app.main:app --host 127.0.0.1 --port 8080 --reload

6. Acceder a la documentación de la API en:
   - http://localhost:8080/docs
