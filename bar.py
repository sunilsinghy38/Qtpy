import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

w=0.4
plt.style.use('bmh')
download_url = ("https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv")
df = pd.read_csv(download_url)
x = df['Rank']
college_job = df['College_jobs']
non_college_job = df['Non_college_jobs']
bar1 = np.arange(len(x))
bar2 = [i+w for i in bar1]
plt.bar(bar1,college_job,w,label="college_job")
plt.bar(bar2,non_college_job,w,label="non_college_job")

plt.xlabel('College Rank')
plt.ylabel("Jobs")
plt.legend()
plt.xticks(bar1,x)
plt.show()

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

#        hour = [1,2,3,4,5,6,7,8,9,10]
 #       temperature = [30,32,34,32,33,31,29,32,35,45]

        # plot data: x, y values
        self.graphWidget.plot(bar1, bar2)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

