"""lab3_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

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
motor_L.setPosition(float('+inf'))

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    motor_R.setVelocity(-3)
    motor_L.setVelocity(-2)
    
    compass_data = compass.getValues()
    lidar_F_data = lidar_F.getValue()
    
    print(compass_data)
    print(lidar_F_data)

    pass
