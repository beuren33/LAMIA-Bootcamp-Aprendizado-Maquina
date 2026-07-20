# Base Image
FROM apache/airflow:2.10.3-python3.12
LABEL maintainer="LAMIA-Bootcamp"

USER root

# Java para o pyspark (spark-submit)
RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
        default-jdk-headless \
        procps \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV SPARK_HOME=/home/airflow/.local/lib/python3.12/site-packages/pyspark
ENV PATH="${SPARK_HOME}/bin:${PATH}"

USER airflow

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /requirements.txt \
        --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.3/constraints-3.12.txt"
