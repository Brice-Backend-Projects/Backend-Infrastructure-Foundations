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

### Type Mismatch Results

The file, `add_demo.py` included several functions to observe behavior.  The following functions were created: 
- add_int(a,b)
- add_str(a,b)
- add_error(a,b)

The functions passed an int, str, and a combo of int/str, respectively.  The int added number, the str concantenated the string variables and the error threw a "TypeError: unsupported operand type(s) for +: 'int' and 'str'".  

Running the file through `mypy` library yielded the following:
`add_demo.py:10: error: Argument 1 to "add_str" has incompatible type "int"; expected "str"  [arg-type]
Found 1 error in 1 file (checked 1 source file)`
This result is telling the user that the types of arguments passed to the functions mismatch the expected data types required for the function.

### Strict Typing Results

The file `math_utils.py` was created with the function `safe_divide_demo` which divides two numbers and returns `None` if division by zero.  To begin the lab, the following function was written:

```python
def safe_divide(a: float, b: float) -> Optional[float]:
    """Safe divide function"""
    if b == 0:
        return None
    return a / b

def main():
    print(f"safe_divide(10, 5) = {safe_divide(10, 5)}")
    print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")
```

The function runs as intended, but when run in strict mode with `mypy`, the following error was rendered:

```bash
math_utils_demo.py:11: error: Function is missing a return type annotation  [no-untyped-def]
math_utils_demo.py:11: note: Use "-> None" if function does not return a value
math_utils_demo.py:16: error: Call to untyped function "main" in typed context  [no-untyped-call]
(backend-infrastructure-foundations) bnelson_regex@
```

Then, the strict mode was removed and run in `mypy` again, which yielded the following result:

```bash
Success: no issues found in 1 source file
```

The function works as intended, but it is not optimized to be Pythonic.  When the pyproject.toml tools dev dependencies strict mode is set to true, the library checks for pythonic code so merely functional code will not necessarily pass without errors when running the `mypy` library.



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
