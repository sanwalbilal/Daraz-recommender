# Daraz Recommender System

An intelligent product recommendation system for Daraz (Pakistan's largest e-commerce platform) powered by Retrieval-Augmented Generation (RAG) and LangChain.

## Overview

The Daraz Recommender System uses advanced AI techniques to provide personalized product recommendations and answer customer queries based on product reviews and metadata. The system leverages:

- **RAG (Retrieval-Augmented Generation)**: Combines document retrieval with LLM generation for accurate, context-aware responses
- **LangChain**: Framework for building LLM applications with memory and conversation history
- **AstraDB**: Serverless vector database for efficient similarity search
- **Groq LLM**: Fast inference engine for real-time recommendations
- **Prometheus + Grafana**: Monitoring and metrics visualization

## Project Structure

```
Daraz_recomder/
├── app.py                          # Flask application entry point
├── Dockerfile                      # Docker container configuration
├── requirements.txt                # Python dependencies
├── setup.py                        # Package setup configuration
├── daraz/                          # Main package
│   ├── __init__.py
│   ├── config.py                  # Configuration settings
│   ├── data_converter.py          # Data processing utilities
│   ├── data_ingestion.py          # Vector store ingestion
│   └── rag_chain.py               # RAG chain builder
├── data/
│   └── daraz_product_review.csv   # Product review dataset
├── utils/
│   ├── __init__.py
│   ├── custom_exception.py        # Custom exceptions
│   └── logger.py                  # Logging utilities
├── templates/
│   └── index.html                 # Web UI
├── static/
│   └── style.css                  # Styling
├── grafana/
│   └── grafana-deployment.yaml    # Grafana deployment config
└── prometheus/
    ├── prometheus-configmap.yaml  # Prometheus configuration
    └── prometheus-deployment.yaml # Prometheus deployment config
```

## Features

- 🤖 **AI-Powered Recommendations**: Get personalized product suggestions using RAG
- 💬 **Conversational Interface**: Interactive chat-based UI for queries
- 📊 **Real-time Monitoring**: Prometheus metrics and Grafana dashboards
- 🐳 **Containerized Deployment**: Docker and Kubernetes ready
- 🔄 **Vector-based Search**: Semantic similarity search for accurate results
- 💾 **Session Management**: Maintains conversation history for context

## Prerequisites

- Python 3.8+
- Docker (for containerized deployment)
- Kubernetes cluster (for Kubernetes deployment)
- API Keys:
  - Groq API Key (for LLM)
  - AstraDB credentials (for vector store)
  - HuggingFace API Key (for embeddings)

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Daraz_recomder
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
ASTRADB_API_ENDPOINT=your_astradb_endpoint
ASTRADB_TOKEN=your_astradb_token
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

## Usage

### Local Development

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Accessing the Application

- **Web UI**: `http://localhost:5000/` - Interactive chat interface
- **Metrics**: `http://localhost:5000/metrics` - Prometheus metrics endpoint

### Docker Deployment

Build and run with Docker:

```bash
docker build -t daraz-recommender .
docker run -p 5000:5000 --env-file .env daraz-recommender
```

### Kubernetes Deployment

Deploy to Kubernetes cluster:

```bash
# Deploy Flask application
kubectl apply -f flask-deployment.yaml

# Deploy Prometheus
kubectl apply -f prometheus/prometheus-configmap.yaml
kubectl apply -f prometheus/prometheus-deployment.yaml

# Deploy Grafana
kubectl apply -f grafana/grafana-deployment.yaml
```

## API Endpoints

### GET `/`
Returns the web UI for interacting with the recommender system.

**Response**: HTML page with chat interface

### POST `/get`
Send a user query to get product recommendations or answers.

**Request**:
```json
{
  "msg": "What are the best smartphones under 50000?"
}
```

**Response**:
```json
"Recommended products: [list of products with explanations]"
```

### GET `/metrics`
Returns Prometheus metrics for monitoring.

**Response**: Prometheus format metrics

## Configuration

Edit `daraz/config.py` to modify:
- Vector store settings
- LLM parameters
- Embedding model selection
- Chain configuration

## Dependencies

| Package | Purpose |
|---------|---------|
| `langchain` | LLM framework |
| `langchain-astradb` | AstraDB integration |
| `langchain-groq` | Groq LLM integration |
| `langchain-huggingface` | HuggingFace embeddings |
| `flask` | Web framework |
| `prometheus_client` | Metrics collection |
| `pandas` | Data processing |
| `pypdf` | PDF processing |
| `datasets` | Dataset utilities |

## Monitoring

### Prometheus
- **URL**: `http://localhost:9090` (if running locally)
- **Scrape interval**: Configurable in `prometheus/prometheus-configmap.yaml`

### Grafana
- **URL**: `http://localhost:3000` (if running locally)
- **Default credentials**: admin/admin (change in production)
- **Data source**: Prometheus

### Metrics Tracked
- `http_requests_total`: Total HTTP requests received

## Troubleshooting

### Connection Issues
- Verify API keys in `.env` file
- Check AstraDB endpoint accessibility
- Ensure Groq API is reachable

### Vector Store Issues
- Clear existing vector store and reingest data: Set `load_existing=False` in `data_ingestion.py`
- Verify CSV data format

### Performance Issues
- Monitor Prometheus metrics
- Check Grafana dashboards for bottlenecks
- Adjust batch sizes in configuration

## Development

### Project Setup
```bash
pip install -e .
```

### Running Tests
```bash
pytest
```

### Code Structure

- **app.py**: Flask application and route definitions
- **daraz/rag_chain.py**: RAG chain construction and LLM interaction
- **daraz/data_ingestion.py**: Vector store initialization and data ingestion
- **utils/**: Logging and error handling utilities

## Contributing

1. Create a feature branch
2. Make changes and commit
3. Push to remote repository
4. Create a pull request

## License

[Add your license information here]

## Author

Sanwal Bilal

## Support

For issues and questions, please open an issue in the repository or contact the maintainers.

---

**Last Updated**: 2026-07-03
