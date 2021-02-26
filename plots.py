import numpy as np
import matplotlib.pyplot as plt


def plot(INPUT_FILE):
    data = np.loadtxt(INPUT_FILE)
    time = data[:, 0]  # first column
    states = data[:, 1:3]  # next two columns x,y
    displacement = data[:, 3:5]
    angular_displacement = data[:, 5:6]
    angular_velocity = data[:, 6:7]
    wheel_angular_velocity = data[:, 7:9]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(states[:, 0], states[:, 1])
    plt.xlabel('x mm')
    plt.ylabel('y mm')
    plt.title(INPUT_FILE[7:-4] + "_Simulation")
    plt.grid()
    ax.set_aspect('equal', adjustable='box')

    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(time, displacement[:, 0], label="x")
    axs[0, 0].plot(time, displacement[:, 1], label="y")
    axs[0, 0].set_xlabel('time')
    axs[0, 0].set_ylabel('mm')
    axs[0, 0].set_title(INPUT_FILE[7:-4] + "_Displacement")
    axs[0, 0].grid()

    axs[0, 1].plot(time, np.degrees(angular_displacement))
    axs[0, 1].set_xlabel('time')
    axs[0, 1].set_ylabel('degrees')
    axs[0, 1].set_title(INPUT_FILE[7:-4] + "_Angular_Displacement")
    axs[0, 1].grid()

    axs[1, 0].plot(time, np.degrees(angular_velocity))
    axs[1, 0].set_xlabel('time')
    axs[1, 0].set_ylabel('degrees/sec')
    axs[1, 0].set_title(INPUT_FILE[7:-4] + "_Angular_Velocity")
    axs[1, 0].grid()

    axs[1, 1].plot(time, np.degrees(wheel_angular_velocity[:, 0]), label="left")
    axs[1, 1].plot(time, np.degrees(wheel_angular_velocity[:, 1]), label="right")
    axs[1, 1].set_xlabel('time')
    axs[1, 1].set_ylabel('degrees/sec')
    axs[1, 1].set_title(INPUT_FILE[7:-4] + "_Wheel_Angular_Displacement")
    axs[1, 1].grid()

    fig.subplots_adjust(hspace=0.35)
    plt.show()
