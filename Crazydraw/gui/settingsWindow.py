from PyQt5.QtCore import QDir
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog


class SettingsWidget(QWidget):
    def __init__(self, settings):
        super().__init__()

        self.trajectory_file = None
        self.polynomials_label = None
        self.polynomials_value = None
        self.trajectory_label = None
        self.trajectory_value = None

        self.settings = settings

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.get_trajectory_saves())
        self.layout.addWidget(self.get_polynomial_saves())
        self.setLayout(self.layout)

    def get_trajectory_saves(self):
        row = QWidget()
        row_layout = QHBoxLayout()

        self.trajectory_label = QLabel("Trajectory files location:")
        self.trajectory_value = QLineEdit()
        self.trajectory_value.setPlaceholderText(self.settings.get_trajectory_path())

        self.trajectory_file = QPushButton(QIcon(QDir.currentPath() + "/gui/res/icons/icons8-directory-100.png"),"SELECT FILE",self)
        self.trajectory_file.clicked.connect(self.get_trajectory_file_dialog)

        row_layout.addWidget(self.trajectory_label)
        row_layout.addWidget(self.trajectory_value)
        row_layout.addWidget(self.trajectory_file)

        row.setLayout(row_layout)

        return row

    def get_polynomial_saves(self):
        row = QWidget()
        row_layout = QHBoxLayout()

        self.polynomials_label = QLabel("Polynomials files location:")
        self.polynomials_value = QLineEdit()
        self.polynomials_value.setPlaceholderText(self.settings.get_polynomials_path())

        self.polynomials_file = QPushButton(QIcon(QDir.currentPath() + "/gui/res/icons/icons8-directory-100.png"),
                                           "SELECT FILE", self)
        self.polynomials_file.clicked.connect(self.get_polynomial_file_dialog)

        row_layout.addWidget(self.polynomials_label)
        row_layout.addWidget(self.polynomials_value)
        row_layout.addWidget(self.polynomials_file)

        row.setLayout(row_layout)

        return row

    def get_trajectory_file_dialog(self):
        return str(QFileDialog.getExistingDirectory(self, "Select Directory"))

    def get_polynomial_file_dialog(self):
        return str(QFileDialog.getExistingDirectory(self, "Select Directory"))