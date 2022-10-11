from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from controller.spline import DrawSpline
import os


class FileManagerMain(QWidget):

    def __init__(self, rel_path):
        super().__init__()

        self.selected_file = None
        self.tmp_file = QDir.currentPath() + "/" + rel_path + "/tmp.csv"
        pagelayout = QHBoxLayout()
        toolbar = QtWidgets.QToolBar()
        toolbar.setStyleSheet("QToolBar{spacing:5px;}")
        self.file_manager_widget = FileManager(rel_path)
        self.file_manager_widget.treeview.clicked.connect(self.on_clicked)

        pagelayout.addWidget(self.file_manager_widget)
        pagelayout.addWidget(toolbar)

        self.bttn_delete = QPushButton(QIcon(QDir.currentPath() + "/gui/res/icons/icons8-delete-64.png"), "", self)
        self.bttn_delete.clicked.connect(self.delete_file)
        self.bttn_delete.setDisabled(True)
        self.bttn_delete.setFixedSize(60,100)

        self.bttn = QPushButton("SPLINE", self)
        self.bttn.clicked.connect(self.print_spline)
        self.bttn.setDisabled(True)
        self.bttn.setFixedSize(60, 100)

        toolbar.addWidget(self.bttn_delete)
        toolbar.addWidget(self.bttn)

        self.setLayout(pagelayout)

    def on_clicked(self, index):
        self.selected_file = self.file_manager_widget.dirModel.fileInfo(index).absoluteFilePath()

        if self.selected_file == self.tmp_file:
            self.bttn_delete.setDisabled(True)
            self.bttn.setDisabled(True)
        else:
            self.bttn_delete.setDisabled(False)
            self.bttn.setDisabled(False)

    def print_spline(self):
        DrawSpline.plot_cubic_spline(self.selected_file)

    def delete_file(self):
        os.remove(self.selected_file)
        self.bttn_delete.setDisabled(True)


class FileManager(QWidget):
    def __init__(self, rel_path):
        QWidget.__init__(self)
        hlay = QHBoxLayout(self)
        self.treeview = QListView()
        hlay.addWidget(self.treeview)

        path = QDir.currentPath() + "/" + rel_path

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.Files)

        self.treeview.setModel(self.dirModel)
        self.treeview.setRootIndex(self.dirModel.index(path))

        self.treeview.setFixedWidth(250)
