# Home About Project

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

## 📖 Descripción

Este proyecto es una aplicación web simple construida con **Django**, que incluye páginas de inicio (home) y acerca de (about). Está diseñado para demostrar la estructura básica de un proyecto Django con vistas, plantillas y modelos. El proyecto utiliza SQLite como base de datos por defecto y está configurado para desarrollo local.

### ✨ Características

- 🏠 Página de inicio personalizable
- ℹ️ Página "Acerca de" con información del proyecto
- 📱 Diseño responsivo con plantillas HTML
- 🔧 Configuración modular con apps Django
- 🗄️ Base de datos SQLite integrada
- 🚀 Servidor de desarrollo fácil de ejecutar

## 🛠️ Instalación

### Prerrequisitos

- Python 3.8 o superior
- Git (opcional, para clonar el repositorio)

### Pasos de Instalación

1. **Clona el repositorio** (si aplica):
   ```bash
   git clone https://github.com/tu-usuario/home-about.git
   cd home-about
   ```

2. **Crea un entorno virtual**:
   ```bash
   python -m venv .venv
   ```

3. **Activa el entorno virtual**:
   - En Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Realiza las migraciones de la base de datos**:
   ```bash
   python manage.py migrate
   ```

6. **Ejecuta el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

7. **Accede a la aplicación**:
   - Abre tu navegador y ve a: `http://127.0.0.1:8000/`

## 📁 Estructura del Proyecto

```
home_about/
├── db.sqlite3                 # Base de datos SQLite
├── manage.py                  # Script de gestión de Django
├── requirements.txt           # Dependencias del proyecto
├── base_project/              # Configuración principal del proyecto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── pages/                     # App principal con vistas y modelos
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       └── __init__.py
└── templates/                 # Plantillas HTML
    ├── _base.html
    ├── about.html
    └── home.html
```

## 🚀 Uso

### Ejecutar el Servidor

```bash
python manage.py runserver
```

### Crear un Superusuario (para acceder al admin)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear un usuario administrador.

### Acceder al Panel de Administración

Ve a `http://127.0.0.1:8000/admin/` e inicia sesión con tus credenciales de superusuario.

## 🧪 Pruebas

Para ejecutar las pruebas del proyecto:

```bash
python manage.py test
```

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Para contribuir:

1. Haz un fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Guías de Contribución

- Sigue las convenciones de código de Django
- Escribe pruebas para nuevas funcionalidades
- Actualiza la documentación según sea necesario

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Contacto

- **Autor**: Tu Nombre
- **Email**: tu.email@ejemplo.com
- **Proyecto**: [Enlace al repositorio](https://github.com/tu-usuario/home-about)

## 🙏 Agradecimientos

- [Django](https://www.djangoproject.com/) - El framework web utilizado
- [Python](https://www.python.org/) - El lenguaje de programación
- Comunidad de Django por la excelente documentación

---

⭐ Si te gusta este proyecto, ¡dale una estrella en GitHub!