import matplotlib
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSlider, QLayout, QLabel

matplotlib.use('Qt5Agg')
from PyQt5 import QtWidgets, QtCore
from matplotlib.figure import Figure
from controller.spline import DrawSpline
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import numpy as np


class GraphPreview(QWidget):

    def __init__(self, file_name):
        super().__init__()
        self.x, self.y, self.t, linecount = DrawSpline.get_cords(file_name)

        self.canvas = MplCanvas(width=10, height=10, dpi=100)
        self.update_plot(len(self.t) - 1)

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        self.slider = QSlider(orientation=Qt.Horizontal)
        self.slider.setMaximum(len(self.t) - 1)
        self.slider.setMinimum(0)
        self.slider.valueChanged.connect(self.__my_list_slider_valuechange__)

        self.label = QLabel()
        self.label.setText("t = " + str(self.t[-1]))
        self.label.setAlignment(Qt.AlignCenter)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def __my_list_slider_valuechange__(self, index):
        # update plot
        self.update_plot(index)
        self.label.setText("t = " + str(self.t[index]))

    def update_plot(self, max_time):
        xdata = self.x[:max_time]
        ydata = self.y[:max_time]

        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(xdata, ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


def get_max_value(axes):
    max_value = []

    for ax in axes:
        data = np.array(ax.get_ydata())
        max_value.append(np.max(data))

    return np.max(max_value)
