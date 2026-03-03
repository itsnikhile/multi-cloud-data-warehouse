# Multi-Cloud Data Warehouse

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

> AWS Redshift + Azure Synapse + GCP BigQuery — unified query layer

## Architecture

![Architecture Diagram](./architecture.svg)

## Project Structure

```
multi-cloud-data-warehouse/
    ├── .env.example
    ├── .gitignore
    ├── Makefile
    ├── main.py
    ├── requirements.txt
    ├── config/
    ├── docker/
    ├── sql/
    ├── src/
        ├── __init__.py
        ├── connectors/
            ├── bigquery_connector.py
            ├── redshift_connector.py
            ├── synapse_connector.py
        ├── router/
            ├── query_router.py
        ├── sync/
            ├── cross_cloud_sync.py
        ├── utils/
    ├── terraform/
        ├── main.tf
    ├── tests/
        ├── __init__.py
```

## Quick Start

```bash
# 1. Clone
git clone https://github.com/itsnikhile/multi-cloud-data-warehouse
cd multi-cloud-data-warehouse

# 2. Install
pip install -r requirements.txt

# 3. Configure
cp .env.example .env
# Edit .env with your credentials

# 4. Run demo (no external services needed)
python main.py demo
```

## Local Development with Docker

```bash
# Start all infrastructure (Kafka, Redis, etc.)
docker-compose up -d

# Run the full pipeline
make run

# Run tests
make test
```

## Running Tests

```bash
pytest tests/ -v --cov=src --cov-report=term-missing
```

## Configuration

All config is in `config/config.yaml`. Override with environment variables.
Copy `.env.example` to `.env` and fill in your credentials.

## Key Features

- ✅ Production-grade error handling and retry logic
- ✅ Comprehensive test suite with mocks
- ✅ Docker Compose for local development
- ✅ Makefile for common commands
- ✅ Structured logging with metrics
- ✅ CI/CD ready (GitHub Actions workflow)

---

> Built by [Nikhil E](https://github.com/itsnikhile) — Senior Data Engineer
