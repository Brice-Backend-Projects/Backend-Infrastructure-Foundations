# Python Typing — Module Overview

## 🎯 Purpose

Briefly explain what this module covers.  
*This module will use the library `mypy` to anaylze a simple function with hints that passes an incorrect argument type.*

---

## 🧪 Experiments & Demos

List scripts, notebooks, or demos here with a 1–2 sentence description.

- `add_demo.py` → Compare add function with `int` vs. `str`.  
- `add_test.py` → Test function with incorrect types.
- `error_handle_add_test.py` -> Rewrites the function with proper error handling.  

---

## 📈 Results / Findings

The file, `add_demo.py` included several functions to observe behavior.  The following functions were created: 
- add_int(a,b)
- add_str(a,b)
- add_error(a,b)

The functions passed an int, str, and a combo of int/str, respectively.  The int added number, the str concantenated the string variables and the error threw a "TypeError: unsupported operand type(s) for +: 'int' and 'str'".  

Running the file through `mypy` library yielded the following:
`add_demo.py:10: error: Argument 1 to "add_str" has incompatible type "int"; expected "str"  [arg-type]
Found 1 error in 1 file (checked 1 source file)`
This result is telling the user that the types of arguments passed to the functions mismatch the expected data types required for the function.

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
