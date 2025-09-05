# Python Typing — Module Overview

## Purpose

Briefly explain what this module covers.  
*This module will use the library `mypy` to analyze a simple function with hints that passes an incorrect argument type.*

---

## Experiments & Demos

List scripts, notebooks, or demos here with a 1–2 sentence description.

### Type Mismatch Demo

- `add_demo.py` → Compare add function with `int` vs. `str`.  
- `add_test.py` → Test function with incorrect types.  
- `error_handle_add_test.py` -> Rewrites the function with proper error handling.  

### Strict Typing Demo

- Added `mypy` as a dev dependency. In the `pyproject.toml` file, the tool was set to strict (`strict = true`).  
- A simple function, `safe_divide(a,b)` was created. The function essentially returns `None` when dividing by zero and the float in all other cases.  
- The function was created with type assignments as well as return type, making the function strict typing compliant.  
- A second function, `main()` was created to call on the `safe_divide(a,b)` function and pass arguments.  
- The `main()` function did not assign a type to the return, originally. See Results for remaining discussion on this lab.  

---

## Results / Findings

### Type Mismatch Results

The file, `add_demo.py` included several functions to observe behavior. The following functions were created: 
- add_int(a,b)  
- add_str(a,b)  
- add_error(a,b)  

The functions passed an int, str, and a combo of int/str, respectively. The int added numbers, the str concatenated the string variables, and the error threw a "TypeError: unsupported operand type(s) for +: 'int' and 'str'".  


Running the file through `mypy` library yielded the following:
```bash
add_demo.py:10: error: Argument 1 to "add_str" has incompatible type "int"; expected "str"  [arg-type]
Found 1 error in 1 file (checked 1 source file)``` 

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

The function works as intended, but it is not optimized to pass `mypy` strict mode.  When the pyproject.toml tools dev dependencies strict mode is set to true, the library checks for strict typing compliant code so merely functional code will not necessarily pass without errors when running the `mypy` library.  

The errors in m`mypy` output tell us exactly what line is causing the error.  The `safe_divide` function passes strict mode, but the `main()` function does **not**.  In strict mode, every function must have a return type.  There are no attributes within the `main()` function.

**Solution**: Annotate the `main()` function with a return type:

```bash
def safe_divide(a: float, b: float) -> Optional[float]:
    """Safe divide function"""
    if b == 0:
        return None
    return a / b

def main() -> None:
    print(f"safe_divide(10, 5) = {safe_divide(10, 5)}")
    print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")

if __name__ == "__main__":
    main()
```

With the above code, the `mypy` yields a *Success* output

---

## Notes & Takeaways

### Topics to Discuss in this Section

- Key insights or conclusions from the experiments.
- What concepts you learned.  
- Pitfalls or surprises.  
- How this connects to real-world infra work (e.g., Affirm’s batch infra).  

### Type Mismatch

**Key insights or conclusions from the experiments**

- When assigning types to functions, the function will throw errors when mismatching.  
- The function will run even when the wrong type is passed as an argument, for example: `int` is defined, but `str` is passed **as long as both arguments are the same**.  

**What concepts you learned**

- In python, the types matter.  In JavaScript, the browser will make assumptions and run the code, but python will provide an error for an unsupported type.
- Details are important when writing Python applications.

### Strict Typing

**Key insights or conclusions from the experiments**

- First, I did not know about the library `mypy`, I can see a lot of usefulness knowing how to use this library.
- This library is useful to pass strict mode checks.
- Functional code is important, but type-safe code will be cleaner and easier to maintain..

**What concepts you learned**

- Strict mode will allow the code to run if it is functional.  It will only provide errors when the `mypy` library is used.
- Strict mode checks for **ALL** functions, so when a function is strictly calling another function to run and pass arguments, that function still needs to assign a return type.

**Pitfalls or surprises**

- I was surprised to see the `main()` function needed to have a return type assigned since all it was doing was calling another function to be run.

**How this connects to real-world infra work**

- Fintech and other regulated industries rely heavily on strict rulesets.  
- Setting up an environment in strict mode may come in very useful as it is easy to miss something.

---

## Next Steps

- Further experiments to run.
- Planned experiments or improvements.  
- Links to related modules (e.g., Python concurrency scripts that load into Postgres).  

---

## References

- Tutorials, docs, or articles that helped.
- [Postgres Indexing docs](https://www.postgresql.org/docs/current/indexes.html)
- [Postgres EXPLAIN docs](https://www.postgresql.org/docs/current/using-explain.html)
- [Official Postgres docs: Indexing](https://www.postgresql.org/docs/current/indexes.html)  
- [Designing Data-Intensive Applications](https://dataintensive.net/) (Ch. 3)  
