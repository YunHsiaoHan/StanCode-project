"""
File: babygraphics.py
Name: 雲筱涵
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui  # Graphical user interface 輸入按鈕等

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
    space = (width-2*GRAPH_MARGIN_SIZE)/len(YEARS)  # Every space between straight line
    x_value = GRAPH_MARGIN_SIZE + year_index*space  # Each year x value on graphic
    return x_value


def get_y_coordinate(height, rank):
    """
     Given the height of the canvas and the rank of the current year
    , returns the y coordinate of the vertical line associated with that year.

    Input:
        height (int): The height of the canvas
        rank (str): The rank number
    Returns:
        y_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    if rank != '*':  # Y value if rank number less than Max rank
        return GRAPH_MARGIN_SIZE+int(rank)*(height-2*GRAPH_MARGIN_SIZE)/MAX_RANK
    else:            # Y value if no rank or rank number more than Max rank
        return height-GRAPH_MARGIN_SIZE


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # Top line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    # Bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # Straight line and year text
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT,
                           width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i],
                           anchor=tkinter.NW)


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

    for i in range(len(lookup_names)):   # Loop each name in 'lookup_names' dictionary
        color = COLORS[i % len(COLORS)]  # Every name with different color line in 'COLORS' list
        name = lookup_names[i]  # Name in lookup_names list.
        year_r = name_data[name]  # (Dict) year_r is a value under name_data dict, it's key is 'name'.
        year_list = []  # To save year list in year_r dict.
        for key, val in year_r.items():
            year_list.append(key)
        rank = []  # To save each year's rank list
        for each_year in YEARS:  # Check each year in YEARS list.
            if str(each_year) not in year_list:  # If there's no year data in year_list.
                rank.append('*')                 # Add '*' to rank list.
            # If there are year data in year_list, but rank is over Max rank
            elif int(year_r[str(each_year)]) > MAX_RANK:
                rank.append('*')
            else:                                # Rank is between 1 to max rank.
                rank.append(int(year_r[str(each_year)]))  # Add rank number to list.

        x1 = get_x_coordinate(CANVAS_WIDTH, 0)         # First x value
        y1 = get_y_coordinate(CANVAS_HEIGHT, rank[0])  # First y value

        for k in range(len(YEARS)-1):  # All points after 1st point
            x2 = get_x_coordinate(CANVAS_WIDTH, k+1)    # Next x value
            y2 = get_y_coordinate(CANVAS_HEIGHT, rank[k+1])  # Next y value
            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)  # Draw rank line between years.
            # Add year and rank text next to point
            canvas.create_text(x1+TEXT_DX, y1, text=name+' '+str(rank[k]), anchor=tkinter.SW, fill=color)
            # Re-assign last point as x1, y1
            x1,y1 = x2, y2  # 沒加括號的為tuple,可直接assign
            # x1 = x2
            # y1 = y2
        # Add last point text
        canvas.create_text(x1+TEXT_DX, y1, text=name+' '+str(rank[-1]), anchor=tkinter.SW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')  # 視窗上文字
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
