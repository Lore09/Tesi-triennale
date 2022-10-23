from PyQt5.QtWidgets import QMainWindow, QHBoxLayout
from gui.fileManager import *
from gui.paintWidget import *
from gui.settingsWindow import SettingsWidget
import controller.utils as util
import gui.splineWidget


class MainWindow(QMainWindow):

    def __init__(self, settings):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Crazydraw")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)

        draw_window = DrawWindow(settings)
        spline_window = SplineWindow(settings)
        settings_window = SettingsWidget(settings)

        tabs.addTab(draw_window, "Draw")
        tabs.addTab(spline_window, "Spline")
        tabs.addTab(settings_window, "Settings")

        #TODO editor settings

        self.setCentralWidget(tabs)


class DrawWindow(QWidget):
    def __init__(self, settings):
        super(DrawWindow, self).__init__()

        layout = QHBoxLayout()

        paintWidget = paintMainWidget(settings)

        fileManager= FileManagerDraw(settings.get_trajectory_path())

        layout.addWidget(paintWidget)
        layout.addWidget(fileManager)

        self.setLayout(layout)


class SplineWindow(QWidget):

    def __init__(self, settings):
        super(SplineWindow, self).__init__()

        layout = QHBoxLayout()
        self.settings = settings

        self.file_manager = FileManagerSpline(settings.get_trajectory_path())
        self.spline_widget = SplineWidget(settings)

        self.file_manager.bttn_spline.clicked.connect(self.plot_spline)
        self.file_manager.bttn_save.clicked.connect(self.save_spline)

        layout.addWidget(self.file_manager)
        layout.addWidget(self.spline_widget)

        self.setLayout(layout)

    def plot_spline(self):
        self.spline_widget.plot_spline(self.file_manager.selected_file)

    def save_spline(self):
        self.spline_widget.save_spline(self.file_manager.selected_file,
                                           self.settings.get_polynomials_path(),
                                           30)