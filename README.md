## 🚀 **Cómo iniciar la aplicación DOCKER**

### **Requisitos previos**
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)


### **1. Clonar el repositorio**
```bash
git clone https://github.com/DyEsSuCr/candelasoft.git
cd candelasoft-api
```

### **2. Configurar variables de entorno**
Crea un archivo .env.docker en la raíz del proyecto con las siguientes variables:

```bash
# Entorno
ENV=dev

# App
APP_PORT=8000
APP_NAME='Api CandelaSoft'
APP_DESCRIPTION='API CandelaSoft'
APP_HOST=0.0.0.0

# PostgreSQL
DB_HOST=db
DB_PORT=5432
DB_DATABASE=candelasoft
DB_USERNAME=postgres
DB_PASSWORD=awds

# CORS
ALLOWED_ORIGINS='http://localhost:3000'

# API Externa
EXTERNAL_API_URL='https://jsonplaceholder.typicode.com'
```


### **3. Construir y ejecutar con Docker**

```bash
docker compose --env-file .env.docker build
docker compose --env-file .env.docker up -d
```


### **4. Acceder a la API**
```bash
http://localhost:8000/
```

## 🛠 **Endpoints principales**
```http
http://localhost:8000/api/v1/users
http://localhost:8000/api/v1/countries
```
Parámetros:
   - page (opcional): Número de página (por defecto: 1).
   - limit (opcional): Cantidad de registros por página (por defecto: 5, máximo: 100).

#### Respuestas

 users
```json
{
  "data": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      ...
    },
    ...
  ],
  "pagination": {
    "total_count": 100,
    "limit": 10,
    "offset": 10,
    "total_pages": 10,
    "current_page": 2
  }
}
```

countries
```json
{
  "data": [
    {
      "id": 1,
      "name": "Argentina",
      "code": "AR",
      ...
    },
    ...
  ],
  "pagination": {
    "total_count": 50,
    "limit": 20,
    "offset": 0,
    "total_pages": 3,
    "current_page": 1
  }
}
```

```http
http://localhost:8000/api/v1/users/{user_id}
```
Parámetros:
   - user_id (requerido): ID del usuario.

#### Respuesta
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "country": {
    "id": 1,
    "name": "Argentina",
    "code": "AR"
  },
  ...
}
```

### **Detener y eliminar contenedores**
```bash
docker-compose down -v
```


### 🛠 **Tecnologías y herramientas utilizadas**

| **Categoría** | **Herramienta** | **Descripción** |
|---------------|-----------------|-----------------|
| **Lenguaje** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Lenguaje de programación principal. |
| **Framework** | ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)  | Framework para construir APIs rápidas y modernas. |
| **ORM** | ![SQLModel](https://img.shields.io/badge/SQLModel-000000?style=flat)            | ORM para interactuar con la base de datos PostgreSQL. |
| **Base de datos** | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white) | Sistema de gestión de bases de datos relacional. |
| **Contenedores** | ![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=flat&logo=docker&logoColor=white) | Plataforma para empaquetar y ejecutar aplicaciones en contenedores. |
| **Control de versiones** | ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white) | Sistema de control de versiones distribuido. |
| **API Externa** | ![JSONPlaceholder](https://img.shields.io/badge/JSONPlaceholder-000000?style=flat) | API de prueba para simular datos externos.eventos.                             |
| **Documentación** | ![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=flat&logo=swagger&logoColor=black) | Interfaz interactiva para explorar y probar la API. |


# Explicación de la API Externa

Este código utiliza una API externa para obtener información adicional sobre las tareas (todos) de un usuario específico. Veamos cómo funciona:

1. La función `get_by_id` primero busca al usuario por su ID en la base de datos local.
2. Luego hace una solicitud asíncrona a una API externa usando `httpx` para obtener las tareas asociadas a ese usuario.
3. La URL de la solicitud es `{EXTERNAL_API_URL}/todos?userId={user_id}`, lo que indica que está consultando el endpoint "todos" de la API externa, filtrando por el ID del usuario.
4. Si encuentra que alguna tarea está marcada como completada (`external_data[0]['completed']`), genera una notificación por correo electrónico.
5. Finalmente, retorna un objeto con los datos del usuario, los datos obtenidos de la API externa y, si corresponde, la notificación por correo.
