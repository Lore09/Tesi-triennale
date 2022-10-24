import yaml
import io
import os

from PyQt5.QtCore import QDir


class SettingsParser:
    def __init__(self):

        self.paint_widget_size = None
        with open(QDir.currentPath() + "/settings.yaml") as stream:
            try:
                self.data = yaml.safe_load(stream)
                print(self.data)
            except yaml.YAMLError as exc:
                print(exc)

        self.screen_res = None

        self.trajectory_path = QDir.currentPath() + "/" + self.data["data_storage"]["trajectory_directory"]
        self.polynomials_path = QDir.currentPath() + "/" + self.data["data_storage"]["polynomials_directory"]

        if not os.path.isdir(self.trajectory_path):
            os.makedirs(self.trajectory_path)

        if not os.path.isdir(self.polynomials_path):
            os.makedirs(self.polynomials_path)
    def get_screen_res(self):
        return self.screen_res

    def set_screen_res(self,screen_res):
        self.screen_res = screen_res

        size = self.data["area_settings"]["paint_square_size"]

        self.paint_widget_size = []
        self.paint_widget_size.append(int(size[0] * screen_res.height()*2/3 / size[1]))
        self.paint_widget_size.append(int(screen_res.height()*2/3))

    def get_paint_size_scaled(self):

        return self.paint_widget_size

    def get_area_size_meters(self):

        return self.data["area_settings"]["paint_square_size"]

    def get_trajectory_path(self):
        return self.trajectory_path

    def get_polynomials_path(self):
        return self.polynomials_path

    def get_scale_factor(self):

        x_size, y_size = self.get_area_size_meters()
        x_widget, y_widget = self.get_paint_size_scaled()

        y_dist = int(y_widget / y_size)
        x_dist = int(x_widget / x_size)

        if x_dist == y_dist:
            return x_dist
        else:
            return 0
