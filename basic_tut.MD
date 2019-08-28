
# Installation

## 0. Thonny IDE

To start programming your Ringo phone using MicroPython, you will need an IDE. Thonny IDE offers a simple interface and tools that you will need to get you started.

We provided a setup file for Thonny IDE in the repository.

Install Thonny IDE and proceed to the next step.
## 1. Download CircuitMess-Ringo-python repository

Download the repository from this link: https://github.com/CircuitMess/CircuitMess-Ringo-python/archive/master.zip

## 2. Install Thonny IDE

We provided a setup file for Thonny IDE in the repository.
Install Thonny IDE and proceed to the next step.

## 3. Flashing Ringo with MicroPython firmware

Follow the guide at: https://learn.adafruit.com/building-and-running-micropython-on-the-esp8266/flash-firmware

**NOTE**: Remember to flash the provided "ESP32_c.bin" custom firmware as it contains all the dependencies required for Ringo phone to work with MicroPython!

## 4. Thonny IDE setup

Before starting you will need to configure the IDE to work with Ringo phone

<img src="https://www.dropbox.com/s/p10v8j5oos71r25/0_.png?raw=1" alt="drawing" width="700"/>

## Interpreter and serial port configuration

1. Tools -> Options -> Interpreter
<img src="https://www.dropbox.com/s/dqv5pj2kfrpym33/1_.png?raw=1" alt="drawing" width="700"/>

<img src="https://www.dropbox.com/s/z7rwx20pmkt9j6w/2_.png?raw=1" alt="drawing" width="700"/>

2. Dropdown menu -> MicroPython on a generic device
	
3. Select your serial port from the second dropdown menu (Silicon Labs CP210x USB to UART Bridge(COMx))
<img src="https://www.dropbox.com/s/2ru2y8saev4webj/3_.png?raw=1" alt="drawing" width="700"/>

**NOTE** If you're having issues with drivers, we've included SiliconLabsC210x drivers in the repository. Follow instructions [here](https://startingelectronics.org/software/arduino/installing-arduino-software-windows-10/) (Windows 10)

## Uploading and running scripts
	
1. File -> Open
2. Open one of the scripts in the /examples folder provided in the repository
3. To run the script you have two options:
		
<b>a) Upload and run a script</b>	
1. Device -> Upload current script with current name
<img src="https://www.dropbox.com/s/lsnd4z74h3rw3ul/4_.png?raw=1" alt="drawing" width="700"/>


2. To run the script from Ringo phone, use REPL Shell (Bottom of the IDE screen), type:
	
	import scriptName
	
<img src="https://www.dropbox.com/s/h01voezv2x6gf8m/6_.png?raw=1" alt="drawing" width="700"/>


<b>b) Run a script without uploading it</b>  
1. Press the Run current script button and your script will run without uploading to your device
<img src="https://www.dropbox.com/s/1dfotrnozfevgdl/5_.png?raw=1" alt="drawing" width="700"/>


You're now ready to start writing your own MicroPython scripts and running them on your Ringo phone!
