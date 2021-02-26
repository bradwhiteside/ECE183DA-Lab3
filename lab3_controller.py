#!/usr/bin/python
"""lab3_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Supervisor
import numpy as np




import csv


# create the Robot instance.

robot = Supervisor()
segway = robot.getFromDef('robot')


# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())



motor_R = robot.getDevice('motor_R')
motor_L = robot.getDevice('motor_L')
lidar_F = robot.getDevice('lidar_F')
lidar_R = robot.getDevice('lidar_R')
gyro = robot.getDevice('gyro')
compass = robot.getDevice('compass')


lidar_F.enable(timestep)
lidar_R.enable(timestep)
gyro.enable(timestep)
compass.enable(timestep)

motor_R.setPosition(float('+inf'))
motor_L.setPosition(float('-inf'))


OUTPUT_FILE = "segway_output.txt"
outputFile = open(OUTPUT_FILE, "w")

robot_true_state = list()
i = 0
while robot.step(timestep) != -1 and i <100:
    i += 1
    print(i)
    motor_R.setVelocity(5)
    motor_L.setVelocity(5)
    
    compass_data = compass.getValues()
    lidar_F_data = lidar_F.getValue()
    position = segway.getPosition()
    robot_true_state.append(position)
    
    # print(compass_data)
    # print(lidar_F_data)
    # print(position)
    
    pass
    
    
motor_R.setVelocity(0)
motor_L.setVelocity(0)

robot_true_state = np.array(robot_true_state)
outputFile.write(str(robot_true_state))
outputFile.close()

print(robot_true_state.shape)