from PyQt5.QtWidgets import QMainWindow, QHBoxLayout
from gui.fileManager import *
from gui.paintWidget import *
from gui.settingsWindow import SettingsWidget
from gui.rosWidget import *
import controller.utils as util
from gui.splineWidget import *


class MainWindow(QMainWindow):

    def __init__(self, settings):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Crazydraw")
        self.setWindowIcon(QtGui.QIcon(QDir.currentPath() + '/gui/res/icons/drone.png'))

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)

        draw_window = DrawWindow(settings)
        spline_window = SplineWindow(settings)
        ros_window = RosWindow(settings)
        settings_window = SettingsWidget(settings)

        tabs.addTab(draw_window, "Draw")
        tabs.addTab(spline_window, "Spline")
        tabs.addTab(ros_window, "ROS")
        tabs.addTab(settings_window, "Settings")

        self.setCentralWidget(tabs)


class DrawWindow(QWidget):
    def __init__(self, settings):
        super(DrawWindow, self).__init__()

        layout = QHBoxLayout()

        paintWidget = paintMainWidget(settings)

        fileManager = FileManagerDraw(settings.get_trajectory_path())

        layout.addWidget(paintWidget)
        layout.addWidget(fileManager)

        self.setLayout(layout)


class SplineWindow(QWidget):

    def __init__(self, settings):
        super(SplineWindow, self).__init__()

        layout = QHBoxLayout()
        self.settings = settings

        self.file_manager = FileManagerSpline(settings)
        self.spline_widget = SplineWidget(settings)

        self.file_manager.bttn_spline.clicked.connect(self.plot_spline)
        self.file_manager.bttn_save.clicked.connect(self.save_spline)
        self.file_manager.bttn_compare.clicked.connect(self.plot_comparison)

        layout.addWidget(self.file_manager)
        layout.addWidget(self.spline_widget)

        self.setLayout(layout)

    def plot_spline(self):
        self.spline_widget.plot_spline(self.file_manager.selected_file, self.file_manager.time_scale)

    def save_spline(self):
        self.spline_widget.save_spline(self.file_manager.selected_file,
                                       self.settings.get_polynomials_path(),
                                       30)
    def plot_comparison(self):
        self.spline_widget.plot_comparison(self.file_manager.selected_file, self.file_manager.time_scale)

class RosWindow(QWidget):

    def __init__(self, settings):
        super(RosWindow, self).__init__()

        layout = QHBoxLayout()
        file_manager = FileManagerRos(settings.get_trajectory_path())
        ros_widget = RosWidget()

        layout.addWidget(file_manager)
        layout.addWidget(ros_widget)

        self.setLayout(layout)

    def fly(self):
        return
