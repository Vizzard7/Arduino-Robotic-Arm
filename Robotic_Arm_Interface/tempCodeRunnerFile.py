from tkinter import *

import serial

comPort = '/dev/cu.usbmodem1101'

ser = serial.Serial(comPort, baudrate=9600, timeout=1)

def servo_angle(angle):
    
    ser.write(f"{angle}\n".encode())
    

def scale_angle(value):
    
    servo_angle(value)
    

def scale_release_direction(event):
    
    ser.write(b"stopd\n")
    
def scale_release_elbow(event):
    
    ser.write(b"stope\n")
    
root = Tk()

root['bg'] = '#0E0000'

root.title("Robotic_Arm_Interface")

root.geometry('750x550')

label_direction = Label(root, text="Directional Servo", font=("Arial", 12), bg='#0E0000', fg='white')

label_direction.pack(pady=10)

directional_scale = Scale(root, from_=0, to=180, orient=HORIZONTAL, length=700,  resolution=1, command=scale_angle)

directional_scale.pack(pady=10, anchor='n')

directional_scale.bind("<ButtonRelease-1>", scale_release_direction)


label_elbow = Label(root, text="Elbow Servo", font=("Arial", 12), bg='#0E0000', fg='white')

label_elbow.pack(pady=10)

elbow_scale = Scale(root, from_=0, to=180, orient=HORIZONTAL, length=700,  resolution=1, command=scale_angle)

elbow_scale.pack(pady=10, anchor='n')

elbow_scale.bind("<ButtonRelease-1>", scale_release_elbow)



root.mainloop()








    
    
    
    
    
    
    

    
    



