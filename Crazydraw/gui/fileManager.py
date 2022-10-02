from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QListView


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

        self.treeview.setFixedWidth(400)

    def on_clicked(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        print(path)
