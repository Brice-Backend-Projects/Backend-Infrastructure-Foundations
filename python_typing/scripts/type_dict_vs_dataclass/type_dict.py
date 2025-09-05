"""type_dict.py"""

from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    debug: bool

def main():
    """entry point"""
    u: User = {"name": "Brice", "age": 52, "debug": True}
    print(
        f'Name: {u["name"]} \nAge: {u["age"]}\nDebug: {u["debug"]}'
    )

if __name__ == "__main__":
    main()
