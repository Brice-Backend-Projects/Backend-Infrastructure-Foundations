# [Folder Name] — Module Overview

## 🎯 Purpose

Briefly explain what this module covers.  
*(Example for postgres_demos: “Explore indexing, partitioning, and transaction isolation in Postgres for performance at scale.”)*

---

## 🧪 Experiments & Demos

List scripts, notebooks, or demos here with a 1–2 sentence description.

- `index_demo.sql` → Compare query times with and without indexes.  
- `partitioning_test.sql` → Test table partitioning on large dataset.  
- `etl_loader.py` → Load CSV into Postgres with bulk vs single inserts.  

---

## 📈 Results / Findings

Summarize what you observed from the experiments. Include query times, logs, screenshots, or charts.

- Example: *“Adding a B-tree index reduced query time from 1200ms → 15ms.”*  
- Example: *“Bulk inserts were 6x faster than row-by-row inserts.”*  

---

## 📚 Notes & Takeaways

- Key insights or conclusions from the experiments.
- What concepts you learned.  
- Pitfalls or surprises.  
- How this connects to real-world infra work (e.g., Affirm’s batch infra).  

---

## 🚀 Next Steps

- Further experiments to run.
- Planned experiments or improvements.  
- Links to related modules (e.g., Python concurrency scripts that load into Postgres).  

---

## 📖 References

- Tutorials, docs, or articles that helped.
- [Postgres Indexing docs](https://www.postgresql.org/docs/current/indexes.html)
- [Postgres EXPLAIN docs](https://www.postgresql.org/docs/current/using-explain.html)
- [Official Postgres docs: Indexing](https://www.postgresql.org/docs/current/indexes.html)  
- [Designing Data-Intensive Applications](https://dataintensive.net/) (Ch. 3)  
