# SentinelRAG: Secure, Observable RAG Platform for Enterprise QA (Discovery/Learning Prototype)

## Overview
**SentinelRAG** is a prototype system that simulates a secure, production-grade Retrieval-Augmented Generation (RAG) application. It is designed to test and demonstrate how enterprise-grade GenAI systems can be built with strong security, observability, and reliability principles.

The system enables secure question answering over private documents (e.g., resumes, PDFs), while incorporating modern DevOps and MLOps practices such as:

- TLS/mTLS encryption and hardened Docker containers
- Observability through Galileo's GenAI SDK or Prometheus/Grafana
- Kubernetes-based CI/CD with Helm and GitHub Actions
- Modular, API-driven architecture with FastAPI and LangChain

This project is a **testing prototype**, not yet intended for production use. It is being developed to explore and demonstrate infrastructure practices relevant to building reliable, secure GenAI systems — especially those aligned with roles such as Senior DevOps at AI companies like Galileo.

## Stack
- **Backend**: Python, FastAPI, LangChain
- **Deployment**: Docker, Kubernetes, Helm, GitHub Actions
- **Security**: TLS, mTLS (Istio/NGINX), hardened container images (distroless, Trivy)
- **Observability**: Galileo SDK (primary), Prometheus + Grafana (fallback)

## Status
=> In Progress – First commit: June 7th, 2025  
=> MVP delivery goal: June 12th, 2025  
=> This is a **prototype project for learning and demonstration purposes only**

## Planned Structure
rag-secure-platform/
- backend/ # FastAPI + LangChain pipeline
- frontend/ # Streamlit app
- k8s/ # Helm charts, manifests
- security/ # TLS, OAuth2, hardening configs
- observability/ # Galileo fallback tools
- README.md # This file