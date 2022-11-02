import sys

from controller.settings import SettingsParser
from gui.mainWindow import *
from qt_material import apply_stylesheet

extra = {
    # Density Scale
    'density_scale': '2',
}

app = QtWidgets.QApplication(sys.argv)
screen_resolution = app.desktop().screenGeometry()

exit_code = 1

while exit_code == 1:
    settings = SettingsParser(app)
    settings.set_screen_res(screen_resolution)

    window = MainWindow(settings)
    window.showMaximized()

    apply_stylesheet(app, theme='dark_teal.xml', extra=extra)

    window.show()
    exit_code = app.exec_()
    window.close()
