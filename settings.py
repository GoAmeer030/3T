# Imports
import copy
import sys
import random

import pygame
import numpy as np

import logging

DEBUG = False

# Constant Settings
WIDTH = 600
HEIGHT = 600

ROWS = 3
COLS = 3
SQSIZE = WIDTH // COLS

LINE_WIDTH = 15
CIRC_WIDTH = 15
CROSS_WIDTH = 20

RADIUS = SQSIZE // 4

OFFSET = 50

BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRC_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Logger Sertings
logging.basicConfig(
    level=logging.INFO if not DEBUG else logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
    if DEBUG
    else "%(asctime)s - %(message)s",
)

# PyGame Settings
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE AI")
screen.fill(BG_COLOR)
