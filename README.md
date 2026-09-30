# Proyecto ComercioConecta API

## Pasos para ejecutar el proyecto localmente

**1. Clonar el repositorio y entrar a la carpeta**
\`\`\`bash
git clone <URL_DEL_REPOSITORIO>
cd comercio_conecta
\`\`\`

**2. Crear y activar el entorno virtual**
\`\`\`bash
# Crear entorno
python -m venv venv

# Activar en Windows:
.\venv\Scripts\activate
# Activar en Mac/Linux:
source venv/bin/activate
\`\`\`

**3. Instalar las dependencias**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

**4. Crear la base de datos local**
\`\`\`bash
python manage.py migrate
\`\`\`

**5. Ejecutar el servidor**
\`\`\`bash
python manage.py runserver
\`\`\`

**6. Probar la API**
Abre tu navegador en: `http://127.0.0.1:8000/api/docs/` para ver la interfaz de Swagger y probar los endpoints.