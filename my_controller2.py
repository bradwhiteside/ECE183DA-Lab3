"""lab3_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Supervisor
import numpy as np
import csv
import matplotlib.pyplot as plt


# create the Robot instance.
robot = Supervisor()
segway = robot.getFromDef('robot')


# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

motor_R = robot.getDevice('motor_R')
motor_L = robot.getDevice('motor_L')
lidar_F = robot.getDevice('lidar_F')
lidar_R = robot.getDevice('lidar_R')
gyro    = robot.getDevice('gyro')
compass = robot.getDevice('compass')


lidar_F.enable(timestep)
lidar_R.enable(timestep)
gyro.enable(timestep)
compass.enable(timestep)

motor_R.setPosition(float('+inf'))
motor_L.setPosition(float('-inf'))

INPUT_FILE = "Inputs/analytic_inputs/path_7"
OUTPUT_FILE = "Output_Analytical.csv"

np.set_printoptions(precision=3)


def get_sensors():
    lidar = [0,0]
    lidar[0] = lidar_F.getValue()
    lidar[1] =  lidar_R.getValue()
                
    gyr = gyro.getValues()[0]

    comp = [0,0]        
    c = np.array(compass.getValues())
    comp = np.delete(c,1) #0,2
            
    p = np.array(segway.getPosition())
    position = np.delete(p,1)
            
    orient = segway.getOrientation()[0]
    orientation = np.degrees(orient)
    
    return lidar, gyr, comp, position, orientation
    


with open(INPUT_FILE) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    inputs = list(csvReader)
    
    data_length = len(inputs)
 

    time = np.arange(0, data_length, 0.005)
    lidar = np.zeros((data_length, 2))
    gyr = np.zeros((data_length, 1))
    comp = np.zeros((data_length, 2))
    position = np.zeros((data_length,2))
    orientation = np.zeros((data_length,1))

  
    i = 0
    print("Start")
    print(len(inputs))
    
    while robot.step(timestep) != -1 and i < 4000: 
        # print(inputs[i])
        input = inputs[i]
        inputL = float(input[0])
        inputR = float(input[1])
  
        
        motor_L.setVelocity(inputL)
        motor_R.setVelocity(inputR)
        
       
        
        
        lidar[i,:], gyr[i], comp[i,:], position[i,:], orientation[i] = get_sensors()
        i+=1
    
  
            
    print("loop done")
    plt.subplot(311)
    plt.scatter(position[:,0], 1*position[:,1])
    plt.xlabel("x(m)")
    plt.ylabel("y(m)")
    
    plt.subplot(312)
    plt.plot(position[:,0])
    plt.xlabel("t(ms)")
    plt.ylabel("x(m)")
    
    plt.subplot(313)
    plt.plot(position[:,1])
    plt.xlabel("t(ms)")
    plt.ylabel("y(m)")
    
    
    
    
    
    
    
    plt.show()

    

    
    
    # output_matrix = time
    # output_matrix = np.column_stack((output_matrix, lidar))
    # output_matrix = np.column_stack((output_matrix, gyr))
    # output_matrix = np.column_stack((output_matrix, comp))
    # output_matrix = np.column_stack((output_matrix, position))
    # output_matrix = np.column_stack((output_matrix, orientation))
    # np.savetxt(OUTPUT_FILE, output_matrix, delimiter=' ', fmt='%.4f')
    
    motor_R.setVelocity(0)
    motor_L.setVelocity(0)


