# Building An Android APK
[README](../README.md)  

## Links

* [Buildozer's docs](https://buildozer.readthedocs.io/en/latest/installation.html)
* [WSL Installation doc](https://learn.microsoft.com/en-us/windows/wsl/install)
* [Video from MariyaSha](https://www.youtube.com/watch?v=VsTaM057rdc)


## WSL2 and Ubuntu

1. Start a new instance of ubuntu (20.04 or 22.04)

2. Update apt
```sh
sudo apt update && sudo apt upgrade
```

3. Installations
```sh
sudo apt install python3-pip
```

4. Create folders
```sh
sudo mkdir ~/projects/repos-git
sudo chmod -R 777 ~/projects
cd ~/projects/repos-git
git clone https://github.com/fabiorado/fr1-py-game-bird-kivy.git
```

## Buildozer

### Installation
pip
```sh
pip3 install --user --upgrade buildozer
```
Dependecies
```sh
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
```
Cython
```sh
pip3 install --user --upgrade Cython==0.29.19 virtualenv
```
### set PATH
```sh
vim ~/.bashrc
```
Add this to the end:
```sh
export PATH=$PATH:~/.local/bin/
```
Use this to save and quit VIM
> \<ESC> + :wq!


> **Note:**  
For debugging, WSL does not have direct access to USB. Copy the .apk file to the Windows partition and run ADB (Android Debug Bridge) from a Windows prompt.


### Build the App

```sh
buildozer init
```

Edit the "buildozer.spec" file.  
You should at least change the title, package.name and package.domain in the [app] section.
* Attention to the "source.dir = ./src"
* If you have other files extentions, add here: "source.include_exts = py,png,jpg,kv,atlas"
* Specify the version(40): "requirements = python3,kivy=2.1.0"
* Uncomment (252): "android.logcat_filters = *:S python:D"


Start a Android/debug build

```sh
buildozer -v android debug
```
> **Note:** It takes around 20 minutes.

End of instruction:
```
# Android packaging done!
# APK BirdMario-0.1-arm64-v8a_armeabi-v7a-debug.apk available in the bin directory
```


### App in Phone

**Copy the "APK" to the phone, install and open it!**

