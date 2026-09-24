#!/bin/bash
echo "🪽 Iniciando EL PRIMER ANGEL - SaaS & KALI Panel..."
cd "$(dirname "$0")"

# Usar el python y streamlit del entorno virtual venv
if [ -f "venv/bin/streamlit" ]; then
    echo "🚀 Lanzando plataforma en el puerto 8501..."
    ./venv/bin/streamlit run app.py
else
    echo "❌ Error: Entorno virtual no encontrado o dependencias faltantes."
fi
