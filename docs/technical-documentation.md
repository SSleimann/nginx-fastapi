# Documentación Técnica - Nginx FastAPI

## Configuración de Nginx

### Archivo de Configuración

El archivo `nginx.conf` contiene la configuración del servidor proxy inverso:

```nginx
upstream backend {
    server web:8080; # Automaticamente mapea los servidores replicas.
}

server {
    listen 80;
    server_name localhost;

    location = /metrics {
        return 301 /;  # Redirige a la ruta / para evitar accesos no autorizados.
    }

    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        add_header X-XSS-Protection "1; mode=block"; # Agrega proteccion contra XSS
        add_header X-Frame-Options "SAMEORIGIN"; # Evita clickjacking
        add_header X-Content-Type-Options "nosniff"; #Previene MIME type sniffing
    }
}
```

## Configuración de Prometheus

### Archivo de Configuración

El archivo `config/prometheus.yaml` define cómo Prometheus recolecta métricas:

```yaml
global:
  scrape_interval: 15s # Hace el scrape cada 15 segundos

scrape_configs:
  - job_name: "http-example"

    docker_sd_configs:
      - host: "unix:///var/run/docker.sock" # Conexion con Docker para el Service Discovery
        port: 8080 # Obtiene el puerto 8080 de las metricas

    basic_auth:
      username: creds # Credenciales de autenticacion
      password: creds # Credenciales de autenticacion

    relabel_configs:
      - source_labels: [__meta_docker_container_label_prometheus_job]
        action: keep
        regex: web # Esta regla hace que solo se obtenga los contenedores con el label prometheus_job=web
      - source_labels: [__meta_docker_container_name]
        action: replace
        target_label: container_name
        regex: ^/(.+)$
        replacement: "$1" # Esta regla sustituye el container_name por el nombre del contenedor de Docker

  - job_name: "docker-host" # Scrapea el daemon de Docker, es opcional. Se debe configurar Docker para esto. https://docs.docker.com/engine/daemon/prometheus/
    static_configs:
      - targets: ["host.docker.internal:9323"]

  - job_name: "prometheus" # Scrape a prometheus
    static_configs:
      - targets: ["localhost:9090"]
```

### Métricas Recolectadas

Las metricas disponibles por la API son:

| Métrica | Tipo | Descripción | Labels |
|---------|------|-------------|--------|
| `cpu_usage` | Gauge | CPU usage in percentage | - |
| `memory_usage` | Gauge | Memory usage in bytes | - |
| `request_count` | Counter | Total number of requests | method, endpoint, status_code |
| `request_latency_seconds` | Histogram | Request latency in seconds | method, endpoint, status_code |
| `requests_in_progress` | Gauge | Number of requests in progress | method, endpoint |