from PyQt5.QtWidgets import QMainWindow, QHBoxLayout
from gui.fileManager import *
from gui.paintWidget import *
import controller.utils as util


class MainWindow(QMainWindow):

    def __init__(self, settings):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Crazydraw")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        draw_window = DrawWindow(settings)
        spline_window = SplineWindow(settings)

        tabs.addTab(draw_window, "Draw")
        tabs.addTab(spline_window, "Spline")

        self.setCentralWidget(tabs)


class DrawWindow(QWidget):
    def __init__(self, settings):
        super(DrawWindow, self).__init__()

        layout = QHBoxLayout()
        layout.addWidget(paintMainWidget(settings))
        layout.addWidget(FileManagerDraw(settings.get_trajectory_path()))

        self.setLayout(layout)


class SplineWindow(QWidget):

    def __init__(self, settings):
        super(SplineWindow, self).__init__()

        layout = QHBoxLayout()
        # layout.addWidget(util.get_trajectory_plot())
        layout.addWidget(FileManagerSpline(settings.get_trajectory_path()))

        self.setLayout(layout)
