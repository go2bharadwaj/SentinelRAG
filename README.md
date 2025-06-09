# SentinelRAG: Private, Secure T&C and Contract QA Assistant (Discovery/Learning Prototype)

## Overview
**SentinelRAG** is a self-hosted prototype designed to help you make sense of the legal documents you’ve signed — from Terms & Conditions and NDAs to privacy policies and contracts — simply by asking questions in plain English.

### 💡 The idea for this project was inspired by a real experience:  
When I bought a home, I had to sign a large number of legal documents for the first time — and it made me realize how little visibility I had into what I was actually agreeing to. That experience sparked the idea for a system that would let anyone securely upload their own contracts and later ask meaningful questions about them — without needing to dig through legal jargon.


## 🔍 What SentinelRAG does
**SentinelRAG** lets you:
- Upload contracts, policies, or agreements
- Ask natural-language questions like:
  - “Can they share my data?”
  - “Am I locked into a renewal?”
  - “Who owns the intellectual property?”
- Receive fast, relevant answers that help you understand what you’ve agreed to — without reading every clause manually.

## 🔐 Why it matters
Legal documents shouldn’t be a black box. SentinelRAG aims to bring clarity, security, and control to your agreements, powered by Retrieval-Augmented Generation (RAG) and wrapped in best practices for DevOps and AI infrastructure.

This is an ongoing **learning prototype** 
— built to explore how GenAI, when combined with secure infrastructure, can make legal understanding more human-friendly and trustworthy.


## Key Practices Demonstrated
- TLS/mTLS encryption and hardened Docker containers
- Observability via Galileo GenAI SDK (or Prometheus + Grafana fallback)
- Kubernetes-based CI/CD with Helm and GitHub Actions
- Modular, API-first design using FastAPI and LangChain
- Uses hardened infrastructure to keep sensitive data protected

> 🛡️ This is a **prototype**, not yet intended for production use. It is being developed to explore infrastructure, security, and reliability practices relevant to secure GenAI systems.

## Stack

- **Backend**: Python, FastAPI, LangChain
- **Retrieval**: FAISS (persistent disk storage) (For now)
- **Embeddings**: HuggingFace (MiniLM-L6-v2)
- **LLM**: Mistral via Ollama (local inference using Ollama)
- **Security**: SHA256 deduplication, TLS/mTLS planned
- **Deployment**: Docker → K8s (via Helm)
- **Observability**: Galileo SDK (planned) or Prometheus + Grafana (fallback)
- **DevOps**: GitHub Actions (planned)

## Status
- First commit: June 7, 2025   
- MVP target: June 12, 2025  
- Actively being developed — structure and pipeline under construction

## Planned Structure
SentinelRAG/
SentinelRAG/
- backend/ # FastAPI app + LangChain pipeline
  * main.py # REST API (upload, ask, delete vectordb)
  * rag_pipeline.py
  * requirements.txt
- vectorstores/ # Persistent FAISS index + hash DB
- security/ # TLS, hardening configs (planned)
- k8s/ # Helm charts and manifests (planned)
- observability/ # Monitoring and tracing setup (planned)
- frontend/ # Streamlit UI (optional)
- README.md