from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from controller.utils import MplCanvas
from controller.spline import DrawSpline


class SplineWidget(QWidget):

    def __init__(self):
        super(SplineWidget, self).__init__()
        self.canvas = None
        self.file_name = None

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def plot_spline(self, file_name):

        if file_name is not None:
            self.layout.removeWidget(self.canvas)
            self.canvas = MplCanvasSpline(width=10, height=10, dpi=100)
            DrawSpline.plot_cubic_spline(file_name,self.canvas.fig,self.canvas.axes)
            #self.layout = QVBoxLayout()
            self.layout.addWidget(self.canvas)
            self.setLayout(self.layout)


class MplCanvasSpline(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = []
        self.axes.append(self.fig.add_subplot(211))
        self.axes.append(self.fig.add_subplot(212))
        super(MplCanvasSpline, self).__init__(self.fig)