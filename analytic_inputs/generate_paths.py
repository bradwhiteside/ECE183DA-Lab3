#!/usr/bin/python
import numpy as np

# def input_func_1(time):
#     if (time < 5):
#         return -6, -1
#     elif (time < 10):
#         return -8, 4
#     elif (time < 15):
#         return -6, -2
#     else:
#         return -2, -8

def path_spin(time):
    if time < 10000:
        return 1, -1
    else:
        return -1, -1

def path_turn(time):
    return -2, -1

def path_S1_ABCD(time):
    if time < 5000:
        return -6, -1
    elif time < 10000:
        return -8, 4
    elif time < 15000:
        return -6, -2
    else:
        return -2, -8

def path_S2(time):
    if time < 4000:
        return -1, -8
    elif time < 8000:
        return -4, -4
    elif time < 12000:
        return 6, -6
    elif time < 16000:
        return -6, -6
    else:
        return -6, -1

def path_S3(time):
    if time < 4000:
        return -8, -8
    elif time < 8000:
        return 8, -8
    elif time < 12000:
        return -4, -4
    elif time < 16000:
        return -1, -6
    else:
        return -1, -4

def path_S10_ABCD(time):
    if time < 4000:
        return -2, -2
    elif time < 8000:
        return 2, -2
    elif time < 12000:
        return -3, -3
    elif time < 16000:
        return -1, -4
    else:
        return -1, -2

def path_S11(time):
    if time < 4000:
        return -1, -2
    elif time < 8000:
        return 1, -2
    elif time < 12000:
        return -4, -1
    elif time < 16000:
        return -1, -4
    else:
        return -1, -2

def path_S12(time):
    if time < 4000:
        return -6, -1
    elif time < 8000:
        return 4, -4
    elif time < 12000:
        return -1, -3
    elif time < 16000:
        return -1, -2
    else:
        return -2, -2

def path_P1_ABCD(time):
    if time < 4000:
        return -2, -2
    elif time < 8000:
        return 2, -2
    elif time < 12000:
        return -3, -3
    elif time < 16000:
        return -1, -4
    else:
        return -1, -3

def path_P2(time):
    if time < 4000:
        return -1, -4
    elif time < 8000:
        return -2, -2
    elif time < 12000:
        return 3, -3
    elif time < 16000:
        return -1, -2
    else:
        return -3, -1

def path_P3(time):
    if time < 4000:
        return -1, -2
    elif time < 8000:
        return -1, -4
    elif time < 12000:
        return -3, -3
    elif time < 16000:
        return -4, -1
    else:
        return -2, -1

def path_P10_ABCD(time):
    if time < 4000:
        return -2, -2
    elif time < 8000:
        return 2, -2
    elif time < 12000:
        return -3, -3
    elif time < 16000:
        return -1, -4
    else:
        return -1, -2

def path_P11(time):
    if time < 4000:
        return -1, -2
    elif time < 8000:
        return 1, -2
    elif time < 12000:
        return -4, -1
    elif time < 16000:
        return -1, -4
    else:
        return -1, -2

def path_P12(time):
    if time < 4000:
        return -6, -1
    elif time < 8000:
        return 4, -4
    elif time < 12000:
        return -1, -3
    elif time < 16000:
        return -1, -2
    else:
        return -2, -2

def path_4(time):
    if time < 10000:
        return 1, 1
    else:
        return -1, -3

def path_5(time):
    if time < 5000:
        return 1, 2
    elif time < 10000:
        return -1, -2
    else:
        return -1, -1

def path_6(time):
    if time < 5000:
        return 0, 2
    elif time < 10000:
        return 2, 0
    else:
        return -1, -1

def path_7(time):
    if time < 5000:
        return 1, -1
    elif time < 10000:
        return 1, 1
    elif time < 15000:
        return -5, -1
    else:
        return -1, -5

def path_8(time):
    if time < 5000:
        return -1, -1
    elif time < 10000:
        return 1, 1
    elif time < 15000:
        return -2, -2
    else:
        return 2, 2

def path_9(time):
    if time < 15000:
        return -1, -5
    else:
        return 5, 1

def path_13(time):
    if time < 5000:
        return 1, 1
    elif time < 10000:
        return 2, -2
    else:
        return -1, -1

def path_14(time):
    if time < 5000:
        return -2, -1
    elif time < 10000:
        return 2, 2
    else:
        return -1, -2

def path_15(time):
    if time < 5000:
        return -2, -2
    elif time < 10000:
        return 1, 1
    else:
        return -1, -3

def path_16(time):
    if time < 8000:
        return 2, 2
    elif time < 12000:
        return -3, -2
    else:
        return -1, -3

def path_17(time):
    if time < 4000:
        return -2, -2
    elif time < 8000:
        return 5, 2
    else:
        return -5, -1

def path_18(time):
    if time < 10000:
        return -1, -5
    else:
        return -5, -1

def create_input_file_from_func(file_name, func, time_step, max_time):
    time = np.arange(0, max_time + time_step, time_step)
    inputs = np.zeros((time.shape[0], 2))
    for i in range(time.shape[0]):
        values = func(time[i])
        inputs[i] = [values[0],values[1]] # scale paths to account for webots vs python differences

    np.savetxt(file_name, inputs, delimiter=',', fmt='%.4f')

def main():
    paths = [path_spin, path_turn, path_S1_ABCD, path_S2, path_S3, path_S10_ABCD, path_S11, path_S12, path_P1_ABCD, path_P2, path_P3, path_P10_ABCD, path_P11, path_P12, path_4, path_5, path_6, path_7, path_8, path_9, path_13, path_14, path_15, path_16, path_17, path_18]
    for func in paths:
        create_input_file_from_func(func.__name__, func, 5, 20000)

if __name__ == "__main__":
    main()