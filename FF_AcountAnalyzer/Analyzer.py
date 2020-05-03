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
    root = None
    text_fileName = None
    button_file_chooser = None
    file = None

    # CLASS CONSTANTS


    def __init__(self):
        '''
        starting point of app
        :return: N/A
        '''
        # create GUI root
        self.root = tk.Tk()
        self.root.title(string="First Financial Checking Account Data Analyzer")

        # attach button for file dialog
        self.button_file_chooser = tk.Button(self.root, text='Choose file', command=self.get_file_path)
        self.button_file_chooser.pack()

        # attach Text field for initial date range
        #self.text_initial_date = tk.Text(self.root, )
        #self.text_initial_date.pack()

        # attach text to display file path
        self.text_fileName = tk.Label(self.root, text='')
        self.text_fileName.pack()

        # attach button to do analysis
        self.button_analyze = tk.Button(self.root, text='Analyze Data', command=self.analyze)
        self.button_analyze.pack()

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

    def analyze(self):
        chart = Chart(self.root, 'Balance Over Time', self.file.get_file_contents(), 'Post Date', 'Balance')
        chart.pack()


class Chart(tk.Frame):

    df_data = None
    chart_title = ''

    def __init__(self, tk_parent, chart_title, df, x_axis_ind, y_axis_ind):
        tk.Frame.__init__(self, tk_parent)
        self.df_data = df
        self.chart_title = chart_title

        # init figure w/ data on backend
        f = Figure(figsize=(5,5), dpi=100) # init figure
        subp = f.add_subplot(111) # add a plot to the figure. 1x1, 1st chart spot
        subp.plot(
            df[x_axis_ind].tolist()[::-1], # [::-1] reverses the list -> most recent data is at top of file by default
            df[y_axis_ind].tolist()[::-1]
        )

        # prepare canvas w/ connection to tk to display
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # nav tools for chart
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = Application()