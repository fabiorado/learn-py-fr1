
# PyRepo
Learning Python.<br>
Basic scripts and functions created from lessons.

## Installation (ubuntu):

### GIT
``` bash
sudo apt-get update
sudo apt install git
sudo mkdir /home/fabio/projects
sudo chmod -R 777 /home/fabio/projects/
cd /home/fabio/projects/
git clone https://github.com/fabiorado/PyRepo.git PyRepo
cd PyRepo
```

### Python
```
sudo apt install python3.8
sudo apt install python3.8-pip
sudo apt install python3.8-venv
```
To solve the problem with "PySide6"
```
sudo apt install libopengl0 -y
```
### Setup a "venv"

``` python
python -m venv env
Windows >> env\Scripts\activate
Bash >> source env/bin/activate
code .
```
### Requirements
To install all the requirements
```
pip install -r requirements.txt
```
To generate the list of requirements
```
pip freeze > requirements.txt
```
## Questions and more

- TDD
- WebApp with Flask or Djungle?
- all-in executable (install)?
- module Typer why?

## Things to remender

- GIT basics
- TDD + pytest
- venv
- modules
    - | os | pathlib | json | PySide6 |

