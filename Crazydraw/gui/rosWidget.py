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

        self.bttn_hover = QPushButton(QIcon(QDir.currentPath() + "/gui/res/icons/drone.png"), "HOVER", self)
        self.bttn_land = QPushButton("LAND", self)
        self.bttn_stop = QPushButton("STOP", self)
        self.bttn_plot = QPushButton("PLOT", self)

        top_toolbar.addWidget(self.bttn_hover)
        top_toolbar.addWidget(QLabel("Height:"))
        self.hover_height = QLineEdit()
        self.hover_height.setFixedWidth(50)
        self.hover_height.setText(str(1))
        top_toolbar.addWidget(self.hover_height)
        
        top_toolbar.addWidget(self.bttn_land)
        top_toolbar.addWidget(self.bttn_stop)
        top_toolbar.addWidget(self.bttn_plot)

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