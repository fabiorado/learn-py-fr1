echo "------------------------------------------"
echo "Script to help with 'Python', 'Kivy' and 'Buildozer'"

# Variables
gitCloneURL="https://github.com/fabiorado/fr1-py-game-bird-kivy.git"

# Menu
cat << EOF
------------------------------------------
Choose an option:

1 -> Intall Buildozer
2 -> Generate APK
------------------------------------------
EOF

read option

# if [[ ( $username == "admin" && $password == "secret" ) ]]; then

if [ -z "$option" ]; then
    echo "You need to make a choise."
elif [ $option == 1 ]; then
    echo "option 1"
elif [ $option == 2 ]; then
    echo "gitCloneURL -> $gitCloneURL"
else
    echo "choise dont exists"
fi


if [ $option == 9 ]; then
    echo "Starting..."
    # sudo apt update && sudo apt upgrade

    # echo "Pip..."
    # sudo apt install python3-pip

    # echo "Git configuration..."
    # git config --global user.name "Fabio Rado"
    # git config --global user.email "fabio.rado@hotmail.com"

    # echo "Git clone..."
    # sudo mkdir ~/projects/repos-git
    # sudo chmod -R 777 ~/projects
    # cd ~/projects/repos-git
    # git clone $gitCloneURL

    # echo "Buildozer..."

    # pip3 install --user --upgrade buildozer
    # sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
    # pip3 install --user --upgrade Cython==0.29.19 virtualenv

    # export PATH=$PATH:~/.local/bin/
fi

echo "Now, go to the project folder and continue avec buildozer."

# buildozer init
# buildozer -v android debug
