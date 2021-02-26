"""lab3_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Supervisor

import csv


# create the Robot instance.

robot = Supervisor()
segway = robot.getFromDef('robot')

# robot getFromDevice('robot')
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

# outputFile = open("output_python.csv", "w")
# OUTPUT_FILE = "segway_output.csv"
# outputFile = open(OUTPUT_FILE, "w")

while robot.step(timestep) != -1:

    motor_R.setVelocity(5)
    motor_L.setVelocity(5)
    
    compass_data = compass.getValues()
    lidar_F_data = lidar_F.getValue()
    position = segway.getPosition()
    # outputFile.write(compass_data)
    
    # print(compass_data)
    # print(lidar_F_data)
    print(position)

    pass
