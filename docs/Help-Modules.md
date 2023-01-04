# Help for the modules

## os
``` python
import os
print(os.path.dirname(__file__))
```

## pathlib
``` python
from pathlib import Path
print(Path("../test.txt").resolve())
```

## fake
```
pip install Faker
```
``` python
from faker import Faker
print(Faker().name())
```

## json
``` python
import json

with open("test.json", "w") as f:
    json.dump([1, 2, 3, 4], f, indent=4)
```
## pytest
```
pip install pytest
pytest -v
```

## pprint
_À vérifier..._
``` python
from pprint import pprint
```

## typer
_À vérifier..._
```
pip install typer
```

## pyside
Pour les interfaces graphiques.
```
pip instal PySide6
```
``` python
from PySide6 import QtCore, QtWidgets
```
