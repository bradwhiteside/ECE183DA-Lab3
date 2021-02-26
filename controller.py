import numpy as np
import csv
import yaml
import pygame
import time
from robot import Agent
from plots import plot

INPUT_FILE = "Inputs/Segway3.csv"
PARAMETER_FILE = "SegwayParameters.yml"
OUTPUT_FILE = "Output_Analytical.csv"
ENABLE_RENDERING = False

# $ pip install pygame
# code for pygame taken from this tutorial:
# https://coderslegacy.com/python/python-pygame-tutorial/
def loop(robot):
    outputFile = open(OUTPUT_FILE, "w")
    column_headers = np.array(['time', 'lidar_F', 'lidar_R',
                               'gyro', 'compass_x', 'compass_y'])
    np.savetxt(OUTPUT_FILE, column_headers)

    w = robot.width
    l = robot.length
    xOffset = robot.S[0] - (l // 2)
    yOffset = robot.S[1] - (w // 2)

    pygame.init()
    screen = pygame.display.set_mode((robot.room_width, robot.room_length))
    with open(INPUT_FILE) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        inputs = list(csvReader)

        time = np.arange(0, 20.005, 0.005)
        lidar = np.zeros((len(time), 2))
        gyro = np.zeros((len(time), 1))
        compass = np.zeros((len(time), 2))

        for i in range(len(time)):
            robot.state_update(inputs[i])

            # draw
            screen.fill((0, 0, 0))
            angle = robot.S[2] * 180 / np.pi
            surf = pygame.Surface((l, w)).convert_alpha()
            surf.fill((0, 128, 255))
            x = xOffset + robot.S[0]
            y = yOffset + robot.S[1]
            blitRotate(screen, surf, (x, y), (l // 2, w // 2), -angle)
            pygame.display.update()

        output_matrix = time
        output_matrix = np.column_stack((output_matrix, lidar))
        output_matrix = np.column_stack((output_matrix, gyro))
        output_matrix = np.column_stack((output_matrix, compass))
        np.savetxt(OUTPUT_FILE, output_matrix, delimiter=' ', fmt='%.4f')

        plot(OUTPUT_FILE)

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
    """
    Main Loop for the simulation.
    inputFile will be a csv file seperated by spaces where each line will have two integers
    between 0 and 255. These will represent the 2 inputs
    """
    # load parameters
    with open(PARAMETER_FILE) as pFile:
        P = yaml.load(pFile, Loader=yaml.FullLoader)

        init_state = [P["startingX"], P["startingY"], np.radians(P['startingAngle'])]
        robot = Agent(init_state, P['w'], P['l'], P['d'], P['roomWidth'], P['roomHeight'],
                      P['maxrpm'], P['lstddev'], P['astddev'], P['mstddev'])
        loop(robot)


if __name__ == "__main__":
    main()
