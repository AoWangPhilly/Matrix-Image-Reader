from dearpygui.core import *
from dearpygui.simple import * 
from read_matrix import draw_borders

# Window object settings
set_main_window_size(540, 720)
set_global_font_scale(1.25)
set_theme('Dark') # Dark, Dark 2 

with window('Matrix Image Reader', width=520, height=677):
    print('GUI is RUNNING')
    set_window_pos('Matrix Image Reader', 0, 0)
start_dearpygui()