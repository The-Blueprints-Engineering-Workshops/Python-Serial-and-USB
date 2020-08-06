#File: PythonUSBDemo
#Purpose: The purpose of this code is to connect to a wired USB device and read the data it outputs

#Relevant Imports
import usb.core
import usb.util

#Vendor and Product ID values

#Wired Mouse
#vendor=0x413c #This changes depending on the particular brand of device
#product=0x3012 #This changes depending on the particular device

#Wired Keyboard
vendor=0x413c
product=0x2105

#Assumes system backend is configured to work with PyUSB. Windows OS will require configuration.

#Discover the device. 
dev = usb.core.find(idVendor=vendor, idProduct=product)

#The first found endpoint
endpoint = dev[0][(0,0)][0]

#For the first found interface
interface = 0

#If the device is found
if dev.is_kernel_driver_active(interface) is True:
    #Detach from Operating System
    dev.detach_kernel_driver(interface)
    #Attach to this program
    usb.util.claim_interface(dev,interface)

#Loop variables
collected = 0
attempts = 50

#Until 50 data packets are collected, keep looping.
while collected < attempts:
    #Attempt to read the data and print to the terminal
    collected += 1
    try:
        data = dev.read(endpoint.bEndpointAddress,endpoint.wMaxPacketSize)
        #collected += 1
        print(data)
    #If USB exception occurs, simply ignore and continue looping
    except usb.core.USBError as e:
        data = None
        print("{C}: Operation timed out.".format(C=collected))

#Release the interface
usb.util.release_interface(dev, interface)

#Reattach to the Operating System so that it will function as normal
dev.attach_kernel_driver(interface)
