# 🎯 Pokémon TCG - Fullstack App

Este proyecto es una aplicación Fullstack que consume una base de datos con información de los sets y cartas del juego Pokémon TCG. La aplicación incluye un backend en Flask con una API REST documentada con **flask-swagger-ui** y un frontend en Vue 3 con TypeScript y Tailwind CSS.

## 🛠️ Tecnologías Utilizadas

### **Backend**

- Python
- Flask
- Flask-SQLAlchemy
- PostgreSQL
- Flask-Swagger-UI
- Docker / Docker Compose
- Render (para despliegue)

### **Frontend**

- Vue 3
- Vite
- TypeScript
- Tailwind CSS
- Netlify (para despliegue)

## 🌐 Despliegue

- **Frontend**: [Enlace a Netlify](https://pokemon-tcg-ajav06.netlify.app)
- **Backend**: [Enlace a Render](https://lab-prueba-fullstack-qnrn.onrender.com/swagger)

## 🛡️ Instalación y Uso

### 1. Ejecutar con Docker Compose

```sh
docker-compose up --build
```

Esto iniciará el backend, frontend y la base de datos PostgreSQL.

### 2. Acceder a la Aplicación

- Frontend: [http://localhost:8085](http://localhost:8085)
- Backend (Swagger UI): [http://localhost:8181/swagger](http://localhost:8181/swagger)

## 📝 Documentación de la API

La API está documentada con **Swagger** y es accesible en: [http://localhost:8181/swagger](http://localhost:8181/swagger)

### **Endpoints Disponibles**

#### **Sets**

- `GET /sets` - Obtiene todos los sets
- `GET /sets/{id}` - Obtiene un set por ID
- `GET /sets/{id}/cards` - Obtiene cartas por Set

#### **Cartas**

- `GET /cards` - Obtiene todas las cartas
- `GET /cards/{id}` - Obtiene una carta por ID

## 📖 Estructura del Proyecto

```
/
├── backend/
│   ├── app/
│   │   ├── cards/
│   │   │   ├── models.py   # Modelos SQLAlchemy
│   │   │   ├── repository.py   # Repositorios para acceso a datos
│   │   │   ├── views.py   # Rutas y vistas de la API
│   │   ├── sets/
│   │   │   ├── models.py   # Modelos SQLAlchemy
│   │   │   ├── repository.py   # Repositorios para acceso a datos
│   │   │   ├── views.py   # Rutas y vistas de la API
│   │   ├── static/
│   │   │   ├── swagger.json   # Modelos Swagger
│   ├── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   ├── vite.config.ts
├── Dockerfile.frontend
├── Dockerfile.backend
├── docker-compose.yml
├── README.md
```
