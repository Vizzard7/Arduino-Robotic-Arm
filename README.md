<h1>Arduino Robotic Arm</h1>

This project includes a robotic arm controller based on the Arduino platform. The arm servomotors are programmed in C++, which is the main tool for writing program code for Arduino microcontrollers. The robotic arm is controlled through a special interface developed in the Python programming language.


https://github.com/Vizzard7/Arduino-Robotic-Arm/assets/157525015/4e396aba-a000-48e9-ab56-20ed0655ec7e


<h1>Usage</h1>

1 - Install PlatformIO in the development environment. For more information use the fallowing link: <a> https://platformio.org </a>

2 - Intall pyserial to your project to communicate with Arduino, using the fallowing link: <a> https://pypi.org/project/pyserial/</a>

2 - Create a project based on this platform 

3 - Connect Arduino Uno to the computer

4 - Paste the code main.cpp which is located in src into the development environment

5 - Create a Python file and paste the code for the interface there.

6 - View the port to which the Arduino is connected

7 - Insert the port name into the comPort variable

8 - Upload the code to the Arduino

9 - Launch the interface to control the servo motors in the Robotic Arm
