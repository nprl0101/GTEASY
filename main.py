# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

import pygame
import pygame_gui
import csv
from datetime import datetime
from SWARM17 import input_simulator


def user_login():
    global ID
    ID = input("Please enter your Patient ID (Ex:Bob, Sam, John, 903x):")
    return print('Welcome to the MTR-SWARM')


user_login()
pygame.init()

pygame.display.set_caption('MTR SWARM GUI V.1')
window_surface = pygame.display.set_mode((1080, 800))

background = pygame.Surface((1080, 800))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((1080, 800))

Login = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 41.667), (110, 50)),
                                            text=ID,
                                            manager=manager)
Calibration = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((80, 95), (170, 50)),
                                            text='Begin Calibration',
                                            manager=manager)
Task = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 41.667), (160, 50)),
                                            text='Performance Task',
                                            manager=manager)
Save = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((670, 41.667), (150, 50)),
                                            text='Save last Score',
                                            manager=manager)
Logs = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((900, 41.667), (130, 50)),
                                            text='Show Log File',
                                            manager=manager)
clock = pygame.time.Clock()
is_running = True

with open(str(ID+'.csv'), mode='a') as file:
    writer = csv.writer(file, delimiter=",")

    while is_running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == Login:
                        print('Hello Patient', ID)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == Calibration:
                        print('CALIBRATED: "Number"')

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == Task:
                        print('Beginning Performance Paradigm')
                        time_taken = input_simulator()
                        writer.writerow([datetime.strftime(datetime.now(), '%b %d, %Y %H:%M:%S'), time_taken])

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == Save:
                        print('Saved! - TIME')

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == Logs:
                        print('Log Files "here"')

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()
