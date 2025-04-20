from PIL import Image, ImageDraw 
import math

# Inputs
BIRTH_YEAR = 1994
BIRTH_MONTH = 5
BIRTH_DAY = 19

# Calendar settings
HOLE_DIA_MM = 2.38125 # 3/32 in
HOLE_SPACING_MM = 3
SECTION_GAP_FACTOR = 2 # value of 1 means no additional gap between sections
SIDE_MARGINS_MM = 25
VERT_MARGINS_MM = 25
NUMBERS_MARGIN_FACTOR = 2
MONTHS_MARGIN_FACTOR = 2
DOTS_PER_ROW_MO = 8
TOTAL_YEARS = 85
LIFE_SECTIONS = [15, 25, 35, 45, 55, 65, 75]

# Image settings
PX_PER_MM = 10

# Derived constants
MONTH_WIDTH_MM = HOLE_SPACING_MM * (DOTS_PER_ROW_MO - 1 + SECTION_GAP_FACTOR)
MONTH_HEIGHT_MM = HOLE_SPACING_MM * (math.ceil(31 / DOTS_PER_ROW_MO) - 1 + SECTION_GAP_FACTOR)
LIFE_SECTION_ADD_GAP = HOLE_SPACING_MM * SECTION_GAP_FACTOR * (SECTION_GAP_FACTOR - 1)

def add_day(x_mm, y_mm, x1_mm, y1_mm):
    x = x_mm * PX_PER_MM
    y = y_mm * PX_PER_MM
    x1 = x1_mm * PX_PER_MM
    y1 = y1_mm * PX_PER_MM
    draw.ellipse(xy = (x, y, x1, y1),
                            outline = (0, 0, 0),
                            fill = (0, 0, 0),
                            width = 0)

# Form background image
w_mm = (1 + NUMBERS_MARGIN_FACTOR) * SIDE_MARGINS_MM + MONTH_WIDTH_MM * 12
h_mm = (1 + MONTHS_MARGIN_FACTOR) * VERT_MARGINS_MM + MONTH_HEIGHT_MM * TOTAL_YEARS + len(LIFE_SECTIONS) * LIFE_SECTION_ADD_GAP
w_in, h_in = 0.03937 * w_mm, 0.03937 * h_mm
print(f'width (in): {w_in:.2f} \nheight (in): {h_in:.2f}')
w_px = w_mm * PX_PER_MM
h_px = h_mm * PX_PER_MM
img = Image.new('RGB', (w_px,h_px), color=(71,95,122))

# Creating a Draw object 
draw = ImageDraw.Draw(img) 

# Draw dots
first_year = True
for k in range(TOTAL_YEARS):
    cur_year = k + BIRTH_YEAR
    day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] if cur_year % 4 != 0 else [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for m, days in enumerate(day_list):
        cur_total_life_section_gap = len([1 for x in LIFE_SECTIONS if k > x - 1]) * LIFE_SECTION_ADD_GAP
        x0, y0 = SIDE_MARGINS_MM * NUMBERS_MARGIN_FACTOR + m * MONTH_WIDTH_MM, VERT_MARGINS_MM * MONTHS_MARGIN_FACTOR + k * MONTH_HEIGHT_MM + cur_total_life_section_gap
        for i in range(days):
            x = x0 + (i % DOTS_PER_ROW_MO) * HOLE_SPACING_MM
            y = y0 + i // DOTS_PER_ROW_MO * HOLE_SPACING_MM
            x1 = x + HOLE_DIA_MM
            y1 = y + HOLE_DIA_MM
            if not first_year or m > BIRTH_MONTH - 1 or (m == BIRTH_MONTH - 1 and i >= BIRTH_DAY - 1):
                add_day(x, y, x1, y1)
    first_year = False
  
# Method to display the modified image 
img.show() 