import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from controller.spline import DrawSpline
from gui.custom_dialogs import DeleteDialog
from controller.utils import *
from gui.splineWidget import SplineWidget


class FileManager(QWidget):
    def __init__(self, rel_path):
        super().__init__()
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


class FileManagerMain(QWidget):

    def __init__(self, rel_path):
        super().__init__()

        self.selected_file = None
        self.tmp_file = QDir.currentPath() + "/" + rel_path + "/tmp.csv"
        self.pagelayout = QVBoxLayout()
        self.toolbar = QtWidgets.QToolBar()
        self.toolbar.setStyleSheet("QToolBar{spacing:5px;}")
        self.file_manager_widget = FileManager(rel_path)

        self.pagelayout.addWidget(self.toolbar)
        self.pagelayout.addWidget(self.file_manager_widget)

        self.bttn_delete = QPushButton(QIcon(QDir.currentPath() + "/gui/res/icons/icons8-delete-64.png"), "", self)
        self.bttn_delete.setDisabled(True)
        self.bttn_delete.setFixedSize(70, 70)
        self.toolbar.addWidget(self.bttn_delete)

        self.setLayout(self.pagelayout)


class FileManagerDraw(FileManagerMain):

    def __init__(self, rel_path):
        super().__init__(rel_path)

        self.bttn_preview = QPushButton("PREVIEW", self)
        self.bttn_preview.clicked.connect(self.preview_trajectory)
        self.bttn_preview.setDisabled(True)
        self.bttn_preview.setFixedHeight(70)
        self.toolbar.addWidget(self.bttn_preview)

        self.bttn_delete.clicked.connect(self.delete_file)
        self.file_manager_widget.treeview.clicked.connect(self.on_clicked)

    def delete_file(self):

        dlg = DeleteDialog(self.selected_file)

        if dlg.exec() == QMessageBox.Yes:
            os.remove(self.selected_file)
            self.bttn_delete.setDisabled(True)
            self.bttn_preview.setDisabled(True)

    def on_clicked(self, index):
        self.selected_file = self.file_manager_widget.dirModel.fileInfo(index).absoluteFilePath()

        if self.selected_file == self.tmp_file:
            self.bttn_delete.setDisabled(True)
            self.bttn_preview.setDisabled(True)
        else:
            self.bttn_delete.setDisabled(False)
            self.bttn_preview.setDisabled(False)

    def preview_trajectory(self):
        dlg = QDialog(self)
        preview = GraphPreview(self.selected_file)
        layout = QVBoxLayout()
        layout.addWidget(preview)
        dlg.setWindowTitle("Preview!")
        dlg.setLayout(layout)
        dlg.exec()


class FileManagerSpline(FileManagerMain):

    def __init__(self, rel_path):
        super().__init__(rel_path)

        self.bttn_spline = QPushButton("SPLINE", self)
        self.bttn_spline.setDisabled(True)
        self.bttn_spline.setFixedHeight(70)
        self.toolbar.addWidget(self.bttn_spline)

        self.bttn_delete.clicked.connect(self.delete_file)
        self.file_manager_widget.treeview.clicked.connect(self.on_clicked)

    def delete_file(self):

        dlg = DeleteDialog(self.selected_file)

        if dlg.exec() == QMessageBox.Yes:
            os.remove(self.selected_file)
            self.bttn_delete.setDisabled(True)
            self.bttn_spline.setDisabled(True)

    def on_clicked(self, index):
        self.selected_file = self.file_manager_widget.dirModel.fileInfo(index).absoluteFilePath()

        if self.selected_file == self.tmp_file:
            self.bttn_delete.setDisabled(True)
            self.bttn_spline.setDisabled(True)
        else:
            self.bttn_delete.setDisabled(False)
            self.bttn_spline.setDisabled(False)