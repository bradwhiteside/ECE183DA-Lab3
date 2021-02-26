#!/usr/bin/python
import numpy as np
import csv
import yaml
import pygame
import time
from robot import Agent
from plots import plot

PAPERBOT_INPUT_FILES = \
    ["analytic_inputs/path_P2", "analytic_inputs/path_P3", "analytic_inputs/path_4", "analytic_inputs/path_5",
     "analytic_inputs/path_6", "analytic_inputs/path_7", "analytic_inputs/path_8", "analytic_inputs/path_9",
     "analytic_inputs/path_P11", "analytic_inputs/path_P12", "analytic_inputs/path_13", "analytic_inputs/path_14",
     "analytic_inputs/path_15", "analytic_inputs/path_16", "analytic_inputs/path_17", "analytic_inputs/path_18"]
PAPERBOT_COMPARISON_FILES = \
    ["webots_outputs/P2.txt", "webots_outputs/P3.txt", "webots_outputs/P4.txt", "webots_outputs/P5.txt", "webots_outputs/P6.txt",
     "webots_outputs/P7.txt", "webots_outputs/P8.txt", "webots_outputs/P9.txt", "webots_outputs/P11.txt", "webots_outputs/P12.txt",
     "webots_outputs/P13.txt", "webots_outputs/P14.txt", "webots_outputs/P15.txt", "webots_outputs/P16.txt", "webots_outputs/P17.txt",
     "webots_outputs/P18.txt"]
PAPERBOT_PLOT_NAMES = \
    ["Paperbot2", "Paperbot3", "Paperbot4", "Paperbot5", "Paperbot6", "Paperbot7", "Paperbot8", "Paperbot9", "Paperbot11",
     "Paperbot12", "Paperbot13", "Paperbot14", "Paperbot15", "Paperbot16", "Paperbot17", "Paperbot18"]

SEGWAY_INPUT_FILES = \
    ["analytic_inputs/path_S2", "analytic_inputs/path_S3", "analytic_inputs/path_4", "analytic_inputs/path_5",
     "analytic_inputs/path_6", "analytic_inputs/path_7", "analytic_inputs/path_8", "analytic_inputs/path_9",
     "analytic_inputs/path_S11", "analytic_inputs/path_S12", "analytic_inputs/path_13", "analytic_inputs/path_14",
     "analytic_inputs/path_15", "analytic_inputs/path_16", "analytic_inputs/path_17", "analytic_inputs/path_18"]
SEGWAY_COMPARISON_FILES = \
    ["webots_outputs/S2.txt", "webots_outputs/S3.txt", "webots_outputs/S4.txt", "webots_outputs/S5.txt", "webots_outputs/S6.txt",
     "webots_outputs/S7.txt", "webots_outputs/S8.txt", "webots_outputs/S9.txt", "webots_outputs/S11.txt", "webots_outputs/S12.txt",
     "webots_outputs/S13.txt", "webots_outputs/S14.txt", "webots_outputs/S15.txt", "webots_outputs/S16.txt", "webots_outputs/S17.txt",
     "webots_outputs/S18.txt"]
SEGWAY_PLOT_NAMES = \
    ["Segway2", "Segway3", "Segway4", "Segway5", "Segway6", "Segway7", "Segway8", "Segway9", "Segway11",
     "Segway12", "Segway13", "Segway14", "Segway15", "Segway16", "Segway17", "Segway18"]

PARAMETER_FILE = "PaperbotParameters.yml"

# $ pip install pygame
# code for pygame taken from this tutorial:
# https://coderslegacy.com/python/python-pygame-tutorial/
def loop(robot, input_file, comparison_file, plot_name):
    output_file = "analytic_outputs/" + plot_name + ".csv"
    outputFile = open(output_file, "w")
    """column_headers = np.array(['time', 'lidar_F', 'lidar_R',
                               'gyro', 'compass_x', 'compass_y'])
    np.savetxt(OUTPUT_FILE, column_headers)"""

    w = robot.width
    l = robot.length
    xOffset = robot.S[0] - (l // 2)
    yOffset = robot.S[1] - (w // 2)

    #pygame.init()
    #screen = pygame.display.set_mode((robot.room_width, robot.room_length))
    with open(input_file) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        inputs = list(csvReader)

        time = np.arange(0, 20.005, 0.005)
        lidar = np.zeros((len(time), 2))
        gyro = np.zeros((len(time), 1))
        compass = np.zeros((len(time), 2))
        position = np.zeros((len(time), 3))

        for i in range(len(time)):
            try:
                robot.state_update(inputs[i])
            except IndexError:
                break
            data = robot.get_observation()
            lidar[i] = data[:2]
            gyro[i] = data[2]
            compass[i] = np.array(data[3:])
            position[i] = robot.S.reshape((3,))

            """# draw
            screen.fill((0, 0, 0))
            angle = robot.S[2] * 180 / np.pi
            surf = pygame.Surface((l, w)).convert_alpha()
            surf.fill((0, 128, 255))
            x = xOffset + robot.S[0]
            y = yOffset + robot.S[1]
            blitRotate(screen, surf, (x, y), (l // 2, w // 2), -angle)
            pygame.display.update() """

        output_matrix = time
        output_matrix = np.column_stack((output_matrix, lidar))
        output_matrix = np.column_stack((output_matrix, gyro))
        output_matrix = np.column_stack((output_matrix, compass))
        output_matrix = np.column_stack((output_matrix, position))
        np.savetxt(output_file, output_matrix, delimiter=' ', fmt='%.4f')

        plot(output_file, comparison_file, plot_name)

# adjust coords so the surface rotates about its center
# https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame
def blitRotate(surf, image, pos, originPos, angle):
    # calcaulate the axis aligned bounding box of the rotated image
    w, h = image.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot
    pivot = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, (origin[0][0], origin[1][0]))


def main():
    PAPERBOT_SIM = True

    if PAPERBOT_SIM:
        with open("PaperbotParameters.yml") as pFile:
            P = yaml.load(pFile, Loader=yaml.FullLoader)

            init_state = [P["startingX"], P["startingY"], np.radians(P['startingAngle'])]

            for i in range(len(PAPERBOT_INPUT_FILES)):
                robot = Agent(init_state, P['w'], P['l'], P['d'], P['roomWidth'], P['roomHeight'],
                              P['maxrpm'], P['lstddev'], P['astddev'], P['mstddev'])
                loop(robot, PAPERBOT_INPUT_FILES[i], PAPERBOT_COMPARISON_FILES[i], PAPERBOT_PLOT_NAMES[i])

    if not PAPERBOT_SIM:
        with open("SegwayParameters.yml") as pFile:
            P = yaml.load(pFile, Loader=yaml.FullLoader)
        
            init_state = [P["startingX"], P["startingY"], np.radians(P['startingAngle'])]
        
            for i in range(len(SEGWAY_INPUT_FILES)):
                robot = Agent(init_state, P['w'], P['l'], P['d'], P['roomWidth'], P['roomHeight'],
                              P['maxrpm'], P['lstddev'], P['astddev'], P['mstddev'])
                loop(robot, SEGWAY_INPUT_FILES[i], SEGWAY_COMPARISON_FILES[i], SEGWAY_PLOT_NAMES[i])

if __name__ == "__main__":
    main()
