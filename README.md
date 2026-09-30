# 🛒 ComercioConecta API

## 📖 Contexto del Proyecto

ComercioConecta es una pyme que agrupa tiendas de barrio. Este proyecto es el *backend* (API REST) de un sistema diseñado para entender las relaciones entre los productos que los clientes compran juntos frecuentemente. 

En lugar de basarse en la intuición o en complejos modelos de Inteligencia Artificial, este sistema utiliza **Teoría de Grafos**. Los productos actúan como "nodos" y las compras conjuntas como "aristas" (conexiones no dirigidas). El peso de cada conexión representa la cantidad de veces que dos productos se han comprado juntos. Esto permitirá a los encargados de ventas descubrir redes de productos y armar propuestas comerciales justificables.

## ✨ Características (Features)

- ✅ **Feature 1 - Red comercial inicial:** Registro de productos y relaciones de compra conjunta. Validaciones estrictas para evitar relaciones duplicadas, productos inexistentes y control de autorelaciones.
- 🚧 **Feature 2 - Exploración de relaciones:** *(En desarrollo)* Algoritmo de búsqueda para encontrar productos conectados a partir de un nodo inicial.
- 🚧 **Feature 3 - Propuesta comercial:** *(Próximamente)* Sistema de recomendación basado en el peso y alcance de las conexiones.

## 🛠️ Tecnologías

- **Lenguaje:** Python 3.x
- **Framework:** Django & Django REST Framework (DRF)
- **Documentación API:** Swagger UI (vía `drf-spectacular`)
- **Base de Datos Local:** SQLite3 (Excluida del repositorio por control de versiones)

---

## 🚀 Guía de Instalación Local (Para el equipo de desarrollo)

Sigue estos pasos en tu terminal para levantar el proyecto en tu máquina local. Es indispensable tener Git y Python instalados.

### 1. Clonar el repositorio
Descarga el código fuente a tu computadora y entra en la carpeta del proyecto.

`git clone https://github.com/angel20555/comercio_conecta.git`
`cd comercio_conecta`

### 2. Crear el entorno virtual
Aislamos las dependencias del proyecto para no interferir con las librerías globales de tu computadora.

`python -m venv venv`

### 3. Activar el entorno virtual
Dependiendo de tu sistema operativo, ejecuta el comando correspondiente. *(Deberías ver un `(venv)` al inicio de tu línea de comandos).*

**En Windows:**
`.\venv\Scripts\activate`

**En Mac / Linux:**
`source venv/bin/activate`

### 4. Instalar las dependencias
Instala exactamente las mismas versiones de Django y DRF que está usando el equipo.

`pip install -r requirements.txt`

### 5. Configurar la base de datos local
Como la base de datos `db.sqlite3` está ignorada en Git, debes crear tu propia base de datos local y construir las tablas a partir de los modelos.

`python manage.py migrate`

### 6. Levantar el servidor
Enciende la API localmente.

`python manage.py runserver`

---

## 🧪 Pruebas y Uso (Swagger)

Una vez que el servidor esté corriendo, no necesitas herramientas externas como Postman. La API incluye una interfaz gráfica interactiva.

1. Abre tu navegador y dirígete a: **http://127.0.0.1:8000/api/docs/**
2. Expande el endpoint `POST /api/products/` para crear algunos productos de prueba (ej. "Pan", "Huevos").
3. Expande el endpoint `POST /api/relationships/` usando los IDs de los productos que acabas de crear para conectarlos y simular una compra conjunta.
