# Building An Android APK

We can use the Buildozer tool to make a standalone fully functional android APK. First of all the dependencies should be taken care of after installing the tool. If you are using kivy on windows, there might be a few redundancies, so it is better to use Linux or any other platform. Instead you can also use a virtual box to make the APK on windows as well.

Following are the steps you need to follow to make a standalone android APK of your kivy application.

1. The first step after the installation is to make a .spec file using buildozer. This file will contain all the parameters you need while building your application. The following command will create a .spec file with default values.

> buildozer init

2. After you create a .spec file, you need to make a few changes, like title, package name, orientation, version, requirements, etc.

3. The next step, after you create all the necessary changes to the .spec file is to build your APK. The following command will make a android APK in a build mode.

> buildozer android debug  

The last argument ‘deploy’, tells buildozer to automatically install the APK on your device when the build process is over.

> buildozer android debug deploy
