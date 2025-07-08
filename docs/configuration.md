# Guía de Configuración

## Variables de Entorno

### Configuración de la Aplicación

| Variable | Descripción | Valor por Defecto | Requerido |
|----------|-------------|-------------------|-----------|
| `ENV` | Entorno de ejecución (dev, testing, prod) | `dev` | No |
| `API_METRICS_USERNAME` | Usuario para acceder a métricas | `admin` | No |
| `API_METRICS_PASSWORD` | Contraseña para acceder a métricas | `admin` | No |

### Ejemplo de archivo .env

```env
# Entorno de ejecución
ENV=prod

# Credenciales para métricas
API_METRICS_USERNAME=prometheus_user
API_METRICS_PASSWORD=secure_password_123
```
