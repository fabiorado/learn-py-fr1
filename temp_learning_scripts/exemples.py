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

def t3():
    import uuid
    print(str(uuid.uuid4()))

def t4():
    # dict1 = ['user']
    dict1 = []
    if dict1 is None:
        print("None")

t4()