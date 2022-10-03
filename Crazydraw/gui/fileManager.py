from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class FileManagerMain(QWidget):

    def __init__(self,rel_path):
        super().__init__()
        pagelayout = QHBoxLayout()
        toolbar = QtWidgets.QToolBar()
        toolbar.setStyleSheet("QToolBar{spacing:5px;}")
        file_manager_widget = FileManager(rel_path)

        pagelayout.addWidget(file_manager_widget)
        pagelayout.addWidget(toolbar)

        bttn_clear = QPushButton(QIcon(QDir.currentPath() + "/gui/res/icons/icons8-clear-64.png"), "Clear", self)

        toolbar.addWidget(bttn_clear)

        self.setLayout(pagelayout)

class FileManager(QWidget):
    def __init__(self,rel_path):
        QWidget.__init__(self)
        hlay = QHBoxLayout(self)
        self.treeview = QListView()
        hlay.addWidget(self.treeview)

        path = QDir.currentPath()+"/"+rel_path

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setFilter(QDir.NoDotAndDotDot |  QDir.Files)

        self.treeview.setModel(self.dirModel)
        self.treeview.setRootIndex(self.dirModel.index(path))
        self.treeview.clicked.connect(self.on_clicked)

        self.treeview.setFixedWidth(300)

    def on_clicked(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        print(path)
