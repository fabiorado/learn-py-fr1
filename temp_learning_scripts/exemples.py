import json
from pathlib import Path

msg = "testing ..."

print(msg)

def t1():
    from faker import Faker
    print(Faker().name())

def t2():
    dir1 = Path("../src/data/test.json").resolve()
    print(dir1)
    with open(dir1, "x") as f:
        f.write("[]")

t2()