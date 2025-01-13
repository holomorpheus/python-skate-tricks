"""
Main Script

Created on Jul 25 2024

Author: Gabriel Martins
"""

# Local imports
from name_functions import list_fliptricks
from name_functions import list_homotopies
from flip_animation import animate_fliptrick
from homotopy_animation import animate_homotopy
from spherical_plot import sphere_flip_plot
from spherical_plot import sphere_homotopy_plot

# Showcase

## List
list_fliptricks(complete = True)
list_homotopies()

## Plot and save
sphere_flip_plot('varialkickflip', save=True, dirname='images')
sphere_homotopy_plot(('varialkickflip','inwardheelflip'), save=True, dirname='images')

## Animate and save
animate_fliptrick('varialkickflip', save=True, fps=24, dirname='videos')
animate_homotopy(('ollie','doublekickflip'))
