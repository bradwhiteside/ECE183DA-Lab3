import numpy as np

def get_square_error(analytical_data, webot_data):
    data1 = np.loadtxt(analytical_data, skiprows=0)  # set skiprows to 1 if title is included
    data2 = np.loadtxt(webot_data, skiprows=0)  # ^^^

    time1 = data1[:, 0]  # first column
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

    position_error = (np.square(pos1[:, 0] - pos2[:, 0]).mean(axis=0)) / np.square(time1.shape[0])
    print("Postion square meanr error:", position_error)

    orientation_error = (np.square(np.cos(theta1) - np.cos(theta2)).mean(axis=0))
    print("Orientation square meanr error:", orientation_error)

