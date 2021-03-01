import numpy as np

def get_square_error(analytical_data, webot_data, plot_name):
    data1 = np.loadtxt(analytical_data, skiprows=0)  # set skiprows to 1 if title is included
    data2 = np.loadtxt(webot_data, skiprows=0)  # ^^^

    time1 = data1[:, 0]  # first column
    lidar1 = data1[:, 1:3]/1000  # next two columns
    gyro1 = data1[:, 3]
    compass1 = data1[:, 4:6]
    pos1 = data1[:, 6:8]/1000
    theta1 = data1[:, 8]

    time2 = data2[:, 0]  # first column
    lidar2 = data2[:, 1:3]  # next two columns
    gyro2 = data2[:, 3]
    compass2 = data2[:, 4:6]
    pos2 = data2[:, 6:8]
    theta2 = data2[:, 8]

    # position_error = np.mean((np.sum((np.abs(pos1 - pos2))/pos1 , axis = 0)/len(pos1))*100)
    # print(f'{position_error:.3f}%')

    orientation_error = (np.square(np.cos(theta1) - np.cos(theta2)).mean(axis=0))
    print(f'{orientation_error:.3f}%')

