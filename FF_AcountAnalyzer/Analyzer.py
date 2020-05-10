import os
import numpy as np
import pandas as pd
import datetime
import tkinter as tk
from .FF_File import FF_File as File
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class Application():

    # CLASS VARIABLES
    root = None # tkinter root
    text_fileName = None # display file name after file chosen
    button_file_chooser = None # button to initiate file dialog
    file = None # file that user chooses
    screen_width = None # width of user's screen
    screen_height = None # height of user's screen
    frame_charts = None # holds charts that visualize data from file
    date_start = None
    date_end = None

    # CLASS CONSTANTS


    def __init__(self):
        '''
        starting point of app
        :return: N/A
        '''

        # create GUI root
        self.root = tk.Tk()
        self.root.title(string="First Financial Checking Account Data Analyzer")
        self.screen_height, self.screen_width = self.root.winfo_screenheight(), self.root.winfo_screenwidth() # grab screen dimensions
        self.root.state('zoomed') # set full screen, with title bar.

        # attach button for file dialog
        self.button_file_chooser = tk.Button(self.root, text='Choose file', command=self.get_file_path)
        self.button_file_chooser.pack()

        # attach Text field for initial date range
        self.text_initial_date = tk.Text(self.root, '01/01/2020')
        self.text_initial_date.pack()

        # attach text to display file path
        self.text_fileName = tk.Label(self.root, text='')
        self.text_fileName.pack()

        # Frame for charting area
        self.frame_charts = tk.Frame(self.root)
        self.frame_charts.pack()

        # attach button to do analysis
        #self.button_analyze = tk.Button(self.root, text='Analyze Data', command=self.analyze)
        #self.button_analyze.pack()

        # start GUI loop
        self.root.mainloop()

    def update_GUI(self):
        '''
        Updates GUI with current variable values
        :return: N/A
        '''
        if self.file is not None:
            # update display text to show file name
            self.text_fileName.config(text=self.file.get_file_name())
            self.render_charts()
        else:
            print('file was none')

    def get_file_path(self):
        '''
        1. opens file dialog for user to choose their file
        2. stores
        :return: N/A
        '''
        # grab chosen file path from dialog and refresh GUI
        analysis_file_path = filedialog.askopenfilename()
        self.file = File(analysis_file_path)
        self.update_GUI()

    def render_charts(self):
        df_file_contents = self.file.get_file_contents()

        # chart 1
        x_axis_data = df_file_contents['Post Date'].tolist()[::-1]
        y_axis_data = df_file_contents['Balance'].tolist()[::-1]
        chart1 = Chart(self.root, 'Balance Over Time', x_axis_data, y_axis_data)

        # chart 2
        x_axis_data2 = df_file_contents['Post Date'].tolist()[::-1]
        y_axis_data2 = df_file_contents['Credit'].tolist()[::-1]
        chart2 = Chart(self.root, 'Inflow', x_axis_data2, y_axis_data2)

        chart1.pack()
        chart2.pack()


class Chart(tk.Frame):

    chart_title = ''

    def __init__(self, parent, chart_title, lis_x_axis_data, lis_y_axis_data):
        tk.Frame.__init__(self, parent)

        self.chart_title = chart_title

        # init figure w/ data on backend
        figure = Figure(figsize=(5,5), dpi=100) # init figure
        subp = figure.add_subplot(111) # add a plot to the figure. abc -> a x b grid, cth spot
        subp.plot(
            lis_x_axis_data,
            lis_y_axis_data
        )

        # prepare canvas w/ connection to tk to display
        canvas = FigureCanvasTkAgg(figure, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # nav tools for chart
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = Application()