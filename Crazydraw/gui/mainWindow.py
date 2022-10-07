from PyQt5.QtWidgets import QMainWindow, QHBoxLayout
from gui.fileManager import *
from gui.paintWidget import *

class MainWindow(QMainWindow):

    def __init__(self,settings):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Crazydraw")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        draw_window = DrawWindow(settings)

        tabs.addTab(draw_window,"Draw")


        self.setCentralWidget(tabs)



class DrawWindow(QWidget):
    def __init__(self,settings):
        super(DrawWindow, self).__init__()

        layout = QHBoxLayout()
        layout.addWidget(paintMainWidget(settings))
        layout.addWidget(FileManagerMain(settings.get_trajectory_path()))

        self.setLayout(layout)
