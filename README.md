# SentinelRAG: Private, Secure T&C and Contract QA Assistant (Discovery/Learning Prototype)

## Overview
**SentinelRAG** is a self-hosted prototype system designed to help individuals securely query the Terms & Conditions, NDAs, privacy policies, and other agreements they’ve signed — using natural language.

The idea for this project was inspired by a real experience:  
> *When I bought a home, I had to sign a large number of legal documents for the first time — and it made me realize how little visibility I had into what I was actually agreeing to.*  
That experience sparked the idea for a system that would let anyone securely upload their own contracts and later ask things like:
- “When does this agreement expire?”
- “What happens if I terminate early?”
- “Can they share my data with third parties?”

**SentinelRAG** aims to bring transparency and accessibility to legally binding documents — without sacrificing security or privacy.

Built using a Retrieval-Augmented Generation (RAG) architecture, the system demonstrates how GenAI can support personal legal comprehension while following best practices in infrastructure and DevSecOps.

*This project is a personal learning and infrastructure prototype, not yet intended for production use.*


### 🔍 Why this project?
When I bought a home, I had to sign dozens of legal documents for the first time. It made me realize how unclear and overwhelming contracts and T&C agreements can be — especially when you want to revisit them later.  
**SentinelRAG** was born from the need to ask questions like:
- “When does this agreement expire?”
- “Can they share my personal data?”
- “What happens if I cancel early?”

This project aims to make legal content more accessible — without compromising privacy — by combining Retrieval-Augmented Generation (RAG) with secure, enterprise-grade infrastructure patterns.

## What It Does
The system allows users to:
- Upload their own contracts or PDFs
- Ask natural-language questions about the contents
- Run entirely locally or securely in the cloud
- Use hardened infrastructure to keep sensitive data protected

## Key Practices Demonstrated
- TLS/mTLS encryption and hardened Docker containers
- Observability via Galileo GenAI SDK (or Prometheus + Grafana fallback)
- Kubernetes-based CI/CD with Helm and GitHub Actions
- Modular, API-first design using FastAPI and LangChain

> 🛡️ This is a **prototype**, not yet intended for production use. It is being developed to explore infrastructure, security, and reliability practices relevant to secure GenAI systems.

## Stack
- **Backend**: Python, FastAPI, LangChain
- **Retrieval**: FAISS
- **LLM**: OpenAI API (default), Mistral or other local models (optional)
- **Deployment**: Docker, Kubernetes, Helm, GitHub Actions
- **Security**: TLS, mTLS (Istio/NGINX), hardened containers (distroless + Trivy)
- **Observability**: Galileo SDK (primary), Prometheus + Grafana (fallback)

## Status
- First commit: June 7, 2025   
- MVP target: June 12, 2025  
- Actively being developed — structure and pipeline under construction


## Planned Structure
rag-secure-platform/
- backend/ # FastAPI + LangChain pipeline
- frontend/ # Streamlit app
- k8s/ # Helm charts, manifests
- security/ # TLS, OAuth2, hardening configs
- observability/ # Galileo fallback tools
- README.md # This file