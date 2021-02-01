"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
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
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
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
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x = (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS) * year_index + GRAPH_MARGIN_SIZE
    return x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # Draw horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, canvas.winfo_width() - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    # Draw vertical line base on how many year's data in database
    width = CANVAS_WIDTH
    for year_index in range(len(YEARS)):
        x = get_x_coordinate(width, year_index)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[year_index], anchor=tkinter.NW)


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
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # Write your code below this line
    #################################
    width = CANVAS_WIDTH
    height = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/1000  # Divide the height of the canvas based on 1000 ranking
    for j in range(len(lookup_names)):

        # if name entered more than color we entered in COLORS, use the color in COLORS again orderly
        if j > len(COLORS) - 1:
            new_j = (j % len(COLORS))
        else:
            new_j = j

        # Draw first line and add first and second text on canvas
        # Find (x1,y1) of the first line
        x1 = get_x_coordinate(width, 0)

        # If name in first year's data, use the ranking of name as y and show the ranking
        if str(YEARS[0]) in name_data[lookup_names[j]]:
            rank_1 = name_data[lookup_names[j]][str(YEARS[0])]
            y1 = int(rank_1)*height + GRAPH_MARGIN_SIZE
            canvas.create_text(get_x_coordinate(width, 0) + TEXT_DX, y1, text=str(lookup_names[j] + rank_1),
                               anchor=tkinter.SW, fill=COLORS[new_j])
        # If name not in first year's data, use the bottom of canvas as y and show '*'
        else:
            y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            canvas.create_text(get_x_coordinate(width, 0) + TEXT_DX, y1, text=str(lookup_names[j] + '*'),
                               anchor=tkinter.SW, fill=COLORS[new_j])

        # Find (x2,y2) of the first line
        x2 = get_x_coordinate(width, 1)

        # If name in first year's data, use the ranking of name as y and show the ranking
        if str(YEARS[1]) in name_data[lookup_names[j]]:
            rank_2 = name_data[lookup_names[j]][str(YEARS[1])]
            y2 = int(rank_2)*height + GRAPH_MARGIN_SIZE
            canvas.create_text(get_x_coordinate(width, 1) + TEXT_DX, y2, text=str(lookup_names[j] + rank_2),
                               anchor=tkinter.SW, fill=COLORS[new_j])

        # If name not in second year's data, use the bottom of canvas as y and show '*'
        else:
            y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            canvas.create_text(get_x_coordinate(width, 1) + TEXT_DX, y2, text=str(lookup_names[j] + '*'),
                               anchor=tkinter.SW, fill=COLORS[new_j])
        canvas.create_line(x1, y1, x2, y2, fill=COLORS[new_j], width=LINE_WIDTH)

        # The next line we draw will use the (x2,y2) of the first line as (x1,y1)
        x1 = x2
        y1 = y2

        # Draw the following lines and add texts
        for i in range(2, len(YEARS)):
            x2 = get_x_coordinate(width, i)

            # If name in year's data, use the ranking of name as y and show the ranking
            if str(YEARS[i]) in name_data[lookup_names[j]]:
                rank_2 = name_data[lookup_names[j]][str(YEARS[i])]
                y2 = int(rank_2) * height + GRAPH_MARGIN_SIZE
                canvas.create_text(get_x_coordinate(width, i) + TEXT_DX, y2, text=str(lookup_names[j] + rank_2),
                                   anchor=tkinter.SW, fill=COLORS[new_j])

            # If name not in year's data, use the bottom of canvas as y and show '*'
            else:
                y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                canvas.create_text(get_x_coordinate(width, i) + TEXT_DX, y2, text=str(lookup_names[j] + '*'),
                                   anchor=tkinter.SW, fill=COLORS[new_j])
            canvas.create_line(x1, y1, x2, y2, fill=COLORS[new_j], width=LINE_WIDTH)

            # The next line we draw will use the (x2,y2) of the last line as (x1,y1)
            x1 = x2
            y1 = y2


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
