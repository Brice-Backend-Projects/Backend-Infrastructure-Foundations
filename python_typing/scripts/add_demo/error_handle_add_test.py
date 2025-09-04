"""Rewrites the function with proper error handling."""

def add_error(a: int, b: int) -> int:
    try:
        return a + b
    except TypeError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def main_demo():
    print(f"add_error(1, 2) = {add_error(1, 2)}")
    print(f"add_error('1', '2') = {add_error('1', '2')}")
    print(f"add_error(1, '2') = {add_error(1, '2')}")

def main():
    main_demo()

if __name__ == "__main__":
    main()
