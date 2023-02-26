"""
File: babygraphics.py
Name: Yu-Shan Cheng
--------------------------------
SC101 Baby Names Project
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt']
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    space = (width-2*GRAPH_MARGIN_SIZE)/12
    x_coordinate = GRAPH_MARGIN_SIZE+year_index*space

    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE,0,GRAPH_MARGIN_SIZE,CANVAS_HEIGHT)

    year_indices=[0,1,2,3,4,5,6,7,8,9,10,11]
    text=[1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
    for index in year_indices:
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, index), GRAPH_MARGIN_SIZE,get_x_coordinate(CANVAS_WIDTH, index), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, index) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + TEXT_DX,text=text[index], fill='black', anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    name_order = -1
    for name in lookup_names:

        name_order += 1
        color_num = len(COLORS)
        for year in YEARS:

            if year in YEARS[0:len(YEARS) - 1]:

                filename_1y = ['data/full/baby-' + str(year) + '.txt']
                name_data_1y = babynames.read_files(filename_1y)  # type: dict

                next_filename_1y = ['data/full/baby-' + str(year + 10) + '.txt']
                next_name_data_1y = babynames.read_files(next_filename_1y)  # type: dict

                if name in name_data:
                    if name in name_data_1y:

                        # TEXT
                        text_x = get_x_coordinate(CANVAS_WIDTH, (year - 1900) / 10) + TEXT_DX
                        text_y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 * int(
                            name_data[name][str(year)])
                        rank = name_data[name][str(year)]
                        canvas.create_text(text_x, text_y, text=str(name) + ' ' + str(rank),
                                           fill=COLORS[name_order % color_num],
                                           anchor=tkinter.SW)

                        # DRAW LINE

                        if name in next_name_data_1y:

                            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, (year - 1900) / 10),  # x0
                                               GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 * int(
                                                   name_data[name][str(year)]),  # y0
                                               get_x_coordinate(CANVAS_WIDTH, (year - 1900) / 10 + 1),  # x1
                                               GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 * int(
                                                   name_data[name][str(year + 10)]),  # y1
                                               fill=COLORS[name_order % color_num], width=LINE_WIDTH)

                        elif name not in next_name_data_1y:
                            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, (year - 1900) / 10),
                                               GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 * int(
                                                   name_data[name][str(year)]),
                                               get_x_coordinate(CANVAS_WIDTH, (year - 1900) / 10 + 1),
                                               CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                               fill=COLORS[name_order % color_num], width=LINE_WIDTH)

                    elif name not in name_data_1y:

                        # TEXT
                        text_x = get_x_coordinate(CANVAS_WIDTH, (year - 1900) / 10) + TEXT_DX
                        text_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + TEXT_DX
                        canvas.create_text(text_x, text_y, text=str(name) + "*", fill=COLORS[name_order % color_num],
                                           anchor=tkinter.SW)

                        if name in next_name_data_1y:
                            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, (year - 1900) / 10),
                                               CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                               get_x_coordinate(CANVAS_WIDTH, (year - 1900) / 10 + 1),
                                               GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 * int(
                                                   name_data[name][str(year + 10)]),
                                               fill=COLORS[name_order % color_num], width=LINE_WIDTH)

                        else:
                            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, (year - 1900) / 10),
                                               CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                               get_x_coordinate(CANVAS_WIDTH, (year - 1900) / 10 + 1),
                                               CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                               fill=COLORS[name_order % color_num], width=LINE_WIDTH)

                elif name not in name_data:
                    pass

            # TEXT FOR LAST YEAR
            elif year is YEARS[-1]:

                if name in name_data:
                    if name in name_data_1y:

                        # TEXT
                        text_x = get_x_coordinate(CANVAS_WIDTH, (year - 1900) / 10) + TEXT_DX
                        text_y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 * int(
                            name_data[name][str(year)])
                        rank = name_data[name][str(year)]
                        canvas.create_text(text_x, text_y, text=str(name) + ' ' + str(rank),
                                           fill=COLORS[name_order % color_num],
                                           anchor=tkinter.SW)

                    elif name not in name_data_1y:

                        # TEXT
                        text_x = get_x_coordinate(CANVAS_WIDTH, (year - 1900) / 10) + TEXT_DX
                        text_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + TEXT_DX
                        canvas.create_text(text_x, text_y, text=str(name) + "*", fill=COLORS[name_order % color_num],
                                           anchor=tkinter.SW)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
