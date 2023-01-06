
# PyRepo
Learning Python.<br>
Instructions, basic scripts and functions created from lessons.

Other articles:  
* [Notes of project ideas](docs/notes_project_ideas.md)
* [Install Kivy on WSL](docs/Install-Kivy-on-WSL.md)
* [Help Modules](docs/Help-Modules.md)
* [Build Android APK](docs/build_android_apk.md)
* [Template for the "Main.py" file with Kivy](docs/template-main-py-kivy.md)

Links:
* [WSL Installation doc](https://learn.microsoft.com/en-us/windows/wsl/install)

## Installation (ubuntu):

### GIT
``` bash
sudo apt update && sudo apt upgrade
git config --global user.name "Fabio Rado"
git config --global user.email "fabio.rado@hotmail.com"

sudo mkdir ~/projects/repos-git/
sudo chmod -R 777 ~/projects
cd ~/projects/repos-git/
git clone https://github.com/fabiorado/PyRepo.git PyRepo
cd PyRepo
```

### Setup a "venv"

```sh
mkdir ~/projects/venvs/
cd ~/projects/venvs/
python -m venv env_py310
source env_py310/bin/activate
```

------------------------------
## Troubleshooting history
------------------------------

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

Python 3.10 cammes with Ubuntu 22.04 and we it's not a good idea to touch him.  
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
- WebApp with Flask
- all-in executable (install)?
- module Typer why?

## Things to remender

- GIT basics
- TDD + pytest
- venv
- modules
    - | os | pathlib | json | PySide6 |

