from prometheus_client import Counter, Gauge, Histogram

# Memory usage metrics
CPU_USAGE = Gauge(
    "cpu_usage",
    "CPU usage in percentage",
    multiprocess_mode="liveall",
)
MEMORY_USAGE = Gauge(
    "memory_usage",
    "Memory usage in bytes",
    multiprocess_mode="liveall",
)

# Request metrics
REQUEST_COUNT = Counter(
    "request_count",
    "Total number of requests",
    labelnames=["method", "endpoint", "status_code"],
)
REQUEST_LATENCY = Histogram(
    "request_latency_seconds",
    "Request latency in seconds",
    labelnames=["method", "endpoint", "status_code"],
)
REQUESTS_IN_PROGRESS = Gauge(
    "requests_in_progress",
    "Number of requests in progress",
    labelnames=["method", "endpoint"],
    multiprocess_mode="livesum",
)
