"""Safe divide function"""

from typing import Optional

def safe_divide(a: float, b: float) -> Optional[float]:
    """Safe divide function"""
    if b == 0:
        return None
    return a / b

def main():
    print(f"safe_divide(10, 5) = {safe_divide(10, 5)}")
    print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")

if __name__ == "__main__":
    main()
