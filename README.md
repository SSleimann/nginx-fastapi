<div>
    <h1 align="center">Nginx-Fastapi</h1>
    <p align="center">Este proyecto está enfocado en el uso de Nginx con Prometheus para el monitoreo de la aplicación</p>
</div>
<br/>

## Acerca del Proyecto

Este proyecto demuestra la integración de Nginx como servidor proxy para una API sencilla desarrollada en FastAPI. A su vez también tiene integrado Prometheus para el monitoreo de métricas y rendimiento.

Los objetivos principales del proyecto son:

- Mostrar la configuración y despliegue de estas tecnologías.
- Proporcionar un ejemplo práctico que sirva de guía.
- Utilizar Prometheus y mostrar ejemplos prácticos en la web.
- Demostrar buenas prácticas de arquitectura con contenedores.

## Características

- ✅ **FastAPI**: API moderna y rápida con documentación automática
- ✅ **Nginx**: Servidor proxy inverso para balanceo de carga
- ✅ **Prometheus**: Monitoreo y métricas
- ✅ **Docker**: Containerización completa de la aplicación
- ✅ **Logging**: Sistema de logs estructurado con Loguru
- ✅ **Autenticación**: Protección del endpoint de métricas
- ✅ **Salud del sistema**: Endpoints para monitoreo de CPU y memoria

### Construido con

Las tecnologias usadas en este proyecto son:

![fastapi-badge] ![docker-badge] ![nginx-badge] ![prometheus-badge]

## Arquitectura

![Architecture](docs/architecture.png)

## Instalación y Configuración

### Requisitos

- **Python 3.13+** (para desarrollo local)
- **Docker** y **Docker Compose**
- **Poetry** (manejo de dependencias)
- **Git** (instalación del proyecto)

### Instalación con Docker

1. **Clona el repositorio**

    ```bash
    git clone https://github.com/SSleimann/nginx-fastapi.git
    cd nginx-fastapi
    ```

2. **Construir y ejecutar los contenedores**

    ```bash
    docker compose up -d
    ```

3. **Acceder a los servicios**

   - **Prometheus**: <http://localhost:9090>
   - **FastAPI API**: <http://localhost:80>
   - **Swagger Docs**: <http://localhost:80/docs>
   - **Metricas**: <http://localhost:80/metrics>

## Instalacion Local

1. **Clona el repositorio**

    ```bash
    git clone https://github.com/SSleimann/nginx-fastapi.git
    cd nginx-fastapi
    ```

2. **Instala las dependencias**

    ```bash
    poetry install --no-root
    ```

3. **Iniciar servidor**

    ```bash
    poetry run uvicorn --reload --port 8080 main:app
    ```

# Documentación

Para información más detallada, consulta la [documentación completa](docs/)

## Roadmap

- [x] Configuración inicial e integración de FastAPI.
- [x] Integración de Prometheus para el monitoreo.
- [x] Dockerización de la aplicación.
- [x] Configuración de Nginx como proxy inverso.
- [x] Crear `docker-compose.yml`.
- [x] Finalizar la documentación.

## Soporte

Para mas informacion, puedes contactarme:

- **Email**: <sleimanjose23@hotmail.com>
- **LinkedIn**: <https://www.linkedin.com/in/sleiman-orocua/>

## Licencia

Este proyecto está licenciado bajo los términos de la [licencia](LICENSE) MIT.

<!-- Badges -->
[docker-badge]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[fastapi-badge]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[nginx-badge]: https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white&style=for-the-badge
[prometheus-badge]: https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white