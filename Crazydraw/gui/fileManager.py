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

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.Files |QDir.Writable | QDir.Readable)

        self.treeview.setModel(self.dirModel)
        self.treeview.setRootIndex(self.dirModel.index(rel_path))

        self.treeview.setMinimumWidth(350)
        self.treeview.setMaximumWidth(600)


class FileManagerMain(QWidget):

    def __init__(self, rel_path):
        super().__init__()

        self.selected_file = None
        self.tmp_file = rel_path + "/.tmp.csv"
        self.pagelayout = QVBoxLayout()
        self.toolbar = QtWidgets.QToolBar()
        self.toolbar.setStyleSheet("QToolBar{spacing:5px;}")
        self.file_manager_widget = FileManager(rel_path)

        self.pagelayout.addWidget(self.toolbar)
        self.pagelayout.addWidget(self.file_manager_widget)

        self.bttn_delete = QPushButton(QIcon(QDir.currentPath() + "/gui/res/icons/icons8-rimuovere-100.png"), "DELETE", self)
        self.bttn_delete.setDisabled(True)
        self.bttn_delete.setFixedHeight(70)
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

        self.bttn_save = QPushButton("SAVE", self)
        self.bttn_save.setDisabled(True)
        self.bttn_save.setFixedHeight(70)
        self.toolbar.addWidget(self.bttn_save)

        self.bttn_delete.clicked.connect(self.delete_file)
        self.file_manager_widget.treeview.clicked.connect(self.on_clicked)

    def delete_file(self):

        dlg = DeleteDialog(self.selected_file)

        if dlg.exec() == QMessageBox.Yes:
            os.remove(self.selected_file)
            self.bttn_delete.setDisabled(True)
            self.bttn_spline.setDisabled(True)
            self.bttn_save.setDisabled(True)

    def on_clicked(self, index):
        self.selected_file = self.file_manager_widget.dirModel.fileInfo(index).absoluteFilePath()

        if self.selected_file == self.tmp_file:
            self.bttn_delete.setDisabled(True)
            self.bttn_spline.setDisabled(True)
            self.bttn_save.setDisabled(True)
        else:
            self.bttn_delete.setDisabled(False)
            self.bttn_spline.setDisabled(False)
            self.bttn_save.setDisabled(False)


class FileManagerRos(FileManagerMain):

    def __init__(self, rel_path):
        super().__init__(rel_path)

        self.bttn_fly = QPushButton("SEND TRAJECTORY", self)
        self.bttn_fly.setDisabled(True)
        self.bttn_fly.setFixedHeight(70)
        self.toolbar.addWidget(self.bttn_fly)

        self.bttn_fly.clicked.connect(self.delete_file)
        self.file_manager_widget.treeview.clicked.connect(self.on_clicked)

    def delete_file(self):

        dlg = DeleteDialog(self.selected_file)

        if dlg.exec() == QMessageBox.Yes:
            os.remove(self.selected_file)
            self.bttn_delete.setDisabled(True)
            self.bttn_fly.setDisabled(True)

    def on_clicked(self, index):
        self.selected_file = self.file_manager_widget.dirModel.fileInfo(index).absoluteFilePath()

        if self.selected_file == self.tmp_file:
            self.bttn_delete.setDisabled(True)
            self.bttn_fly.setDisabled(True)
        else:
            self.bttn_delete.setDisabled(False)
            self.bttn_fly.setDisabled(False)
