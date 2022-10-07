from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
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

        toolbar.addWidget(self.bttn_delete)

        self.setLayout(pagelayout)

    def on_clicked(self, index):
        self.selected_file = self.file_manager_widget.dirModel.fileInfo(index).absoluteFilePath()

        if self.selected_file == self.tmp_file:
            self.bttn_delete.setDisabled(True)
        else:
            self.bttn_delete.setDisabled(False)

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
