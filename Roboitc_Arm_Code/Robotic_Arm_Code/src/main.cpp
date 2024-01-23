
// Include Arduino library 
#include <Arduino.h>

// Include Servo Library
#include <Servo.h>

// Creating a Servo Control Object

Servo directional;
Servo elbow;

Servo compression;
Servo handle;

Servo comphan;

// Making variables to store an angle

int start_angle_direction = 0;

int start_angle_elbow = 0;

int start_angle_compression = 0;

int start_angle_handle = 0;

int start_angle_comphan = 0;

// Function that stop a motor


void stop_motor(Servo motor, int &previous_angle, int arduino_pin) {

  previous_angle = motor.read(); 

  motor.detach();

  delay(500);

  motor.attach(arduino_pin, previous_angle, 1000);
}

void setup() {

  // Attach all the servos' to pins

  directional.attach(10);

  elbow.attach(11);

  compression.attach(9);

  // Open a serial communication port to communicate with the interface

  Serial.begin(9600);

  handle.attach(6);

  comphan.attach(5);

  


}

void loop() {

  // If this port is availbale go futher.

  if (Serial.available() > 0) {

    // Getting information from the port

    String port_input = Serial.readStringUntil('\n');

    // Conditions for stopping a motor

    if (port_input.startsWith("stopd")) {

      stop_motor(directional, start_angle_direction, 10);

    } 

    else if (port_input.startsWith("stope")) {

      stop_motor(elbow, start_angle_elbow, 11);
    } 
    

    else if(port_input.startsWith("stopc")) {

       stop_motor(compression, start_angle_compression, 9);

    }

    else if(port_input.startsWith("stoph")) {

      stop_motor(handle, start_angle_handle, 6);

    }

    else if(port_input.startsWith("stopn")) {

      stop_motor(comphan, start_angle_comphan, 5);

    }

    

    else {

      int angle_direction, angle_elbow, angle_compression, angle_handle, angle_comphan;

      // Reading data from a string according to the format

      sscanf(port_input.c_str(), "%d,%d,%d,%d,%d", &angle_direction, &angle_elbow, &angle_compression, &angle_handle, &angle_comphan);

      // Conditions for sending angle to the servo motor

      if (angle_direction != start_angle_direction) {

        directional.write(angle_direction);

        start_angle_direction = angle_direction;

      }

      if (angle_elbow != start_angle_elbow) {

        elbow.write(angle_elbow);

        start_angle_elbow = angle_elbow;

      }

      if (angle_compression != start_angle_compression) {

        compression.write(angle_compression);

        start_angle_compression = angle_compression;

      }

      if (angle_handle != start_angle_handle) {

        handle.write(angle_handle);

        start_angle_handle = angle_handle;

      }

      if (angle_comphan != start_angle_comphan) {

        comphan.write(angle_comphan);

        start_angle_comphan = angle_comphan;

      }





    }
  }
}
