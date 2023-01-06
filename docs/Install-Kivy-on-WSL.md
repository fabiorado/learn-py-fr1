# Install Kivy on WSL

[README](../README.md)  

> WSL with Ubuntu 22.04

## Config

```
sudo apt update && sudo apt upgrade
sudo apt install python3-pip
sudo apt install python3-venv
```

Create python venv
```
sudo mkdir ~/projects
sudo mkdir ~/projects/venvs
sudo chmod -R 777 ~/projects
cd ~/projects/venvs
python3 -m venv kivy_env_py310
```

Activate venv
```
source ~/projects/venvs/kivy_env_py310/bin/activate
```

## On Windows

### WSL
Follow the article [Install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install) to install and configure WSL and VSCode.

### VcXsrv
Install "**VcXsrv**" on Windows host 

Execute:
```
vcxsrv.exe -ac
```
> **Note:** You need to check the option "_Disable access control_"

## GIT
```
git config --global user.name "Fabio Rado"
git config --global user.email "fabio.rado@hotmail.com"
```

Clone
```
cd ~/projects
git clone https://github.com/fabiorado/PyRepo.git PyRepo
cd PyRepo
code .
```

## Install Kivy
Inside the venv...

```
python3 -m pip install "kivy[full,tuio]" kivy_examples
sudo apt-get install libsdl2-image-dev
sudo apt-get install libmtdev-dev
```

Test of the "display"
```
sudo apt-get install -y x11-apps
xclock
xeyes
```

Run the examples
```
python3 ~/projects/venvs/kivy_env_py310/share/kivy-examples/demo/showcase/main.py
```
```
python3 ~/projects/venvs/kivy_env_py310/share/kivy-examples/3Drendering/main.py
```

## If you need

Create a role in the firewall to "VcXsrv"
> I went to Control Panel > System and Security > Windows Defender Firewall > >Advanced Settings > Inbound Rules > New Rule... > Program > %ProgramFiles%\VcXsrv\vcxsrv.exe > Allow the connection > checked >Domain/Private/Public > Named and Confirmed Rule.
