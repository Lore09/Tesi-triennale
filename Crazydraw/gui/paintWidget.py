import os.path
import csv
import time

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QAction, QVBoxLayout
from gui.custom_dialogs import *
from datetime import datetime


class paintMainWidget(QWidget):
    def __init__(self, xsize, ysize, saves_dir):
        super().__init__()
        pagelayout = QVBoxLayout()
        toolbar = QtWidgets.QToolBar()
        toolbar.setStyleSheet("QToolBar{spacing:30px;}");
        paint_widget = paint(xsize, ysize, saves_dir)

        pagelayout.addWidget(toolbar)
        pagelayout.addWidget(paint_widget)

        bttn_clear = QPushButton(QIcon(QDir.currentPath() + "/gui/res/icons/icons8-clear-64.png"), "Clear", self)
        bttn_clear.clicked.connect(paint_widget.clear_all)

        bttn_save = QPushButton(QIcon(QDir.currentPath() + "/gui/res/icons/icons8-save-64.png"), "Save", self)
        bttn_save.clicked.connect(paint_widget.save_data)

        toolbar.addWidget(bttn_clear)
        toolbar.addWidget(bttn_save)

        self.setLayout(pagelayout)


class paint(QtWidgets.QLabel):
    def __init__(self, xsize, ysize, saves_dir):
        super().__init__()

        self.csv_file = None
        self.file_writer = None
        self.saves_dir = QDir.currentPath() + "/" + saves_dir

        self.canvas = QtGui.QPixmap(xsize, ysize)
        self.clear_all()

        self.last_x, self.last_y, self.start_time = None, None, None

    def clear_all(self):
        self.canvas.fill(QtGui.QColor("white"))
        self.setPixmap(self.canvas)

        # Init file save
        if not os.path.isdir(self.saves_dir):
            os.mkdir(self.saves_dir)

        if self.csv_file is not None:
            self.csv_file.close()

        self.csv_file = open(self.saves_dir + "/" + "tmp.csv", mode='w')
        self.file_writer = csv.writer(self.csv_file)
        self.file_writer.writerow(["x", "y", "time"])

        self.csv_file.flush()

        self.last_x, self.last_y, self.start_time = None, None, None

    def save_data(self, s):

        dlg = SaveDialog()
        result = dlg.exec()

        if result == 1:

            filename = dlg.filename.text()
            if filename == "":
                filename = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
            filename = filename + ".csv"

            self.csv_file.close()
            old_file = self.saves_dir + "/tmp.csv"
            new_file = self.saves_dir + "/" + filename
            os.rename(old_file, new_file)

            self.csv_file = open(self.saves_dir + "/" + "tmp.csv", mode='w')
            self.file_writer = csv.writer(self.csv_file)
            self.file_writer.writerow(["x", "y", "time"])



    def mouseMoveEvent(self, e):

        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            self.start_time = time.time()
            return  # Ignore the first time.

        painter = QtGui.QPainter(self.pixmap())

        pen = painter.pen()
        pen.setWidth(2)
        pen.setColor(QtGui.QColor("#e82727"))
        painter.setPen(pen)

        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

        self.file_writer.writerow([str(self.last_x), str(self.last_y), str(time.time() - self.start_time)])

