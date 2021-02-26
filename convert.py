import numpy as np

def input_func_1(time):
    if (time < 5):
        return -6, -1
    elif (time < 10):
        return -8, 4
    elif (time < 15):
        return -6, -2
    else:
        return -2, -8

def create_input_file_from_func(file_name, func, time_step, max_time):
    time = np.arange(0, max_time + time_step, time_step)
    inputs = np.zeros((time.shape[0], 2))
    for i in range(time.shape[0]):
        inputs[i] = func(time[i])

    np.savetxt(file_name, inputs, delimiter=' ', fmt='%.4f')