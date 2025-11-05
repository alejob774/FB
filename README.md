# Capstone Project - Reportes

## Descripción general
**Capstone Project - Reportes** es una aplicación compuesta por un **backend desarrollado con FastAPI** y un **frontend en Node.js (React)** que permite generar, visualizar y administrar reportes de manera dinámica.  
El objetivo del proyecto es integrar un agente de reporte con una interfaz web interactiva para gestionar datos, consultar información y mostrar resultados en tiempo real.

La arquitectura del sistema separa el frontend y el backend para facilitar el desarrollo modular y el despliegue independiente de ambos servicios.

---

## Características principales
- API REST construida con **FastAPI**.
- Servidor de desarrollo ejecutado con **Uvicorn**.
- Frontend en **React / Node.js**, listo para desarrollo local.
- Configuración mediante entorno virtual de Python (`venv`).
- Instrucciones claras para instalación y ejecución de ambos entornos.
- Totalmente adaptable a entornos Windows.

---

## Estructura del proyecto

```
Capstone-Project-Reportes/
├── api/
│   └── inventario-agent-ui/      # Frontend en Node.js / React
│       ├── package.json
│       ├── src/
│       ├── public/
│       └── ...
├── agent.py                      # Punto de entrada del backend (FastAPI)
├── requirements.txt              # Dependencias de Python
├── comandos.txt                  # Notas y comandos de ejecución
└── README.md
```

### Descripción rápida de carpetas
- **api/inventario-agent-ui/** → contiene el frontend (Node/React).  
- **agent.py** → archivo principal que levanta la API con Uvicorn y FastAPI.  
- **requirements.txt** → lista de dependencias del backend.  
- **comandos.txt** → referencia de comandos usados para ejecutar los servicios.  

---

## Requisitos previos

Asegúrate de tener instaladas las siguientes herramientas:

| Herramienta | Versión recomendada |
|--------------|---------------------|
| **Python**   | 3.10 o superior     |
| **Node.js**  | 16 o superior       |
| **npm**      | 8 o superior        |
| **Git**      | Última versión      |

---

## Instalación paso a paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/<tu_usuario>/Capstone-Project-Reportes.git
cd Capstone-Project-Reportes
```

---

### 2. Crear y activar entorno virtual de Python

**Windows (PowerShell o CMD):**
```bash
python -m venv venv
.env\Scriptsctivate
```

**Para desactivar el entorno:**
```bash
deactivate
```

---

### 3. Instalar dependencias del backend

Asegúrate de estar en la raíz del proyecto (donde está `requirements.txt`):

```bash
pip install -r requirements.txt
```

---

### 4. Instalar dependencias del frontend

```bash
cd api/inventario-agent-ui
npm install
```

---

## Ejecución del proyecto

El proyecto se compone de dos partes: el **backend (FastAPI)** y el **frontend (React)**.  
Cada servicio debe iniciarse por separado, **cada uno en su propia terminal**.

---

### 🔹 Iniciar el backend (FastAPI)

Desde la raíz del proyecto, ejecuta:

```bash
uvicorn agent:app --reload --host 0.0.0.0 --port 8000
```

Esto iniciará el servidor en modo desarrollo.

- **Backend activo en:** http://127.0.0.1:8000  
- El parámetro `--reload` permite recargar el servidor automáticamente ante cambios.

Si prefieres usar el puerto por defecto y acceso local únicamente:

```bash
uvicorn agent:app --reload --port 8000
```

---

### 🔹 Iniciar el frontend (React)

En una segunda terminal, dentro del entorno del frontend:

```bash
cd api/inventario-agent-ui
npm run dev -- -p 3000
```

Esto levantará la interfaz de usuario.

- **Frontend activo en:** http://localhost:3000  
- El puerto `3000` puede cambiarse si es necesario (usando la opción `-p`).

---

## Uso

Una vez ambos servicios estén activos:

1. Abre tu navegador y accede a `http://localhost:3000`.
2. Desde la interfaz web podrás:
   - Consultar reportes.
   - Visualizar resultados.
   - Generar nuevas solicitudes hacia la API.
3. El backend responderá desde `http://localhost:8000`.

---

## Variables de entorno

Si el proyecto requiere configuración mediante variables de entorno, crea un archivo `.env` en la raíz con parámetros como:

```
PORT_BACKEND=8000
PORT_FRONTEND=3000
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/mi_basedatos
```

> Asegúrate de no subir el archivo `.env` al repositorio (debe incluirse en `.gitignore`).

---

## Errores comunes y soluciones

| Problema | Posible causa | Solución |
|-----------|----------------|-----------|
| **404 Not Found al acceder al backend** | El servidor Uvicorn no está apuntando al módulo correcto. | Ejecuta `uvicorn agent:app --reload`. |
| **"Port already in use"** | Otro proceso usa el puerto. | Cambia el puerto: `--port 8001` o `-p 3001` en React. |
| **Fallo al instalar dependencias** | Entorno virtual no activado. | Activa `venv` antes de `pip install`. |
| **Frontend no se comunica con backend** | CORS no configurado en FastAPI. | Agrega middleware CORS en `agent.py`. |

---

## Contribución

Si deseas contribuir al proyecto:

1. Haz un **fork** del repositorio.
2. Crea una nueva rama para tu cambio:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz commit:
   ```bash
   git commit -m "Agrega nueva funcionalidad"
   ```
4. Envía un **Pull Request** con una descripción clara del cambio.

---

## Licencia

Este proyecto se distribuye bajo la licencia **MIT**.

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## Autor

Desarrollado como parte del **Capstone Project - Reportes**.  
© 2025. Todos los derechos reservados.

---

## Resumen rápido de comandos

```bash
# Clonar repositorio
git clone https://github.com/<tu_usuario>/Capstone-Project-Reportes.git
cd Capstone-Project-Reportes

# Crear entorno virtual
python -m venv venv
.env\Scriptsctivate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar backend
uvicorn agent:app --reload --port 8000

# Ejecutar frontend
cd api/inventario-agent-ui
npm install
npm run dev -- -p 3000
```

---

## Estado del proyecto
El proyecto se encuentra en fase de desarrollo activo, con integración funcional entre el backend y el frontend para pruebas locales.
