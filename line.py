import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import pandas as pd
download_url = ("https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv")

df = pd.read_csv(download_url)

print(df.head())

rcParams["figure.figsize"]= 10,10

df.plot(x="Rank", y=["Full_time", "Part_time", "Unemployment_rate"], kind="line")

plt.grid(True, color="k", linestyle=":")

plt.show()




class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # Create the maptlotlib FigureCanvas object, 
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        # Create our pandas DataFrame with some simple
        # data and headers.
        df = pd.DataFrame(["Rank"], columns=["Full_time", "Part_time", "Unemployment_rate"])
        df = pd.read_csv(download_url)

        # plot the pandas DataFrame, passing in the 
        # matplotlib Canvas axes.
        df.plot(ax=sc.axes)

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()

