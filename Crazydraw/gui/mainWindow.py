from PyQt5.QtWidgets import QMainWindow, QHBoxLayout
from gui.fileManager import *
from gui.paintWidget import *

class MainWindow(QMainWindow):

    def __init__(self,settings):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Crazydraw")

        layout = QHBoxLayout()
        layout.addWidget(paintMainWidget(settings))
        layout.addWidget(FileManagerMain(settings.get_trajectory_path()))

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

