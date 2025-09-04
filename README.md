# Backend Infra Foundations

A structured **learning lab** and portfolio repo documenting my journey into backend infrastructure engineering.  
This repo contains hands-on experiments, demos, and notes as I work toward senior-level backend/infra roles (e.g., Batch Infra @ Affirm).

---

## 🎯 Purpose

- Gain practical experience with **core backend/infra concepts**: databases, ETL, orchestration, and Kubernetes.
- Build and document **foundational backend/infra skills**: databases, orchestration, distributed systems, and cloud.  
- Serve as a **living portfolio** of infrastructure experiments and technical growth.  
- Generate material for technical blog posts and interview prep.  

---

## 📂 Repo Structure

```plaintext
backend_infra_foundations/
│
├── postgres_demos/         # Indexing, partitions, transactions, EXPLAIN ANALYZE
│   ├── scripts/
│   └── README.md
│
├── python_concurrency/     # asyncio, multiprocessing, futures examples
│   ├── scripts/
│   └── README.md
│
├── etl_batch_jobs/         # Mini ETL pipelines (CSV → Postgres)
│   ├── scripts/
│   └── README.md
│
├── airflow_dags/           # Airflow DAG examples (local Docker)
│   ├── dags/
│   └── README.md
│
├── k8s_experiments/        # First deployments (Hello World, DB in cluster)
│   ├── manifests/
│   └── README.md
│
├── book_notes/             # Notes from *Designing Data-Intensive Applications*
│   ├── ch1-3.md
│   ├── ch4-5.md
│   └── ...
│
└── README.md               # (this file)
```

---

## 🛠️ Planned Topics & Milestones

### Databases (Postgres)

- Indexing and query optimization  
- Partitioning and performance testing  
- Transactions and isolation levels  

### Python at Scale

- Asyncio and concurrency models  
- Multiprocessing for CPU-bound tasks  
- Comparing threading vs async performance  

### ETL / Batch Jobs

- Mini ETL pipelines (CSV → Postgres)  
- Bulk inserts vs row inserts  
- Error handling and retries  

### Workflow Orchestration

- Airflow DAGs (local Docker install)  
- File ingestion pipeline → Postgres  
- Simple transform DAGs (CSV cleanup)  

### Kubernetes (Introductory)

- Run Hello World container on `minikube`  
- First deployment manifests  
- Reflections on running DBs in K8s vs managed services  

### Distributed Systems Concepts

- Notes and takeaways from *Designing Data-Intensive Applications* (Kleppmann)  
- Summaries and diagrams by chapter  

---

## 📅 Timeline (Sept – Dec 2025 Goals)

- **Sept:** Postgres indexing + partitioning, Python concurrency basics  
- **Oct:** Transactions, ETL batch jobs, initial K8s exposure  
- **Nov:** Airflow DAGs + book notes  
- **Dec:** Repo milestone: Postgres demos, ETL jobs, Airflow DAG, and book notes  

---

## ✍️ Blog Pipeline

This repo will also serve as the source for technical blog posts:

1. *Making Postgres Scale with Indexes & Partitions*  
2. *Understanding Postgres Transactions & Isolation Levels*  
3. *My First DAG: Lessons from Airflow*  

---

## ✅ Deliverables by Dec 3, 2025

- **Repo** with working demos (Postgres, ETL, Airflow, K8s basics).  
- **3 blog drafts** published or ready to publish.  
- **Technical notes** on *Designing Data-Intensive Applications* (Ch. 1–5).  

---

> 🚀 This repo is not a production app. It’s a **portfolio lab** to sharpen backend infrastructure skills and prepare for senior-level roles in backend/infra engineering.
