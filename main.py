#!/usr/bin/env python

import pyautogui

max_rows = 4

def convert_to_coord(num: int) -> tuple:
    return (num % 3, num // 3)

def grid_to_pixel(grid_coord: tuple) -> tuple:
    base_x, base_y = 1720, 545
    offset_x, offset_y = 195, 120
    x = base_x + grid_coord[0] * offset_x
    y = base_y + grid_coord[1] * offset_y
    return x, y

for first in range(max_rows * 3):
    for second in range(first + 1, max_rows * 3):
        for third in range(second + 1, max_rows * 3):
            x, y = grid_to_pixel(convert_to_coord(first))
            pyautogui.click(x, y)
            x, y = grid_to_pixel(convert_to_coord(second))
            pyautogui.click(x, y)
            x, y = grid_to_pixel(convert_to_coord(third))
            pyautogui.click(x, y)
