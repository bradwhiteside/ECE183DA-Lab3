import numpy as np
import matplotlib.pyplot as plt

def plot(INPUT_FILE):
    data = np.loadtxt(INPUT_FILE)
    time = data[:, 0]  # first column
    lidar = data[:, 1:3]  # next two columns
    gyro = data[:, 3]
    compass = data[:, 4:6]

    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(time, lidar[:, 0], label="front")
    axs[0, 0].plot(time, lidar[:, 1], label="right")
    axs[0, 0].set_xlabel('time')
    axs[0, 0].set_ylabel('lidar readings')
    axs[0, 0].set_title(INPUT_FILE[7:-4] + "_Lidar")
    axs[0, 0].grid()

    axs[0, 1].plot(time, gyro / (2*np.pi))
    axs[0, 1].set_xlabel('time')
    axs[0, 1].set_ylabel('gyro')
    axs[0, 1].set_title(INPUT_FILE[7:-4] + "_Gyro")
    axs[0, 1].grid()

    axs[1, 1].plot(time, np.degrees(compass[:, 0]), label="x")
    axs[1, 1].plot(time, np.degrees(compass[:, 1]), label="y")
    axs[1, 1].set_xlabel('time')
    axs[1, 1].set_ylabel('compass readings')
    axs[1, 1].set_title(INPUT_FILE[7:-4] + "_Compass")
    axs[1, 1].grid()

    fig.subplots_adjust(hspace=0.35)
    plt.show()
