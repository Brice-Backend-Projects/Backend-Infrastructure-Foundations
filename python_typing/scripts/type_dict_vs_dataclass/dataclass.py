"""dataclasses"""

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    debug: bool

    def __str__(self)->str:
        return f'Name: {self.name} \nAge: {self.age}\nDebug: {self.debug}'

def main()->None:
    """entry point"""
    u = User("Brice", 52, True)
    print(u)

if __name__ == "__main__":
    main()
