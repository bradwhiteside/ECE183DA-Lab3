#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

def plot(INPUT_FILE_1, INPUT_FILE_2):
    data1 = np.loadtxt(INPUT_FILE_1, skiprows = 0)  # set skiprows to 1 if title is included
    data2 = np.loadtxt(INPUT_FILE_2, skiprows = 0)  # ^^^

    time = data1[:, 0]  # first column
    lidar1 = data1[:, 1:3]  # next two columns
    gyro1 = data1[:, 3]
    compass1 = data1[:, 4:6]
    pos1 = data1[:, 6:8]
    theta1 = data1[:, 8]

    time2 = data2[:, 0]  # first column
    lidar2 = data2[:, 1:3]  # next two columns
    gyro2 = data2[:, 3]
    compass2 = data2[:, 4:6]
    pos2 = data2[:, 6:8]
    theta2 = data2[:, 8]

    fig, axs = plt.subplots(4, 2)

    axs[0, 0].plot(time, lidar1[:, 0] / 1000, label="analytic")  # convert mm to m
    axs[0, 0].plot(time, lidar2[:, 0], label="webots")
    axs[0, 0].set_xlabel('time')
    axs[0, 0].set_ylabel('lidar readings (meters)')
    axs[0, 0].set_title("Analytic vs Webots Front Lidar")
    axs[0, 0].grid()
    axs[0, 0].legend()
    
    axs[0, 1].plot(time, lidar1[:, 1] / 1000, label="analytic")
    axs[0, 1].plot(time, lidar2[:, 1], label="webots")
    axs[0, 1].set_xlabel('time')
    axs[0, 1].set_ylabel('lidar readings (meters)')
    axs[0, 1].set_title("Analytic vs Webots Right Lidar")
    axs[0, 1].grid()
    axs[0, 1].legend()

    axs[1, 0].plot(time, compass1[:, 0], label="analytic")
    axs[1, 0].plot(time, compass2[:, 0], label="webots")
    axs[1, 0].set_xlabel('time')
    axs[1, 0].set_ylabel('compass readings [cos(theta)]')
    axs[1, 0].set_title("Analytic vs Webots Compass_X")
    axs[1, 0].grid()
    axs[1, 0].legend()

    axs[1, 1].plot(time, compass1[:, 1], label="analytic")
    axs[1, 1].plot(time, compass2[:, 1], label="webots")
    axs[1, 1].set_xlabel('time')
    axs[1, 1].set_ylabel('compass readings [sin(theta)]')
    axs[1, 1].set_title("Analytic vs Webots Compass_Y")
    axs[1, 1].grid()
    axs[1, 1].legend()

    axs[2, 0].plot(time, gyro1, label="analytic")
    axs[2, 0].plot(time, gyro2, label="webots")
    axs[2, 0].set_xlabel('time')
    axs[2, 0].set_ylabel('gyro (rad/s)')
    axs[2, 0].set_title("Analytic vs Webots Gyro")
    axs[2, 0].grid()
    axs[2, 0].legend()

    axs[2, 1].plot(time, np.degrees(theta1), label="analytic")
    axs[2, 1].plot(time, np.degrees(theta2), label="webots")
    axs[2, 1].set_xlabel('time')
    axs[2, 1].set_ylabel('theta (degrees)')
    axs[2, 1].set_title("Analytic vs Webots Theta")
    axs[2, 1].grid()
    axs[2, 1].legend()
    
    axs[3, 0].plot(time, pos1[:, 0] / 1000, label="analytic")
    axs[3, 0].plot(time, pos2[:, 0], label="webots")
    axs[3, 0].set_xlabel('time')
    axs[3, 0].set_ylabel('x position (meters)')
    axs[3, 0].set_title("Analytic vs Webots X Position")
    axs[3, 0].grid()
    axs[3, 0].legend()

    axs[3, 1].plot(time, pos1[:, 1] / 1000, label="analytic")
    axs[3, 1].plot(time, pos2[:, 1], label="webots")
    axs[3, 1].set_xlabel('time')
    axs[3, 1].set_ylabel('y position (meters)')
    axs[3, 1].set_title("Analytic vs Webots Y Position")
    axs[3, 1].grid()
    axs[3, 1].legend()

    """
    axs[3, 1].plot(pos1[:, 0] / 1000, pos1[:, 1] / 1000, label="analytic")
    axs[3, 1].plot(pos2[:, 0], pos2[:, 1], label="webots")
    axs[3, 1].set_xlabel('x position (meters)')
    axs[3, 1].set_ylabel('y position (meters)')
    axs[3, 1].set_title("Analytic vs Webots Trajectories")
    axs[3, 1].grid()
    axs[3, 1].legend()
    """

    fig.subplots_adjust(hspace=0.35)
    plt.show()