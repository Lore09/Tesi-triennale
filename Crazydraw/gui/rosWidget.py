from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QLineEdit


class RosWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(50)

        top_toolbar = QHBoxLayout()

        bttn_hover = QPushButton(QIcon(QDir.currentPath() + "/gui/res/icons/drone.png"), "HOVER", self)
        bttn_land = QPushButton("LAND", self)
        top_toolbar.addWidget(bttn_hover)
        top_toolbar.addWidget(bttn_land)

        layout.addLayout(top_toolbar)
        layout.addSpacing(100)

        # Direct command tool
        layout.addWidget(QLabel("Send direct command"))

        row = QHBoxLayout()
        row.addWidget(QLabel("ID:"))
        row.addWidget(QLineEdit())
        layout.addLayout(row)

        row = QHBoxLayout()
        row.addWidget(QLabel("x:"))
        row.addWidget(QLineEdit())
        layout.addLayout(row)

        row = QHBoxLayout()
        row.addWidget(QLabel("y:"))
        row.addWidget(QLineEdit())
        layout.addLayout(row)

        row = QHBoxLayout()
        row.addWidget(QLabel("z:"))
        row.addWidget(QLineEdit())
        layout.addLayout(row)

        row = QHBoxLayout()
        row.addWidget(QLabel("time (seconds):"))
        row.addWidget(QLineEdit())
        layout.addLayout(row)

        layout.addWidget(QPushButton("SEND DIRECT COMMAND"))

        self.setLayout(layout)