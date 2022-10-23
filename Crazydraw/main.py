import sys
from gui.mainWindow import *
from controller.settings import SettingsParser
from qt_material import apply_stylesheet
from controller.spline import *

extra = {
    # Density Scale
    'density_scale': '2',
}

app = QtWidgets.QApplication(sys.argv)
screen_resolution = app.desktop().screenGeometry()

settings = SettingsParser()
settings.set_screen_res(screen_resolution)

window = MainWindow(settings)
window.showMaximized()
#window.setFixedSize(settings.get_paint_size_scaled()[0] + 500, 800)

apply_stylesheet(app,theme='dark_teal.xml',extra=extra)

window.show()

app.exec_()
