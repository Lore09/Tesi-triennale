import sys
from gui.mainWindow import *
from controller.settings import SettingsParser
from qt_material import apply_stylesheet
from controller.spline import *

app = QtWidgets.QApplication(sys.argv)

settings = SettingsParser()

window = MainWindow(settings)
window.setFixedSize(settings.get_paint_size_scaled()[0] + 500, 800)

apply_stylesheet(app, theme='dark_red.xml')

DrawSpline.plot_cubic_spline("saves/palle.csv")

window.show()

app.exec_()
