#!/usr/bin/env bash
set -euo pipefail

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER airflow WITH PASSWORD 'airflow';
    CREATE DATABASE airflow_db OWNER airflow;
    GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow;

    CREATE USER hive WITH PASSWORD 'hive';
    CREATE DATABASE metastore_db OWNER hive;
    GRANT ALL PRIVILEGES ON DATABASE metastore_db TO hive;
EOSQL
