from PyQt5 import QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton


class RosWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        bttn_hover = QPushButton(QIcon(QDir.currentPath() + "/gui/res/icons/drone.png"), "HOVER", self)
        layout.addWidget(bttn_hover)

        self.setLayout(layout)