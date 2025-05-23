#!/bin/sh

# Set the values of the prometheus environment variables
export PROMETHEUS_MULTIPROC_DIR="/tmp/prometheus/prometheus_multiproc"

echo "Setting up the prometheus multiproc directory..."

if [ -d "$PROMETHEUS_MULTIPROC_DIR" ]; then
    echo "Cleaning up the prometheus multiproc directory..."
    rm -rf "${PROMETHEUS_MULTIPROC_DIR:?}"/*
else
    echo "Creating the prometheus multiproc directory..."
    mkdir -p "$PROMETHEUS_MULTIPROC_DIR"
fi

echo "Starting the application..."

# Start the application
gunicorn -k uvicorn.workers.UvicornWorker --access-logfile - --bind 0.0.0.0:8080 -w 4 main:app 