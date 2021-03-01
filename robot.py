#!/usr/bin/python
import numpy as np
import math


def L2_norm(a, b):
    return math.sqrt((a ** 2) + (b ** 2))


def get_distance(x, y, W, L, theta):
    # bound theta between 0 and 2 pi
    theta = theta % (2 * np.pi)
    if theta < 0:
        theta = (2 * np.pi) - theta

    # avoid invalid inputs for tan() and cot()
    if theta == 0:
        return W - x
    elif theta == (1 / 2) * np.pi:
        return L - y
    elif theta == np.pi:
        return x
    elif theta == (3 / 2) * np.pi:
        return y

    # determine lengths of legs of two possible triangles
    if theta < (1 / 2) * np.pi:             # quadrant I
        b1 = L - y
        a1 = b1 * (1 / math.tan(theta))
        a2 = W - x
        b2 = a2 * math.tan(theta)
    elif theta < np.pi:                     # quadrant II
        b1 = L - y
        a1 = b1 * (1 / math.tan(theta))
        a2 = x
        b2 = a2 * math.tan(theta)
    elif theta < (3 / 2) * np.pi:           # quadrant III
        a1 = x
        b1 = a1 * math.tan(theta)
        b2 = y
        a2 = b2 * (1 / math.tan(theta))
    else:                                   # quadrant IV
        a1 = W - x
        b1 = a1 * math.tan(theta)
        b2 = y
        a2 = b2 * (1 / math.tan(theta))

    # shorter of the hypotenuses of the two triangles is the lidar reading
    return min(L2_norm(a1, b1), L2_norm(a2, b2))


class Agent:
    def __init__(self, init_state=[0, 0, 0], w=530, l=682, d=502, rw=10000, rl=10000, maxrpm=130, lstddev=0.03,
                 astddev=8,
                 mstddev=1):
        self.S = np.reshape(np.array(init_state), (3, 1))
        self.width = w
        self.length = l
        self.diameter = d
        self.room_width = rw  # x-direction
        self.room_length = rl  # y-direction
        self.delta_t = 0.005
        self.wl = 0
        self.wr = 0
        self.MAXRPM = maxrpm
        self.lidarStdDev = lstddev  # = 3%
        self.accelerometerStdDev = astddev  # = 8 mg-rms
        self.magnetometerStdDev = mstddev
        self.PWM_std = [0, 0]
        self.Wheel_std = [0, 0]

    def PWM_to_RPM(self, x):
        s = np.sign(x)
        k = 0.05
        if (np.abs(x) > 100):
            return self.MAXRPM * s

        return self.MAXRPM * s * np.exp(s * k * x) / (np.exp(k * 100))

    def DPS_RadS(self, x):
        return x * np.pi / 180

    # Convert the angle to -pi tp pi range
    def pi_2_pi(self, a):
        return (a + np.pi) % (2 * np.pi) - np.pi

    def state_update(self, PWM_signal):
        '''
        Moving to the next step given the input u
        return : s
        '''
        u = [0, 0]
        k_l = 1
        k_r = 1

        # u[0] = self.PWM_to_RPM(float(PWM_signal[0]) + np.random.normal(0,self.PWM_std[0])) + np.random.normal(0,self.Wheel_std[0])
        # u[1] = self.PWM_to_RPM(float(PWM_signal[1]) + np.random.normal(0,self.PWM_std[1])) + np.random.normal(0,self.Wheel_std[1])
        # self.wl = self.DPS_RadS(float(PWM_signal[0])) +  np.random.normal(0,self.Wheel_std[0])
        # self.wr = self.DPS_RadS(float(PWM_signal[1])) + np.random.normal(0,self.Wheel_std[1])
        self.wl = float(PWM_signal[0])
        self.wr = float(PWM_signal[1])

        # self.wl = self.MAXRPM * (np.pi / 30) * (u[0] / 100)  # + np.random.normal(0, self.PWM_std[0])
        # self.wr = self.MAXRPM * (np.pi / 30) * (u[1] / 100)  # + np.random.normal(0, self.PWM_std[1])
        # v = u[0]
        # ommega = u[1]
        u = np.vstack((self.wl, self.wr))

        B = np.array([[np.cos(self.S[2, 0]), 0],
                      [np.sin(self.S[2, 0]), 0],
                      [0, 1]])

        Dynamixs = np.array([[self.diameter / 4, self.diameter / 4],
                             [-self.diameter / (2 * self.width), self.diameter / (2 * self.width)]])

        self.S = + self.S + (B @ Dynamixs @ u) * self.delta_t
        self.S[2, 0] = self.pi_2_pi(self.S[2, 0])

        return self.S

    def get_lidar_readings(self):
        front_lidar = \
            get_distance(self.S[0], self.S[1], self.room_width,
                         self.room_length, self.S[2] + np.pi)
        right_lidar = \
            get_distance(self.S[0], self.S[1], self.room_width,
                         self.room_length, self.S[2] - (np.pi / 2))
        return np.random.normal(front_lidar, abs(front_lidar * self.lidarStdDev)), \
               np.random.normal(right_lidar, abs(right_lidar * self.lidarStdDev))

    def get_IMU_velocity(self):
        omega = ((self.wl - self.wr) / self.width) * (self.diameter / 2)
        return np.random.normal(omega, abs(omega * self.accelerometerStdDev))

    def get_IMU_position(self):
        x = math.cos(self.S[2, 0])
        y = math.sin(self.S[2, 0])
        return np.random.normal(x, abs(x * self.magnetometerStdDev)), \
               np.random.normal(y, abs(y * self.magnetometerStdDev))

    def get_observation(self):
        # do the sensor output readings here
        L = self.get_lidar_readings()
        velocity = self.get_IMU_velocity()
        pos = self.get_IMU_position()
        return L[0], L[1], velocity, pos[0], pos[1]
