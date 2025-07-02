#!/bin/bash

echo ">> Iniciando Spark"
spark-submit --jars /opt/spark/jars/postgresql-42.6.0.jar

python3 -m pip install --upgrade pip

echo ">> Instalando requirements"
pip install -r /opt/spark/requirements.txt --timeout 720


echo ">> Iniciando app do streamlit"
streamlit run /opt/spark/app/main.py --server.port=8501 --server.address=0.0.0.0

tail -f /dev/null
