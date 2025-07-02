FROM bitnami/spark:3.5

USER root

RUN mkdir -p /opt/spark/jars/ && \
    apt-get update && apt-get install -y \
    python3 python3-pip python3-dev libpq-dev gcc \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PYSPARK_PYTHON=python3
WORKDIR /opt/spark/app

COPY ./requirements.txt /opt/spark/requirements.txt
COPY ./scripts/startup.sh /opt/spark/startup.sh
COPY ./drivers/postgresql-42.6.0.jar /opt/spark/jars/postgresql-42.6.0.jar

RUN chmod +x /opt/spark/startup.sh

EXPOSE 8501

CMD ["/opt/spark/startup.sh"]
