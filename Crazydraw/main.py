import sys
from gui.mainWindow import *
from controller.settings import SettingsParser
from qt_material import apply_stylesheet

app = QtWidgets.QApplication(sys.argv)

settings = SettingsParser()

window = MainWindow(settings)
window.setFixedSize(settings.get_paint_size_scaled()[0] + 500, 800)

apply_stylesheet(app, theme='dark_blue.xml')

window.show()

app.exec_()
