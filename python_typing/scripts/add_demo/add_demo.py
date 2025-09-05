"""Compare add function with `int` vs. `str`."""

def add_int(a:int, b:int) -> int:
    return a + b

def add_str(a:str, b:str) -> str:
    return a + b

int_demo = add_int(1, 2)
str_demo = add_str("1", "2")
int_demo_error = add_int("1", "2")
#str_demo_error = add_str(1, "2")

def add_demo() -> None:
    print(f"int_demo: {int_demo}")
    print(f"str_demo: {str_demo}")
    print(f"int_demo_error: {int_demo_error}")
    #print(f"str_demo_error: {str_demo_error}")

if __name__ == "__main__":
    add_demo()
