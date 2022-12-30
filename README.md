
# PyRepo
Learning Python.<br>
Basic scripts and functions created from lessons.

## Installation (ubuntu):

### GIT
``` bash
sudo apt-get update
sudo apt install git
git config --global user.name "Fabio Rado"
git config --global user.email "fabio.rado@hotmail.com"

sudo mkdir /home/fabio/projects
sudo chmod -R 777 /home/fabio/projects/
cd /home/fabio/projects/
git clone https://github.com/fabiorado/PyRepo.git PyRepo
cd PyRepo
```

### Python

#### Python 3.8
Python 3.8 cammes with Ubuntu 20.04 and we it's not a good idea to tuch him.

```
sudo apt install python3.8
sudo apt install python3-pip
    OR >> sudo apt install python3.8-pip
sudo apt install python3-venv
    OR >> sudo apt install python3.8-venv
```

To solve the problem with "PySide6"
```
sudo apt install libopengl0 -y
```
#### Python 3.10 (ubuntu)

We can install another version and use the linux command "update-alternatives" to set and alternate between them.

1. Add the new repo and install python
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10
```
2. Set the links to both versions

```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2
```

3. List and alternate between the versions
```
update-alternatives --list python3
update-alternatives --config python3
```

4. Other necessary configurations
```
sudo apt remove --purge python3-apt
sudo apt autoclean
sudo apt install python3-apt

sudo apt install python3.10-distutils
sudo apt install python3-pip
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10

sudo apt install python3.10-venv
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

