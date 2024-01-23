# include tkinter library

from tkinter import *

# include serial library for communication
import serial

# Variable for storing communication port

comPort = '/dev/cu.usbmodem1101'

#Making communication through Comport
ser = serial.Serial(comPort, baudrate=9600, timeout=1)

# Function for sending information to the servo_motors

def servo_angle(direction_angle, elbow_angle, compression_angle, handle_angle, comphan_angle):
    
    ser.write(f"{direction_angle},{elbow_angle},{compression_angle},{handle_angle},{comphan_angle}\n".encode())
    
# Getting information from the scale and send it to a motors

def scale_angle_direction(value):
    
    elbow_angle = int(elbow_scale.get())
    
    compression_angle = int(compression_scale.get())
    
    handle_angle = int(handle_scale.get())
    
    comphan_angle = int(comphan_scale.get())
    
    servo_angle(value, elbow_angle, compression_angle, handle_angle, comphan_angle)

# Getting information from the scale send it to a motors

def scale_angle_elbow(value):
    
    direction_angle = int(directional_scale.get())
    
    compression_angle = int(compression_scale.get())
    
    handle_angle = int(handle_scale.get())
    
    comphan_angle = int(comphan_scale.get())
    
    
    servo_angle(direction_angle, value, compression_angle, handle_angle, comphan_angle)
    
# Getting information from the scale send it to a motors

def scale_angle_compression(value):
    
    direction_angle = int(directional_scale.get())
    
    elbow_angle = int(elbow_scale.get())
    
    handle_angle = int(handle_scale.get())
    
    comphan_angle = int(comphan_scale.get())
    
    servo_angle(direction_angle, elbow_angle, value, handle_angle, comphan_angle)

# Getting information from the scale and send it to a motors
    
def scale_angle_handle(value):
    
    direction_angle = int(directional_scale.get())
    
    elbow_angle = int(elbow_scale.get())
    
    compression_angle = int(compression_scale.get())
    
    comphan_angle = int(comphan_scale.get())
    
    servo_angle(direction_angle, elbow_angle, compression_angle, value, comphan_angle)

# Getting information from the scale and send it to a motors
    
def scale_angle_comphan(value):
    
    direction_angle = int(directional_scale.get())
    
    elbow_angle = int(elbow_scale.get())
    
    compression_angle = int(compression_scale.get())
    
    handle_angle = int(handle_scale.get())
    
    servo_angle(direction_angle, elbow_angle, compression_angle, handle_angle, value)


# Functions for stop the motor and save their pozition
    

def scale_release_direction(event):
    
    ser.write(b"stopd\n")

def scale_release_elbow(event):
    
    ser.write(b"stope\n")

def scale_release_compression(event):
    
    ser.write(b"stopc\n")
    

def scale_release_handle(event):
    
    ser.write(b"stoph\n")
    
    
def scale_release_handle(event):
    
    ser.write(b"stoph\n")
    
def scale_release_comphan(event):
    
    ser.write(b"stopn\n")
    

# Making an interface Window    

root = Tk()

# Background colour
root['bg'] = '#0E0000'

# Interface name
root.title("Robotic_Arm_Interface")

#interface sizes
root.geometry('750x650')

# Making label for a servo motor

label_direction = Label(root, text="Directional Servo", font=("Arial", 12), bg='#0E0000', fg='white')
label_direction.pack(pady=10)

# Making a scale for servo motor

directional_scale = Scale(root, from_=0, to=180, orient=HORIZONTAL, length=700, resolution=1, command=scale_angle_direction)
directional_scale.pack(pady=10, anchor='n')
directional_scale.bind("<ButtonRelease-1>", scale_release_direction)

label_elbow = Label(root, text="Elbow Servo", font=("Arial", 12), bg='#0E0000', fg='white')
label_elbow.pack(pady=10)

# Making a scale for servo motor
elbow_scale = Scale(root, from_=0, to=180, orient=HORIZONTAL, length=700, resolution=1, command=scale_angle_elbow)
elbow_scale.pack(pady=10, anchor='n')
elbow_scale.bind("<ButtonRelease-1>", scale_release_elbow)

# Making label for a servo motor

label_compression = Label(root, text="Compression Servo", font=("Arial", 12), bg='#0E0000', fg='white')
label_compression.pack(pady=10)

# Making a scale for servo motor
compression_scale = Scale(root, from_=0, to=180, orient=HORIZONTAL, length=700, resolution=1, command=scale_angle_compression)
compression_scale.pack(pady=10, anchor='n')
compression_scale.bind("<ButtonRelease-1>", scale_release_compression)

# Making label for a servo motor

label_handle = Label(root, text="Handle Servo", font=("Arial", 12), bg='#0E0000', fg='white')
label_handle.pack(pady=10)

# Making a scale for servo motor
handle_scale = Scale(root, from_=0, to=180, orient=HORIZONTAL, length=700, resolution=1, command=scale_angle_handle)
handle_scale.pack(pady=10, anchor='n')
handle_scale.bind("<ButtonRelease-1>", scale_release_handle)

label_comphan = Label(root, text="Comphan Servo", font=("Arial", 12), bg='#0E0000', fg='white')
label_comphan.pack(pady=10)

# Making a scale for servo motor
comphan_scale = Scale(root, from_=0, to=180, orient=HORIZONTAL, length=700, resolution=1, command=scale_angle_comphan)
comphan_scale.pack(pady=10, anchor='n')
handle_scale.bind("<ButtonRelease-1>", scale_release_comphan)


# Function that running window all the time

root.mainloop()
