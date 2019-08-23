from ADS1x15 import ADS1015
import machine, time
from machine import I2C

class buttons(object):
    #initialization
    def __init__(self):
        self.address = 0x74 #Fixed i2c PCA9539 address
        self.i2c = machine.I2C(sda=machine.Pin(14), scl=machine.Pin(27)) 
        self.i2c.start(); #start condition for i2c
        self.adc_ = ADS1015(machine.I2C(sda=machine.Pin(14), scl=machine.Pin(27)), 72) # ADS1015 is at i2c address 72
    
    def bytesToInt(self, bytes): #supporting func
        result = 0
        for b in bytes:
            result = result * 256 + int(b)
        return result
    
    def reverse(self, s): #supporting func
        str = "" 
        for i in s: 
            str = i + str
        return str
    
    def readState(self, pin): #read pin state func
        result = 0
        port_buf = ""
        port_p0 = "{0:b}".format(self.bytesToInt(self.i2c.readfrom_mem(self.address, 0x01, 1))) #access input port p0, read 1 byte
        port_p1 = "{0:b}".format(self.bytesToInt(self.i2c.readfrom_mem(self.address, 0x00, 1))) #access input port p1
        #fill with "0" if bits are missing, on both ports
        if len(port_p0) < 8:
            while(len(port_p0) < 8):
                port_p0 = "0" + port_p0
        if len(port_p1) < 8:
            while(len(port_p1) < 8):
                port_p1 = "0" + port_p1
        #join ports together
        port_buf += port_p0
        port_buf += port_p1
        port_p = self.reverse(port_buf)
        #check if we're looking at A or B buttons which work over channels 2 and 3 of ADS1015
        if pin == 16:
            if self.adc_.read(2) <= 500: #A button using ADC
                result = True
            else:
                result = False
        elif pin == 17:
            if self.adc_.read(3) <= 500: #B button using ADC
                result = True
            else:
                result = False
        else:
            #check if we're looking at pin 14 (which is inverted), and craft a final result accordingly
            if port_p[pin] == "0" and pin != 14:
                result = True
            elif port_p[pin] == "0" and pin == 14:
                result = False
            elif port_p[pin] == "1" and pin == 14:
                result = True
            else:
                result = False
        return (result)

    def readJoystickX(self):    #read joystick X value from ADS1015 channel 0
        x_val = 0
        x_val = self.adc_.read(0)
        return x_val
        
    def readJoystickY(self):    #read joystick Y value from ADS1015 channel 0
        y_val = 0
        y_val = self.adc_.read(1)
        return y_val

    def fetchPort(self): #fetch whole port p state (binary as string)
        result = 0
        port_p0 = "{0:b}".format(self.bytesToInt(self.i2c.readfrom_mem(self.address, 0x01, 1))) #access input port p0, read 1 byte
        port_p1 = "{0:b}".format(self.bytesToInt(self.i2c.readfrom_mem(self.address, 0x00, 1))) #access input port p1
        #fill with "0" if bits are missing, on both ports
        if len(port_p0) < 8:
            while(len(port_p0) < 8):
                port_p0 = "0" + port_p0
        if len(port_p1) < 8:
            while(len(port_p1) < 8):
                port_p1 = "0" + port_p1
        #join ports together
        port_buf += port_p0
        port_buf += port_p1
        port_p = self.reverse(port_buf)
        result = port_p
        return result






