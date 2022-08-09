#!/usr/bin/python3

# import spacing from space_detail.py
from space_detail import plant_space
from space_detail import row_width
from space_detail import walkway_width
from space_detail import plant_per_stand

# import acres from field_area.py
from field_area import square_mtrs

# import whole acre from field_area.py
from field_area import whole_acres

# 1 meter is 100 cm 
cm_to_mtrs = 1.0e-2

# conveting centimeter to meters
plant_space_mtrs = plant_space * cm_to_mtrs
walkway_width_mtrs = walkway_width * cm_to_mtrs
row_width_mtrs = row_width * cm_to_mtrs

# calculates with meters after conversion
spacing = ((plant_space_mtrs + walkway_width_mtrs) * row_width_mtrs)

field_popullation = (square_mtrs * plant_per_stand)

# formula calculates plant population in unit acre
plant_popullation = field_popullation/spacing

# prints the total plant popullation as whole number
print("In this ", whole_acres, "acrage, the total popullation density is ", format(plant_popullation, ',.0f'), " plants.")
